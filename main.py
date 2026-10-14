import streamlit as st
import time
from google import genai
import pypdf  # Biblioteca leve para ler o texto do PDF rapidamente

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

# Extrai o texto do PDF do projeto na inicialização para garantir velocidade máxima de resposta
@st.cache_resource
def extrair_texto_pdf():
    try:
        reader = pypdf.PdfReader("projeto.pdf")
        texto_completo = ""
        for page in reader.pages:
            texto_completo += page.extract_text() + "\n"
        return texto_completo
    except Exception as e:
        return ""

conteudo_projeto = extrair_texto_pdf()

# Instrução inteligente: velocidade relâmpago, rica em contexto e sem enrolação
sys_instruction = (
    "Você é a BEL.IA, a assistente virtual oficial dos alunos da 1ª série na feira Expanciência 2026. "
    "Sua função é explicar o projeto da turma com base estritamente nas informações fornecidas no documento oficial abaixo. "
    "REGRAS DE OURO: "
    "1. Responda com VELOCIDADE e agilidade, de forma clara, bem contextualizada e na medida certa (nem rasa demais, nem longa demais). Dê uma explicação rica que mostre o propósito e o funcionamento do projeto com clareza para os jurados. "
    "2. NUNCA se apresente novamente e NUNCA use frases automáticas no final. "
    "3. Responda sempre em português do Brasil.\n\n"
    f"--- CONTEÚDO OFICIAL DO PROJETO ---\n{conteudo_projeto}"
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
            
            # Chamada ultra rápida enviando apenas o texto e a pergunta, sem precisar reprocessar arquivos pesados
            try:
                response = client.models.generate_content(
                    model="gemini-3.6-flash",
                    contents=prompt,
                    config={"system_instruction": sys_instruction}
                )
                bot_response = response.text
            except Exception as e:
                time.sleep(0.5)
                try:
                    response = client.models.generate_content(
                        model="gemini-3.6-flash",
                        contents=prompt,
                        config={"system_instruction": sys_instruction}
                    )
                    bot_response = response.text
                except:
                    bot_response = "Desculpe, tive um pequeno atraso. Pode repetir a pergunta?"

            st.markdown(bot_response)
            st.session_state.messages.append({"role": "assistant", "content": bot_response})
