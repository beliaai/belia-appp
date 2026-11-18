import streamlit as st
import google.generativeai as genai
import contexto

st.set_page_config(page_title="BEL.IA - Expanciência 2026", page_icon="🤖", layout="centered")

# Recolhemos todas as 5 chaves disponíveis de forma segura nos Secrets do Streamlit
chaves_api = []
for i in ["GEMINI_API_KEY", "GEMINI_API_KEY_2", "GEMINI_API_KEY_3", "GEMINI_API_KEY_4", "GEMINI_API_KEY_5"]:
    try:
        k = st.secrets.get(i)
        if k:
            chaves_api.append(k.strip())
    except Exception:
        pass

if not chaves_api:
    st.error("Nenhuma chave de API encontrada nos Secrets do Streamlit!")
    st.stop()

# Memória global compartilhada entre TODOS os celulares/dispositivos conectados
@st.cache_resource
def obter_memoria_global():
    return {"chaves_esgotadas": set()}

memoria_global = obter_memoria_global()

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
    <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; width: 100%; margin-top:
