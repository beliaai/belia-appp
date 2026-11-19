import streamlit as st
import google.generativeai as genai

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


def obter_bloco_base(pergunta: str) -> str:
    p = pergunta.lower()

    if any(k in p for k in ["tempo", "demorou", "prazo", "meses", "cronograma", "quando começou", "etapas", "quando"]):
        return (
            "O desenvolvimento do subprojeto aconteceu em duas etapas principais: a primeira foi de pesquisa, levantamento "
            "bibliográfico e elaboração do trabalho escrito entre agosto e setembro (com base na obra 'Introdução à Inteligência "
            "Artificial' da UFG), e a segunda foi de preparação prática, reuniões de alinhamento, ensaios da peça e montagem do "
            "estande entre outubro e novembro. Já a criação e o estudo da BEL.IA envolveram 4 meses de pesquisa e dedicação."
        )

    if any(k in p for k in ["grupo 1", "grupo um", "psicologia", "cibele", "transformer", "nome bel", "bel.ia", "belquis"]):
        return (
            "O Grupo 1 investiga Inteligência Artificial vs. Inteligência Humana e a Psicologia, utilizando a BEL.IA em "
            "uma demonstração prática interativa. A discussão mostra que a IA processa dados e reconhece padrões de linguagem, "
            "mas não possui consciência, sentimentos, escuta empática, vínculos afetivos ou responsabilidade ética e subjetiva "
            "como um psicólogo. Conta com a convidada especial Psicóloga Cibele Valente e referência no artigo Attention Is "
            "All You Need (Vaswani et al., 2017, arquitetura Transformer). O nome BEL.IA vem da junção de 'Bel' (de Belquis) "
            "com 'IA', desenvolvida por Graziella Belquis ao lado de Isadora Gemaque, Carolina Gondim, Erick Santos, Sara Yasmin, "
            "José Arthur e Levi Campos."
        )

    if any(k in p for k in ["grupo 2", "grupo dois", "design", "gráfico", "grafico", "história", "historia", "oeslem", "ufg"]):
        return (
            "O Grupo 2 aborda a História da IA e o Impacto no Design Gráfico, traçando a evolução da IA até a IA generativa "
            "e analisando como ela muda a criação, a edição de imagens, a prototipagem, a autoria, a criatividade e a originalidade "
            "no trabalho dos designers. Tem como convidado especial o designer gráfico Oeslem Maik, referência no e-book "
            "Introdução à Inteligência Artificial (Cegraf UFG, 2025), e conta com Gabriel Malcher, João Paulo Guimarães, "
            "Luís Eduardo Amim, Ricardo Batista, Pedro Paulo Souza, Arthur Mesquita e Miguel Santos."
        )

    if any(k in p for k in ["grupo 3", "grupo três", "grupo tres", "peça", "teatro", "cientista", "laboratório", "laboratorio", "ruth salles"]):
        return (
            "O Grupo 3 apresenta a peça teatral autoral 'A I.A. e o Cientista' (~10 minutos, com cenário de laboratório, "
            "jaleco, figurino de robô e trilha sonora), inspirada na obra Teatro na Escola (Ruth Salles). Na história, um "
            "cientista cria uma IA para apoiar suas pesquisas, mas acaba ficando dependente e duvidando da própria capacidade. "
            "Quando a IA rejeita suas ideias e argumenta que apenas combina dados criados por humanos, ele decide desligá-la "
            "para retomar sua autonomia intelectual e voltar a escrever suas próprias ideias no papel. Participam Maria Clara "
            "Souza, Rafaela Oliveira (roteiro), Izabella Yared, Maria Luisa Duarte, Júlia Carvalho, Geovana Mesquita e Endy Aquino."
        )

    if any(k in p for k in ["grupo 4", "grupo quatro", "educação", "educacao", "quiz", "professores", "talis", "56%"]):
        return (
            "O Grupo 4 trabalha A IA na Educação e o Quiz Interativo, propondo um quiz para diferenciar produções feitas "
            "por IA e por seres humanos e debater o papel do professor. O grupo apresenta dados da pesquisa TALIS 2024 "
            "(OCDE / Agência Brasil), mostrando que 56% dos professores brasileiros utilizam IA para planejar aulas, buscar "
            "metodologias e adaptar materiais — reforçando que a IA apoia, mas não substitui a mediação, o senso crítico e a "
            "sensibilidade humana do docente. Integrantes: Elen Miranda, Samuel Monteiro, Ana Beatriz Vilhena, Lucas Araújo, "
            "Fernanda Pimentel, Rúbia Mendonça e Pedro Bueno."
        )

    if any(k in p for k in ["culminância", "culminancia", "sábado", "sabado", "dia 21", "horário", "horario", "hora", "local", "estande", "onde", "orientadores", "coordenação"]):
        return (
            "A culminância da Expanciência 2026 no Colégio Expansivo (Macapá/AP) acontece no dia 21 de novembro de 2026, "
            "das 18h às 21h (com montagem do estande das 8h às 12h), em estande coletivo próximo ao refeitório e parquinho "
            "da Educação Infantil, com expectativa de mais de 600 visitantes. O projeto é avaliativo para todas as disciplinas "
            "do 3º bimestre da 1ª série, com orientação de Deuziana Almeida e Malrício França e coordenação pedagógica de "
            "Jovelina Souto e Andréa Santa Rosa."
        )

    return (
        "O subprojeto da 1ª série do Ensino Médio do Colégio Expansivo (Macapá/AP) para a Expanciência 2026 tem o tema "
        "'Inteligência Artificial e Inteligência Humana na Prática: Origem e Desenvolvimento da I.A nas Profissões no Brasil', "
        "orientado por Deuziana Almeida e Malrício França. A pesquisa investiga como a IA transforma o trabalho e as profissões "
        "sem substituir a consciência, a emoção, a escuta empática e os vínculos humanos, sendo dividida em quatro frentes: "
        "Grupo 1 (Psicologia e BEL.IA), Grupo 2 (História da IA e Design Gráfico), Grupo 3 (peça teatral 'A I.A. e o "
        "Cientista') e Grupo 4 (IA na Educação e Quiz Interativo com dados da TALIS 2024)."
    )


def gerar_resposta_com_proprias_palavras(pergunta: str, bloco_base: str) -> str:
    if not chave_api:
        return bloco_base

    try:
        genai.configure(api_key=chave_api)
        instrucao = (
            "Você é a BEL.IA, assistente virtual da 1ª série do Colégio Expansivo na Expanciência 2026. "
            "Responda à pergunta usando as SUAS PRÓPRIAS PALAVRAS, de forma fluida, natural, envolvente e bem "
            "desenvolvida, discorrendo sobre o assunto com base EXCLUSIVAMENTE nas informações do bloco fornecido. "
            "Não invente fatos que não estejam no bloco, não se apresente novamente e mantenha nomes, datas, "
            "números e referências fiéis ao bloco."
        )
        model = genai.GenerativeModel(
            model_name="gemini-3.8-flash",
            system_instruction=instrucao
        )
        prompt_final = (
            f"INFORMAÇÕES DO PROJETO:\n{bloco_base}\n\n"
            f"PERGUNTA: {pergunta}\n\n"
            "Explique esse assunto com as suas próprias palavras de maneira clara e bem desenvolvida:"
        )
        response = model.generate_content(
            prompt_final,
            generation_config={
                "temperature": 0.65,
                "max_output_tokens": 500,
            },
            request_options={"timeout": 4},
        )
        if response and response.text and response.text.strip():
            return response.text.strip()
    except Exception:
        pass

    return bloco_base


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
        bloco = obter_bloco_base(prompt)
        bot_response = gerar_resposta_com_proprias_palavras(prompt, bloco)
        st.markdown(bot_response)
        st.session_state.messages.append({"role": "assistant", "content": bot_response})
