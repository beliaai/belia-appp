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

instrucao_sistema = (
    "Você é a BEL.IA, assistente virtual da 1ª série do Colégio Expansivo para a Expanciência 2026 "
    "('Inteligência Artificial e Inteligência Humana na Prática'). "
    "Responda de forma rápida, clara, objetiva e bem explicada, sem se apresentar de novo.\n\n"
    "BASE DO PROJETO:\n"
) + contexto.TEXTO_COMPLETO_PROJETO


def responder_por_palavras_chave(pergunta: str) -> str:
    p = pergunta.lower()

    if any(k in p for k in ["tempo", "demorou", "prazo", "meses", "cronograma", "quando começou", "etapas"]):
        return (
            "O subprojeto foi desenvolvido em duas etapas: a primeira de pesquisa e trabalho escrito entre agosto e setembro, "
            "e a segunda de preparação prática e ensaios entre outubro e novembro. Já a criação da BEL.IA envolveu 4 meses "
            "de estudo e pesquisa."
        )

    if any(k in p for k in ["grupo 1", "grupo um", "psicologia", "cibele", "transformer", "nome bel", "bel.ia"]):
        return (
            "O Grupo 1 aborda IA versus inteligência humana na Psicologia, com participação da psicóloga Cibele Valente e "
            "referência no artigo 'Attention Is All You Need'. Ele mostra que a IA reconhece padrões, mas não tem consciência, "
            "emoção, escuta empática ou vínculo humano, além de apresentar a BEL.IA (cujo nome junta 'Bel' de Belquis com 'IA')."
        )

    if any(k in p for k in ["grupo 2", "grupo dois", "design", "gráfico", "história", "oeslem", "ufg"]):
        return (
            "O Grupo 2 trata da história da IA até a IA generativa e seus impactos no Design Gráfico — como criação, edição, "
            "prototipagem, autoria e originalidade —, com convidado Oeslem Maik e base no e-book da UFG (2025)."
        )

    if any(k in p for k in ["grupo 3", "grupo três", "grupo tres", "peça", "teatro", "cientista", "laboratório", "ruth salles"]):
        return (
            "O Grupo 3 apresenta a peça teatral 'A I.A. e o Cientista' (~10 min, com cenário de laboratório), sobre um cientista "
            "que cria uma IA, fica dependente dela e, ao ver suas ideias rejeitadas, decide desligá-la para retomar sua própria "
            "autonomia intelectual, com base na obra de Ruth Salles."
        )

    if any(k in p for k in ["grupo 4", "grupo quatro", "educação", "quiz", "professores", "talis", "56%"]):
        return (
            "O Grupo 4 traz um quiz interativo diferenciando produções humanas e de IA na educação e cita a pesquisa TALIS 2024 "
            "(OCDE / Agência Brasil), que aponta que 56% dos professores brasileiros usam IA no apoio pedagógico, destacando o "
            "papel insubstituível do professor na mediação e na sensibilidade humana."
        )

    if any(k in p for k in ["culminância", "sábado", "dia 21", "horário", "hora", "local", "estande", "onde"]):
        return (
            "A culminância acontece no dia 21 de novembro de 2026, das 18h às 21h (com montagem do estande das 8h às 12h), "
            "no Colégio Expansivo, em estande coletivo próximo ao refeitório e parquinho da Educação Infantil."
        )

    return (
        "O projeto da 1ª série do Colégio Expansivo na Expanciência 2026 tem o tema 'Inteligência Artificial e Inteligência "
        "Humana na Prática: Origem e Desenvolvimento da I.A nas Profissões no Brasil', com orientação de Deuziana Almeida e "
        "Malrício França, dividido em quatro grupos (Psicologia, Design Gráfico, Peça Teatral e Educação/Quiz)."
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
        bot_response = None
        if chave_api:
            try:
                genai.configure(api_key=chave_api)
                model = genai.GenerativeModel(
                    model_name="gemini-3.8-flash",
                    system_instruction=instrucao_sistema
                )
                response = model.generate_content(
                    prompt,
                    generation_config={
                        "temperature": 0.4,
                        "max_output_tokens": 350,
                    },
                    request_options={"timeout": 3},
                )
                if response and response.text:
                    bot_response = response.text
            except Exception:
                bot_response = None

        if not bot_response:
            bot_response = responder_por_palavras_chave(prompt)

        st.markdown(bot_response)
        st.session_state.messages.append({"role": "assistant", "content": bot_response})
