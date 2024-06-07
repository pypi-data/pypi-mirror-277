#  disai_jazz/arch.py
class SequentialFlow:
    def __init__(self, agent, model):
        self.agent = agent
        self.model = model

    def generate_prompt(self, user_prompt):
        return f"{self.agent} {user_prompt}"

    def gen_image(self, user_prompt):
        full_prompt = self.generate_prompt(user_prompt)
        return self.model.generate_image(full_prompt)
    
    def web_agent(self,user_prompt):
        #full_prompt = self.generate_prompt(user_prompt)
        return self.model.webagent(user_prompt)
    
    def mistral_webagent(self,user_prompt,search_context):
        #context = self.model.search_context(user_prompt)
        full_message=user_prompt+"#### here is the context from internet, use if needed(reply with I've searched the internet):"+search_context
        return self.model.webagent(full_message)

    def mistral_duckduckgo(self,user_prompt):
        return self.model.search(user_prompt)
    
    def talk_to_website(self,website_link, prompt):
        return self.model.talk_to_website(website_link, prompt)
    
    def sql_intiate(self,path):
        schema = self.model.get_db_schema(path)
        return self.model.create_prompt(schema)
    
    def sql_query(self,question,prompt,path):
        response = self.model.get_response(question,prompt)
        query_result = self.model.read_sql_query(response,path)
        return [response,query_result]
    
        
