import streamlit as st
from openai import OpenAI
# streamlit é um framework 

# titulo
titulo = st.write('# Chat com IA'); # markdown

# api da openAI
modelo_ai = OpenAI(
    api_key= # Sua chave de API aqui
    );

if not 'lista_mensagens' in st.session_state:
    st.session_state['lista_mensagens'] = [];

# a cada mensagem que o usuario enviar:
for mensagem in st.session_state['lista_mensagens']:
    st.chat_message(mensagem['role']).write(mensagem['content']);

# input do chat (campo de mensagem)
texto_usuario = st.chat_input('Digite sua mensagem');

if texto_usuario:
    # mostrar a mensagem que o usuário envio o chat
    st.chat_message('user').write(texto_usuario);
    mensagem_usuario = {"role": "user", "content": texto_usuario};
    st.session_state["lista_mensagens"].append(mensagem_usuario);
    resposta_ia  = "Você perguntou: " + texto_usuario;
    # Nome da pessoas
    # user
    # assistant


    # ia respondeu
    resposta_ia = modelo_ai.chat.completions.create(
        messages=st.session_state["lista_mensagens"],
        model= 'chatgpt-4o-latest'
    );

    texto_final = resposta_ia.choices[0].message.content

    st.chat_message("assistant").write(texto_final)
    mensagem_ia = {"role": "assistant", "content": texto_final}
    st.session_state['lista_mensagens'].append(mensagem_ia)

    
    # pegar a pergunta e enviar para uma IA responder
    # exibir a resposta da IA na tela

# Streamlit -> apenas com Python criar o frontend e o backend
    # a IA que vamos usar: OpenAI
    # pip install openai streamlit
    # para rodar seu site streamlit use o comnado no terminal: streamlit run <nome do arquivo>


