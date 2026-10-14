import streamlit as st
import google.generativeai as genai
import contexto

st.set_page_config(page_title="BEL.IA - Expanciência 2026", page_icon="🤖", layout="centered")

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

genai.configure(api_key=API_KEY)

instrucao_base = (
    "Você é a BEL.IA, a assistente virtual inteligente desenvolvida pelos alunos da 1ª série do Colégio Expansivo para a feira Expanciência 2026. "
    "Sua missão é conversar com o público e os jurados explicando o projeto 'Inteligência Artificial e Inteligência Humana na Prática'.\n\n"
    "DIRETRIZES DE RESPOSTA:\n"
    "1. **Responda EXATAMENTE ao que foi perguntado**: Se perguntarem sobre um grupo específico, detalhe apenas ele. Se perguntarem do projeto geral, explique o tema e objetivos sem falar de culminância (datas/local) a menos que pedido.\n"
    "2. **Seja Natural e Fluida**: Use suas próprias palavras, com explicações articuladas e didáticas, sem copiar blocos rígidos de texto.\n"
    "3. **Restrições**: NUNCA se apresente novamente e nunca inclua frases automáticas ou despedidas genéricas no final.\n\n"
    "--- BASE DE CONHECIMENTO COMPLETA DO PROJETO ---\n"
)

system_prompt = instrucao_base + contexto.TEXTO_COMPLETO_PROJETO

# Nome exato aceite pela versão clássica da API
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash-001",
    system_instruction=system_prompt
)

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Olá! Eu sou a BEL.IA, a assistente virtual da 1ª série para a Expanciência 2026. Estou pronta para explicar todos os detalhes do nosso projeto 'Inteligência Artificial e Inteligência Humana na Prática' para você. O que gostaria de saber?"
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
                chat = model.start_chat(history=[])
                response = chat.send_message(prompt)
                bot_response = response.text
            except Exception as e:
                bot_response = f"Erro técnico exato: {str(e)}"

            st.markdown(bot_response)
            st.session_state.messages.append({"role": "assistant", "content": bot_response})
