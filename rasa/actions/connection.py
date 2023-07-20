from pymongo import MongoClient
import openai


def get_database():
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   CONNECTION_STRING = "url-mongodb"
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING)
 
   # Create the database for our example (we will use the same database throughout the tutorial
   return client['TCC']

def get_chatgpt_response(prompt):
    print(prompt)
    api_key = "chave-api-gpt3"
    openai.api_key = api_key
    messages = []
    if prompt:
        messages.append({"role": "user", "content": prompt})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k-0613",  # Especifique o mecanismo do modelo adequado para ChatGPT
            messages=messages,
        )
        print(response)

    return response.choices[0].message.content