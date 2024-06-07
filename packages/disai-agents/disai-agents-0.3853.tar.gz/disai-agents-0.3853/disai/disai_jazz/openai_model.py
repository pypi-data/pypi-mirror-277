#  disai_jazz/openai_model.py
import openai
from newspaper import Article
import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
import datetime
import sqlite3


load_dotenv()

class OpenAIModel:
    def __init__(self, api_key=None, model=None,chat_history=[]):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        openai.api_key = self.api_key
        self.client = openai.OpenAI(api_key=openai.api_key)
        self.model = model
        self.chat_history=chat_history
        task = (
                "I am a knowledgeable assistant and chatbot. However, my dataset lasts only till 2021 and I will explicitly reply only with 'google: <search query>' if I do not have the information."
                'Todays date is '+str(datetime.datetime.now().date())+' I will also check if you are asking me about future events and reply accordingly with a google search aswell'
                'If the question requires knowledge that I do not know about, I will explicitly reply only with "google: <search query>". Then you will provide me with relevant context after the google search along with query.'
        )
        self.chat_history.append({"role": "system", "content": task})

    #agent to generate images
    def generate_image(self, prompt):
        response = self.client.images.generate(
            prompt=prompt,
            n=1,
            model=self.model,
            size="1024x1024",
            quality="standard",
        )
        return response.data[0].url
    
    #agent that has access to internet
    def search(self,input_query):
        user_query = input_query.replace(' ', '+')
        URL = "https://www.google.co.in/search?q=" + user_query

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57'
        }

        try:
            page = requests.get(URL, headers=headers)
            soup = BeautifulSoup(page.content, 'html.parser')
            
            # Get the entire text content of the page
            text_content = soup.get_text()
            
            # Find the index where the relevant information starts
            start_index = text_content.find("Search Results") + len("Search Results")
            
            # Print the relevant information
            return(text_content[start_index:].strip())
        except:
            return "An error occurred while fetching the search results. Please try again later."

        
    def webagent(self,prompt):
        try:
            # Step 1: Initial instruction to the LLM
            initial_prompt = f"{prompt}"
            self.chat_history.append({"role": "user", "content": initial_prompt})

            # Step 2: Attempt to generate a response
            response = self.client.chat.completions.create(
                temperature=0,
                model=self.model,
                messages=self.chat_history
            )
            result = response.choices[0].message.content


            # Step 3: Check for search request
            if result.strip().lower().startswith("google:"):
                search_query = result[len("google:"):].strip()
                search_results = self.search(search_query)
                #print(search_results)


                # Step 4: Refine the prompt with search results
                refined_prompt = f"The question is: {prompt} 'and the google'd information is:'\n{search_results}"
                self.chat_history.append({"role": "user", "content": refined_prompt})
                refined_response = self.client.chat.completions.create(
                    temperature=0.3,
                    model=self.model,
                    messages=self.chat_history
                )
                final_result = refined_response.choices[0].message.content

                return final_result
            else:
                task = (
                        "I am a knowledgeable assistant and chatbot. However, my dataset lasts only till 2021 and I will explicitly reply only with 'google: <search query>' if I do not have the information."
                        'before I reply I will see if you are talking to me like a conversation or asking a question, if you are asking a question I will try to answer it.'
                        'If I do not have the information, I will explicitly reply only with "google: <your search query>". Then you will provide me with relevant context after the google search along with query.'
                )
                self.chat_history.append({"role": "system", "content": task})

                return result
        except Exception as e:
            return {"error": str(e)}    

        # Function to get a response from OpenAI with a limited context
    def get_response(self,question, context):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                    {"role": "system", "content": context},
                    {"role": "user", "content": question}
                ]
            )
        return response.choices[0].message.content.strip()
    
    def talk_to_website(self,website_link, prompt):
        def extract_text_from_url(url):
            article = Article(url)
            article.download()
            article.parse()
            return article.text

        try:
            # Extract text from the website
            content = extract_text_from_url(website_link)
            f"You are an expert in analyzing website content and answering questions based on the provided content. Here is the context: {content}"
            #print(content)
            answer = self.get_response(question=prompt, context=content)
            return answer
        except Exception as e:
            return f"An error occurred: {e}"

    def get_db_schema(self,db_path):
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cur.fetchall()
        schema = {}
        for table in tables:
            table_name = table[0]
            cur.execute(f"PRAGMA table_info({table_name});")
            columns = cur.fetchall()
            schema[table_name] = [col[1] for col in columns]
        conn.close()
        return schema

    # Function to create prompt dynamically
    def create_prompt(self,schema):
        schema_str = "The database schema is as follows:\n"
        for table, columns in schema.items():
            schema_str += f"Table {table} with columns {', '.join(columns)}.\n"
        return f"You are an expert in converting English questions to SQL query! {schema_str}\nFor example,\nExample 1 - How many entries of records are present in STUDENT?, the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ; \nExample 2 - Tell me all the students studying in Data Science class in STUDENT?, the SQL command will be something like this SELECT * FROM STUDENT where CLASS='Data Science'; also the sql code should not have ``` in beginning or end and sql word in output"

    # Function to load Google Gemini Model and provide queries as response
    def get_response(self,question, prompt):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": question}
            ]
        )
        return response.choices[0].message.content

    # Function to retrieve query from the database
    def read_sql_query(self,sql, db_path):
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        conn.commit()
        conn.close()
        return rows

