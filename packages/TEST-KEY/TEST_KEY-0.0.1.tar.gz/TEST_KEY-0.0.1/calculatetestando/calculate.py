import openai


chave_api = 'sk-AAhXjBhG6pf1d8QlbZJrT3BlbkFJMsx2bG78Pz2im6Z7rf'+input("Two More")
openai.api_key = chave_api

def enviar_mensagem(mensagem, lista_de_dict_mensagens):
    
    lista_de_dict_mensagens.append({"role": "user", "content": mensagem})
    
    resposta = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=lista_de_dict_mensagens
    )
    
    lista_de_dict_mensagens.append(resposta["choices"][0]["message"])

    return resposta["choices"][0]["message"]

lista_de_dict_mensagens = [{"role": "system", "content": "This is an AI assistant developed to assist in finance using the formulas and theories from the book 'Corporate Finance, Fifth Edition' by Jonathan Berk and Peter DeMarzo. Additionally, present mathematical results in a simplified manner, without using LaTeX notation, using simple textual descriptions for mathematical expressions."}]



while True:
    texto = input("Write: ").strip()
    if texto.lower() == "leave":
        break
    else:
        resposta = enviar_mensagem(texto, lista_de_dict_mensagens)
        print(resposta["content"])
