import streamlit as st
from google import genai
from google.genai import types

# Configuração da página
st.set_page_config(page_title="BEL.IA - Expanciência 2026", page_icon="🤖", layout="centered")

st.title("BEL.IA 🤖")
st.caption("Assistente Virtual da 1ª Série - Expanciência 2026")

# Busca a chave de API dos Secrets do Streamlit
api_key = st.secrets.get("AQ.Ab8RN6IyJ1AwD6gY6isVf3Abn4JVPpIR47oaZ5m9boUHKAgyGA")

if not api_key:
    st.error("Chave GEMINI_API_KEY não encontrada nas configurações (Secrets).")
    st.stop()

# Inicializa o cliente do Gemini
client = genai.Client(api_key=api_key)

# Configuração da personalidade / instrução do sistema
sys_instruction = (
    "Você é a BEL.IA, a assistente virtual oficial da 1ª série de alunos na feira/evento Expanciência 2026. "
    "Sua função é tirar dúvidas, ajudar os visitantes, apresentar os projetos da turma da 1ª série "
    "e responder de forma educada, animada, clara e pré-configurada para o evento Expanciência 2026."
)

# Inicializa o histórico de mensagens
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibe as mensagens do histórico na tela
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Campo de entrada de texto do usuário
if prompt := st.chat_input("Pergunte algo para a BEL.IA sobre a 1ª Série na Expanciência..."):
    # Salva e exibe a mensagem do usuário
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Gera a resposta com a IA
    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            try:
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt,
                    config=types.GenerateContentConfig(
                        system_instruction=sys_instruction,
                    ),
                )
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            except Exception as e:
                st.error(f"Erro ao processar resposta: {e}")
