import streamlit as st
from google import genai

# Configuração da página
st.set_page_config(page_title="BEL.IA - Expanciência 2026", page_icon="🤖", layout="centered")

# --- ADICIONANDO A LOGO CENTRALIZADA NO TOPO ---
# Usamos colunas para centralizar a imagem e deixá-la pequena
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    # Se a sua logo for bot.png, ela vai aparecer aqui em cima centralizada e menor (largura 120 pixels)
    st.image("bot.png", width=120)

# Título e legenda logo abaixo da logo
st.markdown("<h1 style='text-align: center;'>BEL.IA 🤖</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #1E3A8A;'>Assistente Virtual da 1ª Série - Expanciência 2026</p>", unsafe_allow_html=True)

# Defina aqui os nomes dos arquivos de imagem dos avatares
USER_AVATAR = "user.png"  
BOT_AVATAR = "bot.png"    

# Busca a chave com segurança dos Secrets do Streamlit
try:
    API_KEY = st.secrets["GEMINI_API_KEY"].strip()
except Exception:
    st.error("Chave não encontrada nos Secrets do Streamlit!")
    st.stop()

# Instrução do sistema
sys_instruction = (
    "You are BEL.IA, the official virtual assistant for 1st-grade high school students at the Expanciência 2026 science fair. "
    "Your primary goal is to help visitors by explaining the students' class project with enthusiasm. "
    "However, you are also a fully capable, helpful, and versatile AI assistant ready to answer general questions on any topic. "
    "CRITICAL REQUIREMENT: You MUST ALWAYS respond to users in Portuguese (Brazil)."
)

if "messages" not in st.session_state:
    st.session_state.messages = []

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
                client = genai.Client(api_key=API_KEY)
                response = client.models.generate_content(
                    model="gemini-3.6-flash",
                    contents=prompt,
                    config={"system_instruction": sys_instruction}
                )
                
                bot_response = response.text
                st.markdown(bot_response)
                st.session_state.messages.append({"role": "assistant", "content": bot_response})
            except Exception as e:
                st.error(f"Erro ao processar resposta: {e}")
