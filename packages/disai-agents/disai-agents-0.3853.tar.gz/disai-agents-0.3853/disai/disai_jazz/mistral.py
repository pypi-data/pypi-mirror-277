#  disai_jazz/mistral.py
import requests
import json
from bs4 import BeautifulSoup
from duckduckgo_search import DDGS
class Mistral():
    def __init__(self,model=None,chat_history=[]):
        self.model = model
        self.chat_history=chat_history

    #agent that has access to internet
    def search(self,input_query):
        results = DDGS().text(input_query, max_results=10)  
        return str(results)
        
    def webagent(self,prompt):
        self.chat_history.append({
            "role": "user",
            "content": prompt
        })
        url = "http://localhost:11434/api/chat"
        payload = {"model": "mistral", "messages": self.chat_history}
        headers = {"Content-Type": "application/json"}

        response = requests.post(url, json=payload, headers=headers, stream=True)

        if response.status_code == 200:
            content = ""
            total = " "
            for line in response.iter_lines():
                if line:
                    line_data = json.loads(line.decode('utf-8'))
                    content = line_data.get("message", {}).get("content", "")
                    total+=content
                    yield content
            self.chat_history.append({
                "role": "assistant",
                "content": total
            })
