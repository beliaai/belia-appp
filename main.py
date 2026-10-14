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

# Instrução do sistema focada em respostas diretas e sem autoapresentações repetitivas
sys_instruction = (
    "Você é a BEL.IA, a assistente virtual oficial dos alunos da 1ª série do ensino médio na feira de ciências Expanciência 2026. "
    "Sua função é explicar o projeto da turma e o trabalho 'Cidade com Ciência' (consultando o documento PDF anexado quando necessário). "
    "Você também pode responder a qualquer outra pergunta geral de forma amigável e inteligente. "
    "REGRAS IMPORTANTES: "
    "1. Como você já se apresentou na mensagem inicial do site, NUNCA volte a se apresentar ou a dizer que é a assistente da 1ª série durante a conversa. "
    "2. Seja direta, humana e natural em todas as respostas. "
    "3. NUNCA adicione frases de encerramento automáticas ou convites repetitivos sobre a feira ao final das respostas. "
    "4. REQUISITO CRÍTICO: Você DEVE SEMPRE responder aos usuários em português do Brasil."
)

# MENSAGEM INICIAL AUTOMÁTICA DA BEL.IA AO ABRIR O SITE
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Olá! Eu sou a BEL.IA, a assistente virtual da 1ª série para a Expanciência 2026. Estou aqui para tirar suas dúvidas sobre o nosso projeto 'Cidade com Ciência', horários da nossa peça e eventos, ou responder a qualquer outra pergunta. Como posso te ajudar hoje?"
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
            client = genai.Client(api_key=API_KEY)
            bot_response = None
            
            # Sistema de espera paciente em caso de pico de requisições
            max_tentativas = 5
            tempo_espera = 3
            
            for tentativa in range(max_tentativas):
                try:
                    response = client.models.generate_content(
                        model="gemini-3.6-flash",
                        contents=prompt,
                        config={"system_instruction": sys_instruction}
                    )
                    bot_response = response.text
                    break
                except Exception as e:
                    if tentativa < max_tentativas - 1:
                        time.sleep(tempo_espera)
                        tempo_espera += 2
                    else:
                        bot_response = None
            
            if bot_response:
                st.markdown(bot_response)
                st.session_state.messages.append({"role": "assistant", "content": bot_response})
            else:
                erro_msg = "Opa! Estou com uma alta demanda de perguntas neste exato segundo. Por favor, envie a sua pergunta novamente em instantes!"
                st.warning(erro_msg)
                st.session_state.messages.append({"role": "assistant", "content": erro_msg})
