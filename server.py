from fastapi import FastAPI,Path
from typing import Optional
from pydantic import BaseModel

import nltk
from nltk.chat.util import Chat, reflections


app=FastAPI()

# Define the conversation pairs
pairs = [
    ['hi', ['Hello! I am Selina, a low-key personal assistant developed by Dheeraj. How can I help you today?']],
    ['(.*) you', ['My name is Selina.A chatbot created by Dheeraj']],
    ['(.*) name', ['My name is Selina.A chatbot created by Dheeraj']],['(.*) about', ['He is experienced in web development and related frameworks, and that he is interested in AI. he also like coffee, anime, fitness, and gaming.']],
    ['(.*) about', ['He is experienced in web development and related frameworks, and that he is interested in AI. he also like coffee, anime, fitness, and gaming.']],
    ['(.*) your', ['He is experienced in web development and related frameworks, and that he is interested in AI. he also like coffee, anime, fitness, and gaming.']],
    ['(.*) Dheeraj', ['He is experienced in web development and related frameworks, and that he is interested in AI. he also like coffee, anime, fitness, and gaming.']],
    ['(.*) creator', ['He is experienced in web development and related frameworks, and that he is interested in AI. he also like coffee, anime, fitness, and gaming.']],
    ['(.*) project', ['his current projects include a cloud-based blog that uses authentication and data storage in the cloud, and a chatbot for booking a service. He is also working on a project using gesture recognition.']],
    ['(.*) contact', ['You can contact the creator by the profiles given below.']],
    ['(.*)', ['Sorry, I do not understand what you are saying.']]
]

# Create the chatbot
chatbot = Chat(pairs, reflections)

@app.get("/chat")
def get(query:str):
    print(query)
    response = chatbot.respond(query)
    return {"response":response}
              
