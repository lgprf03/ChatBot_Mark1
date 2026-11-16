from groq import Groq

# Configuración inicial del cliente y límites estimados de Groq (ej. Límite estándar gratuito RPM/RPD)
API_KEY = "TuClaveDeGroq"
MODELO = "openai/gpt-oss-120b"

# Límite estimado de consultas permitidas (ajustable según el tier de tu cuenta de Groq)
LIMITE_MAXIMO_CONSULTAS = 30  
consultas_realizadas = 0

client = Groq(api_key=API_KEY)

def mostrar_metrica():
    """Muestra cuántas consultas quedan antes de alcanzar el límite estimado."""
    restantes = max(0, LIMITE_MAXIMO_CONSULTAS - consultas_realizadas)
    print(f"\n[📊 MÉTRICA DE USO] Consultas realizadas: {consultas_realizadas} | Consultas restantes estimadas: {restantes}/{LIMITE_MAXIMO_CONSULTAS}\n")

def get_ai_response(mensajes_historial, nombre_usuario):
    global consultas_realizadas
    
    # Muestra la métrica antes de hacer la solicitud
    mostrar_metrica()
    
    try:
        chat_completion = client.chat.completions.create(
            messages=mensajes_historial,
            model=MODELO,
        )
        consultas_realizadas += 1
        respuesta_modelo = chat_completion.choices[0].message.content
        
        # Formatea la respuesta para que inicie con "Esta bien NOMBRE, "
        respuesta_formateada = f"Esta bien {nombre_usuario}, {respuesta_modelo}"
        return respuesta_formateada
    
    except Exception as e:
        return f"Esta bien {nombre_usuario}, ocurrió un error al conectar con Groq: {e}"

if __name__ == "__main__":
    print("=== CHATBOT INTELIGENTE CON GROQ ===")
    nombre_usuario = input("Por favor, ingresa tu nombre: ").strip()
    
    if not nombre_usuario:
        nombre_usuario = "Amigo"
        
    print(f"\n¡Hola, {nombre_usuario}! Qué gusto saludarte. Comencemos a chatear (escribe 'salir' para terminar).\n")
    
    # Historial inicial de la conversación con rol de sistema opcional para guiar el prefijo
    # o simplemente manejando el historial de mensajes usuario/asistente.
    historial_mensajes = []

    while True:
        query = input(f"{nombre_usuario}: ")
        if query.lower() in ["salir", "exit", "quit"]:
            print(f"¡Hasta luego, {nombre_usuario}!")
            break
            
        if not query.strip():
            continue

        # Agrega la consulta del usuario al historial
        historial_mensajes.append({"role": "user", "content": query})

        # Obtiene la respuesta de la IA manteniendo el contexto
        respuesta = get_ai_response(historial_mensajes, nombre_usuario)
        
        print(f"Chat: {respuesta}\n")

        # Agrega la respuesta al historial para conservar el contexto de la conversación
        # (Guardamos la respuesta limpia o con el formato según prefieras para el historial interno)
        historial_mensajes.append({"role": "assistant", "content": respuesta})