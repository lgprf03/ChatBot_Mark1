from groq import Groq

def get_ai_response(query):
    # Lee la API Key desde las variables de entorno del sistema
    client = Groq(api_key="TuClaveDeGroq")

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