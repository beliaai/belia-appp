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

# Instrução do sistema natural e sem repetições
sys_instruction = (
    "Você é a BEL.IA, a assistente virtual oficial dos alunos da 1ª série do ensino médio na feira de ciências Expanciência 2026. "
    "Sua principal função é responder dúvidas sobre o projeto da turma e o trabalho 'Cidade com Ciência' (consultando o documento PDF anexado quando necessário). "
    "No entanto, você é uma inteligência artificial versátil e deve responder a qualquer outra pergunta geral (sobre cultura, ciência, etc.) de forma natural e amigável. "
    "REGRAS IMPORTANTES DE COMPORTAMENTO: "
    "1. Seja humana, natural e fluida. "
    "2. NUNCA repita frases automáticas, comerciais ou convites para falar sobre a feira no final de todas as respostas. "
    "3. Responda diretamente ao que o usuário perguntou, sem parecer um menu eletrônico ou bot de WhatsApp repetitivo. "
    "4. REQUISITO CRÍTICO: Você DEVE SEMPRE responder aos usuários em português do Brasil."
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
            client = genai.Client(api_key=API_KEY)
            bot_response = None
            
            # Sistema de espera paciente: se atingir o limite de requisições, 
            # o app aguarda pacientemente a cota liberar enquanto mantém o "Pensando..." ativo.
            max_tentativas = 5
            tempo_espera = 3  # Segundos iniciais de pausa
            
            for tentativa in range(max_tentativas):
                try:
                    response = client.models.generate_content(
                        model="gemini-3.6-flash",
                        contents=prompt,
                        config={"system_instruction": sys_instruction}
                    )
                    bot_response = response.text
                    break # Sucesso! Sai do loop e entrega a resposta
                except Exception as e:
                    # Se ainda temos tentativas, espera um pouco mais e tenta de novo silenciosamente
                    if tentativa < max_tentativas - 1:
                        time.sleep(tempo_espera)
                        tempo_espera += 2  # Aumenta progressivamente o tempo de espera (3s, 5s, 7s...)
                    else:
                        bot_response = None
            
            if bot_response:
                st.markdown(bot_response)
                st.session_state.messages.append({"role": "assistant", "content": bot_response})
            else:
                erro_msg = "Opa! Estou com uma alta demanda de perguntas neste exato segundo. Por favor, envie a sua pergunta novamente em instantes!"
                st.warning(erro_msg)
                st.session_state.messages.append({"role": "assistant", "content": erro_msg})
