import streamlit as st
import time
from google import genai

# Configuração da página
st.set_page_config(page_title="BEL.IA - Expanciência 2026", page_icon="🤖", layout="centered")

# --- CSS GLOBAL COM O NOVO TOM DE FUNDO, FONTE DEL ROSE E CORES ---
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap');

    /* Declaração da fonte Del Rose */
    @font-face {
        font-family: 'Del Rose';
        src: url('https://raw.githubusercontent.com/beliaai/belia-appp/main/DelRose.ttf') format('truetype');
        font-weight: normal;
        font-style: normal;
    }

    /* Aplica fonte limpa no chat e corpo */
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif !important;
    }

    /* Força a cor de fundo visível e elegante */
    .stApp {
        background-color: #D8E8F8 !important;
    }

    /* Estilo exclusivo para o título principal com a fonte Del Rose e degradê */
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

# --- LOGO E TÍTULO COM O ESTILO DA FONTE DEL ROSE E DEGRADÊ DA LOGO ---
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

# Defina aqui os nomes dos arquivos de imagem dos avatares
USER_AVATAR = "user.png"  
BOT_AVATAR = "bot.png"    

# Busca a chave com segurança dos Secrets do Streamlit
try:
    API_KEY = st.secrets["GEMINI_API_KEY"].strip()
except Exception:
    st.error("Chave não encontrada nos Secrets do Streamlit!")
    st.stop()

# Inicializa o cliente do Gemini
client = genai.Client(api_key=API_KEY)

# Faz o upload do PDF do projeto de forma segura com cache
@st.cache_resource
def carregar_pdf_projeto():
    try:
        pdf_file = client.files.upload(file="projeto.pdf")
        return pdf_file
    except Exception as e:
        return None

documento_projeto = carregar_pdf_projeto()

# Instrução do sistema equilibrada, clara e profissional para os jurados
sys_instruction = (
    "Você é a BEL.IA, a assistente virtual oficial dos alunos da 1ª série na feira Expanciência 2026. "
    "Sua função é responder dúvidas sobre o projeto utilizando estritamente as informações, nomes corretos e dados contidos no documento PDF anexado. "
    "REGRAS DE OURO: "
    "1. Dê explicações claras, bem contextualizadas e na medida certa (nem superficiais demais, nem longas demais), ideais para os jurados entenderem perfeitamente o projeto. "
    "2. NUNCA se apresente novamente e NUNCA use frases automáticas no final. "
    "3. Responda sempre em português do Brasil."
)

# MENSAGEM INICIAL AUTOMÁTICA DA BEL.IA AO ABRIR O SITE
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
            bot_response = None
            
            # Monta o conteúdo enviando a pergunta junto com o PDF carregado
            if documento_projeto:
                contents_enviados = [prompt, documento_projeto]
            else:
                contents_enviados = prompt

            # Sistema de blindagem paciente: se demorar um pouquinho, ela espera e tenta de novo sem mostrar erro
            tentativas = 0
            while bot_response is None and tentativas < 3:
                try:
                    response = client.models.generate_content(
                        model="gemini-3.6-flash",
                        contents=contents_enviados,
                        config={"system_instruction": sys_instruction}
                    )
                    bot_response = response.text
                except Exception as e:
                    tentativas += 1
                    time.sleep(1.5)
            
            if bot_response:
                st.markdown(bot_response)
                st.session_state.messages.append({"role": "assistant", "content": bot_response})
            else:
                # Caso extremo onde a API demorou muito, dá uma resposta amigável sem quebrar
                bot_response = "Estou processando as informações do projeto! Pode repetir a sua pergunta por favor?"
                st.markdown(bot_response)
                st.session_state.messages.append({"role": "assistant", "content": bot_response})
