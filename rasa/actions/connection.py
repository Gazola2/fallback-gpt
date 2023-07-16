from pymongo import MongoClient
from .env import MONGOURL
import openai


def get_database():
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   CONNECTION_STRING = "mongodb+srv://yggor1:<zCAXBeG75koc4Urj>@cluster0.pqiu2wh.mongodb.net/"
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING)
 
   # Create the database for our example (we will use the same database throughout the tutorial
   return client['TCC']

def get_chatgpt_response(prompt):
    api_key = "sua_chave_de_api_aqui"
    openai.api_key = api_key
    response = openai.Completion.create(
        engine="text-davinci-002",  # Especifique o mecanismo do modelo adequado para ChatGPT
        prompt=prompt,
        max_tokens=150,  # Defina o máximo de tokens na resposta
        stop=None  # Você pode adicionar palavras para parar a resposta mais cedo, se desejar
    )
    return response.choices[0].text.strip()