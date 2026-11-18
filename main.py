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

# Inicializa as chaves e o controle de quais estão esgotadas na sessão do Streamlit
if "chaves_api" not in st.session_state:
    chaves_carregadas = []
    for i in ["GEMINI_API_KEY", "GEMINI_API_KEY_2", "GEMINI_API_KEY_3"]:
        try:
            k = st.secrets.get(i)
            if k:
                chaves_carregadas.append(k.strip())
        except Exception:
            pass
    st.session_state.chaves_api = chaves_carregadas

if not st.session_state.chaves_api:
    st.error("Nenhuma chave de API encontrada nos Secrets do Streamlit!")
    st.stop()

# Controle de chaves inválidas ou esgotadas para descartar temporariamente
if "chaves_esgotadas" not in st.session_state:
    st.session_state.chaves_esgotadas = set()

instrucao_sistema = (
    "Você é a BEL.IA, a assistente virtual inteligente desenvolvida pelos alunos da 1ª série do Colégio Expansivo para a feira Expanciência 2026. "
    "Sua missão é conversar com o público e os jurados explicando o projeto 'Inteligência Artificial e Inteligência Humana na Prática'.\n\n"
    "DIRETRIZES DE RESPOSTA:\n"
    "1. **Seja Completa e Explicativa**: Evite respostas excessivamente curtas ou superficiais. Desenvolva bem as ideias, traga contexto, explique o raciocínio por trás dos tópicos e dê respostas ricas e bem estruturadas que impressionem os jurados.\n"
    "2. **Responda com Precisão**: Se perguntarem sobre um grupo específico, detalhe-o bem. Se perguntarem do projeto geral, explique o tema e os objetivos com clareza e profundidade.\n"
    "3. **Seja Natural e Fluida**: Use explicações articuladas e didáticas, mantendo uma conversa agradável.\n"
    "4. **Restrições**: NUNCA se apresente novamente e nunca inclua frases automáticas ou despedidas genéricas no final.\n\n"
    "--- BASE DE CONHECIMENTO COMPLETA DO PROJETO ---\n"
) + contexto.TEXTO_COMPLETO_PROJETO

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
            bot_response = None
            
            # Organiza a ordem: testa primeiro as chaves que NÃO estão na lista de esgotadas
            chaves_disponiveis = [k for k in st.session_state.chaves_api if k not in st.session_state.chaves_esgotadas]
            
            # Se todas esgotaram, limpa a lista para tentar dar uma nova chance a elas
            if not chaves_disponiveis:
                st.session_state.chaves_esgotadas.clear()
                chaves_disponiveis = list(st.session_state.chaves_api)

            # Tenta enviar a mensagem iterando apenas pelas chaves ativas/válidas
            for chave in chaves_disponiveis:
                try:
                    genai.configure(api_key=chave)
                    model = genai.GenerativeModel(
                        model_name="gemini-2.5-flash",
                        system_instruction=instrucao_sistema
                    )
                    
                    chat = model.start_chat(history=[
                        {"role": "user" if m["role"] == "user" else "model", "parts": [m["content"]]}
                        for m in st.session_state.messages[:-1]
                    ])
                    response = chat.send_message(prompt)
                    
                    if response and response.text:
                        bot_response = response.text
                        break 
                except Exception as e:
                    erro_str = str(e).lower()
                    # Se detectar erro de cota ou limite atingido (429 / resource exhausted), descarta essa chave temporariamente
                    if "429" in erro_str or "quota" in erro_str or "resource_exhausted" in erro_str or "limit" in erro_str:
                        st.session_state.chaves_esgotadas.add(chave)
                    continue

            if not bot_response:
                bot_response = "⚠️ Todas as chaves atingiram o limite de requisições no momento. Por favor, aguarde um minutinho."

            st.markdown(bot_response)
            st.session_state.messages.append({"role": "assistant", "content": bot_response})
