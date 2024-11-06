import os 
from groq import Groq 

# Defina a chave de API diretamente no codigo ou garanta que ela esteja configurada corretamente no ambiente
os.environ["GROQ_API_KEY"] = "Digite aqui a sua chave de API"

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

# inicializa a lista de mensagens para manter o contexto da conerva 
mensages = []

while true: 
    usuario = input("Digite uma mensagem ou sair para encerrar: ")

    if usuario.lower() == sair:
        print("Conversa encerrada.")
        break

        # adiciona a mensagem do usuario á lista de mensagens
        messages.append({"role": "user", "content"; usuario})

        chat_completion = client.chat.completions.create(
            messages=messages,
            model="11ama-3.1-70b-versatile",
        )

        resposta = chat_completion.choices[0].message.content
        print("resposta:", resposta)

        # Adiciona a resposta do assistente á lista de mensagens para manter o contexto 
        messages.append({"role": assistant', "content": resposta })