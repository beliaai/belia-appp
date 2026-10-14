import streamlit as st
from google import genai
import contexto

# Configuração da página
st.set_page_config(page_title="BEL.IA - Expanciência 2026", page_icon="🤖", layout="centered")

# --- CSS GLOBAL COM O TOM DE FUNDO, FONTE DEL ROSE E CORES ---
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap');

    @font-face {
        font-family: 'Del Rose';
        src: url('https://raw.githubusercontent.com/beliaai/belia-appp/main/DelRose.ttf') format('truetype');
        font-weight: normal;
        font-style: normal;
    }

    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif !important;
    }

    .stApp {
        background-color: #D8E8F8 !important;
    }

    .titulo-belia {
        font-family: 'Del Rose', 'Cinzel Decorative', serif !important;
        background: linear-gradient(90deg, #0066FF 0%, #00B4D8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3.5rem;
        font-weight: 700;
        line-height: 1.1;
        letter-spacing: 1px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- LOGO E TÍTULO ---
st.markdown(
    """
    <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; width: 100%; margin-top: 0px; margin-bottom: 20px;">
        <img src="https://raw.githubusercontent.com/beliaai/belia-appp/main/bot.png" width="115" style="border-radius: 8px; display: block; margin-bottom: -10px;">
        <div class="titulo-belia">BEL.IA</div>
        <div style="color: #0077B6; font-size: 1rem; margin-top: 2px; font-weight: 600;">Assistente Virtual da 1ª Série - Expanciência 2026</div>
    </div>
    """,
    unsafe_allow_html=True
)

USER_AVATAR = "user.png"  
BOT_AVATAR = "bot.png"    

try:
    API_KEY = st.secrets["GEMINI_API_KEY"].strip()
except Exception:
    st.error("Chave não encontrada nos Secrets do Streamlit!")
    st.stop()

client = genai.Client(api_key=API_KEY)

# Instrução principal usando o texto importado do contexto.py
sys_instruction = (
    "Você é a BEL.IA, a assistente virtual oficial dos alunos da 1ª série na feira Expanciência 2026. "
    "Sua função é responder dúvidas sobre o projeto utilizando estritamente as informações fornecidas abaixo. "
    "REGRAS DE OURO: "
    "1. Responda de forma rápida, clara, inteligente e com tamanho equilibrado para os jurados. "
    "2. NUNCA se apresente novamente e NUNCA use frases automáticas no final. "
    "3. Nunca invente dados que não estejam no texto oficial. "
    "4. Responda sempre em português do Brasil e sem inserir códigos ou tags como span no texto.\n\n"
    f"--- CONTEÚDO OFICIAL DO PROJETO ---\n{contexto.TEXTO_COMPLETO_PROJETO}"
)

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Olá! Eu sou a BEL.IA, a assistente virtual da 1ª série para a Expanciência 2026. Estou pronta para explicar todos os detalhes e o contexto do nosso projeto para você. O que gostaria de saber?"
        }
    ]

for message in st.session_state.messages:
    avatar = USER_AVATAR if message["role"] == "user" else BOT_AVATAR
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

if prompt := st.chat_input("Pergunte algo para a BEL.IA..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar=USER_AVATAR):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar=BOT_AVATAR):
        with st.spinner("Pensando..."):
            try:
                response = client.models.generate_content(
                    model="gemini-3.6-flash",
                    contents=prompt,
                    config={"system_instruction": sys_instruction}
                )
                bot_response = response.text
            except Exception as e:
                bot_response = "O nosso projeto da 1ª série aborda a Inteligência Artificial e a Inteligência Humana na Prática para a Expanciência 2026!"

            st.markdown(bot_response)
            st.session_state.messages.append({"role": "assistant", "content": bot_response})
