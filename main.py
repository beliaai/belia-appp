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

chave_api = st.secrets.get("GEMINI_API_KEY", "").strip()

if not chave_api:
    st.error("Configure a chave GEMINI_API_KEY nos Secrets do Streamlit!")
    st.stop()

genai.configure(api_key=chave_api)

instrucao_sistema = (
    "Você é a BEL.IA, assistente virtual da 1ª série do Colégio Expansivo para a Expanciência 2026 "
    "('Inteligência Artificial e Inteligência Humana na Prática').\n"
    "Responda de forma clara, objetiva, didática e bem explicada, sem respostas longas demais nem enrolação. "
    "Não se apresente de novo e não coloque despedidas automáticas.\n\n"
    "BASE DO PROJETO:\n"
) + contexto.TEXTO_COMPLETO_PROJETO

model = genai.GenerativeModel(
    model_name="gemini-3.8-flash",
    system_instruction=instrucao_sistema
)

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Olá! Eu sou a BEL.IA, a assistente virtual da 1ª série para a Expanciência 2026. Estou pronta para explicar os detalhes do nosso projeto 'Inteligência Artificial e Inteligência Humana na Prática'. O que você gostaria de saber?"
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
        with st.spinner("Respondendo..."):
            try:
                response = model.generate_content(
                    prompt,
                    generation_config={
                        "temperature": 0.4,
                        "max_output_tokens": 500,
                    },
                    request_options={"timeout": 25},
                )
                bot_response = response.text if response and response.text else "Sem resposta no momento."
            except Exception as e:
                bot_response = f"Erro ou demora na resposta: {str(e)}"

            st.markdown(bot_response)
            st.session_state.messages.append({"role": "assistant", "content": bot_response})
