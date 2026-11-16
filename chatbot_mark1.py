"""
Créditos al Youtuber ABS Code, https://www.youtube.com/watch?v=uBwh11RWtuE&list=PLO4cXZGABhxLa81Ggje9FdFLSM_OzjtH0

Este mini proyecto esta hecho con fines educativos e informativos, sobre la creación
de un chatbot para soporte. 
Este proyecto se ira puliendo con mayor información y mejores tecnologías con el paso
del tiempo.
Para el desarrollo de este proyecto se usara los medios de la página https://console.groq.com/
Además, deberas instalar groq en tu PC con pip install groq
"""

import os
from groq import Groq

def get_ai_response(query):
    # Lee la API Key desde las variables de entorno del sistema
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": query,
            }
        ],
        model="openai/gpt-oss-120b",
    )

    return chat_completion.choices[0].message.content

if __name__ == "__main__":
    query = input("Envia un mensaje: \n")

    print(get_ai_response(query))