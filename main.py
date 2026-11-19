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
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; width: 100%; margin-top: 0px; margin-bottom: 20px;">
        <img src="https://raw.githubusercontent.com/beliaai/belia-appp/main/bot.png" width="115" style="border-radius: 8px; display: block; margin-bottom: -10px;">
        <div class="titulo-belia">BEL.IA</div>
        <div style="color: #0077B6; font-size: 1rem; margin-top: 2px; font-weight: 600;">Assistente Virtual da 1ª Série - Expanciência 2026</div>
    </div>
    """,
    unsafe_allow_html=True,
)

USER_AVATAR = "user.png"
BOT_AVATAR = "bot.png"

chave_api = st.secrets.get("GEMINI_API_KEY", "").strip()


def responder_por_palavra_chave(pergunta: str):
    p = pergunta.lower()

    if any(k in p for k in ["grupo 1", "grupo um", "psicologia", "psicólogo", "psicologo", "cibele", "transformer", "attention", "nome", "bel.ia", "belquis", "graziella", "criou", "criação"]):
        return "\n".join([
            "### GRUPO 1: Inteligência Artificial vs. Inteligência Humana e a Psicologia",
            "",
            "- **Abordagem:** Estuda as diferenças entre IA e inteligência humana, explicando o funcionamento básico de sistemas computacionais, e utiliza a **BEL.IA** para uma demonstração prática interativa.",
            "- **Problematização Profissional:** Utiliza a profissão de **Psicólogo**. Uma IA pode reconhecer padrões de conversação e gerar respostas coerentes, mas não possui consciência, sentimentos, escuta empática, construção de vínculos ou responsabilidade ética e subjetiva.",
            "- **Convidada Especial:** Psicóloga **Cibele Valente**.",
            "- **Referência Teórica Principal:** Artigo *'Attention Is All You Need'* (Vaswani et al., 2017) sobre a arquitetura Transformer e mecanismos de atenção.",
            "- **Sobre a BEL.IA:** Criada por **Graziella Belquis Gomes dos Santos** ao longo de **4 meses de estudo e muita pesquisa**. O nome **BEL.IA** vem diretamente da junção de **'Bel'** (de Belquis) com **'IA'** (Inteligência Artificial).",
            "- **Integrantes do Grupo 1:** Graziella Belquis Gomes Dos Santos, Isadora Gemaque Dos Santos, Carolina Gondim Mira, Erick Kauã Bentes Santos, Sara Yasmin Sales da Silva, José Arthur Sena Fonseca Mendonça e Levi Lima Campos.",
        ])

    if any(k in p for k in ["grupo 2", "grupo dois", "design", "gráfico", "grafico", "história", "historia", "oeslem", "generativa", "autoria"]):
        return "\n".join([
            "### GRUPO 2: História da IA e o Impacto no Design Gráfico",
            "",
            "- **Abordagem:** Analisa a origem, evolução e marcos históricos da Inteligência Artificial até o cenário atual de IA generativa.",
            "- **Problematização Profissional:** Relaciona a evolução da IA ao trabalho de designers e designers gráficos, discutindo as mudanças na criação, edição de imagens, prototipagem, autoria, criatividade e originalidade.",
            "- **Convidado Especial:** Designer gráfico **Oeslem Maik**.",
            "- **Referência Teórica Principal:** E-book *'Introdução à Inteligência Artificial'* (Cegraf UFG, 2025).",
            "- **Integrantes do Grupo 2:** Gabriel Malcher Gurjão, João Paulo Melo dos Santos Guimarães, Luís Eduardo Marques Amim, Ricardo de Almeida Batista, Pedro Paulo Bentes Souza, Arthur Guedes Mesquita e Miguel Gomes dos Santos.",
        ])

    if any(k in p for k in ["grupo 3", "grupo três", "grupo tres", "peça", "peca", "teatro", "teatral", "cientista", "laboratório", "laboratorio", "ruth salles", "enredo", "elenco"]):
        return "\n".join([
            "### GRUPO 3: Peça Teatral 'A I.A. e o Cientista' e o Trabalho Científico",
            "",
            "- **Abordagem:** Investiga os impactos da IA na vida e no trabalho de cientistas e pesquisadores através de uma peça teatral autoral.",
            "- **Enredo da Peça:** Um cientista genial, criativo, porém solitário e inseguro, cria uma IA para auxiliar em suas pesquisas. No início há perfeita colaboração. Com o tempo, o cientista passa a depender totalmente da máquina para criar e duvidar de sua própria capacidade intelectual. A IA passa a rejeitar suas ideias e argumenta que apenas combina dados criados por humanos. No clímax, ao tentar desligá-la, o cientista percebe que precisa recuperar sua autonomia, desliga o sistema e volta a escrever suas próprias ideias no papel.",
            "- **Elenco e Produção:** Narrador (**Maria Clara Malheiros de Souza**); Inteligência Artificial (**Rafaela Ferreira Oliveira** — autora do roteiro — e **Izabella Gonçalves Gazel Yared**); Cientista (**Maria Luisa dos Santos Duarte** e **Júlia Correia de Carvalho**); Figurante (**Geovana Di Maria Ribeiro Mesquita**); Produção (**Endy Amanajás Aquino**).",
            "- **Recursos e Cenário:** Cenário de laboratório científico (mesa, jaleco para o cientista, figurino de robô para a IA, trilha sonora e efeitos sonoros), com duração de aproximadamente **10 minutos** e **5 ensaios programados**.",
            "- **Referência Pedagógica:** Obra *'Teatro na Escola'* (Ruth Salles).",
        ])

    if any(k in p for k in ["grupo 4", "grupo quatro", "educação", "educacao", "quiz", "professor", "professores", "talis", "56%", "ocde", "escola"]):
        return "\n".join([
            "### GRUPO 4: A IA na Educação e o Quiz Interativo",
            "",
            "- **Abordagem:** Desenvolve um quiz interativo envolvendo produções feitas por IA e por seres humanos para debater a presença da tecnologia na escola e no trabalho dos professores.",
            "- **Dados Estatísticos Oficiais:** Utiliza dados da Pesquisa Internacional sobre Ensino e Aprendizagem (**TALIS 2024**), divulgada pela **OCDE** e **Agência Brasil**, que indicam que **56% dos professores brasileiros** usam IA para planejar aulas, buscar metodologias eficientes e adaptar materiais.",
            "- **Discussão:** A IA como ferramenta de apoio pedagógico versus o papel insubstituível do professor na mediação, avaliação crítica e sensibilidade humana.",
            "- **Integrantes do Grupo 4:** Elen Samilly Paixão Miranda, Samuel Luckas Rodrigues Monteiro, Ana Beatriz Fonseca Vilhena, Lucas Campos Araújo, Fernanda Yasmin Cortês Pimentel, Rúbia Beatriz Siqueira Mendonça e Pedro Oliveira Bueno.",
        ])

    if any(k in p for k in ["grupos", "quatro grupos", "divisão", "divisao", "equipes", "integrantes"]):
        return "\n".join([
            "### Os Quatro Grupos de Trabalho da 1ª Série",
            "",
            "O trabalho colaborativo foi dividido em **4 grupos** orientados pelos professores **Deuziana Almeida** e **Malrício França**:",
            "",
            "1. **Grupo 1 — IA vs. Inteligência Humana e a Psicologia:** Demonstração prática com a **BEL.IA** (criada por Graziella Belquis em 4 meses de estudo), convidada **Psicóloga Cibele Valente** e referência no artigo *'Attention Is All You Need'* (Vaswani et al., 2017).",
            "2. **Grupo 2 — História da IA e o Impacto no Design Gráfico:** Evolução até a IA generativa, criação, autoria e originalidade no design, convidado **Oeslem Maik** e e-book *'Introdução à Inteligência Artificial'* (Cegraf UFG, 2025).",
            "3. **Grupo 3 — Peça Teatral 'A I.A. e o Cientista':** Encenação autoral de ~10 min sobre autonomia intelectual diante da IA, inspirada em *'Teatro na Escola'* (Ruth Salles).",
            "4. **Grupo 4 — A IA na Educação e o Quiz Interativo:** Quiz diferenciando produções humanas e de IA, com dados da pesquisa **TALIS 2024** (OCDE / Agência Brasil) indicando que **56% dos professores brasileiros** usam IA como apoio pedagógico.",
        ])

    if any(k in p for k in ["tempo", "demorou", "prazo", "meses", "cronograma", "quando começou", "etapas", "fases", "metodologia"]):
        return "\n".join([
            "### Metodologia e Cronograma do Projeto",
            "",
            "- **Metodologia:** Trabalho colaborativo dividido em 4 grupos orientados pelos professores **Deuziana Almeida** e **Malrício França**, utilizando exposição, demonstrações práticas e encenação teatral.",
            "- **1ª Fase (Agosto e Setembro):** Orientações iniciais, divisão dos grupos, levantamento de informações, acompanhamento via WhatsApp, estudo da obra *'Introdução à Inteligência Artificial'* (UFG) e elaboração do trabalho escrito.",
            "- **2ª Fase (Outubro e Novembro):** Reuniões de alinhamento, definição de apresentações, ensaios (**5 ensaios programados** para a peça teatral), preparação de materiais e montagem do estande no dia 21 de novembro.",
            "- **Desenvolvimento da BEL.IA:** A criação da assistente virtual se estendeu por **4 meses de estudo e muita pesquisa**.",
        ])

    if any(k in p for k in ["problema", "hipótese", "hipotese", "justificativa", "objetivo", "objetivos", "pesquisa", "teoria", "fundamentação"]):
        return "\n".join([
            "### Problema de Pesquisa, Hipóteses, Justificativa e Objetivos",
            "",
            "- **Problema de Pesquisa:** De que maneira o desenvolvimento da Inteligência Artificial tem transformado as atividades humanas e profissionais no Brasil, e quais são suas possibilidades, contribuições e impactos em relação ao trabalho realizado pela inteligência humana?",
            "- **Hipóteses:** A IA transforma atividades profissionais e exige novas interações; pode auxiliar nas tarefas e aumentar a produtividade sem substituir totalmente o humano; gera impactos positivos e negativos, exigindo novas competências.",
            "- **Justificativa:** Compreender a presença crescente da IA no mercado de trabalho, avaliando seus benefícios (produtividade, auxílio na criação) e seus riscos (substituição, dependência e desafios para os trabalhadores).",
            "- **Objetivo Geral:** Compreender a origem, o desenvolvimento e o funcionamento da IA, refletindo sobre sua relação com a inteligência humana e seus impactos nas profissões e no trabalho no Brasil, por meio de pesquisa, produção escrita e apresentação prática.",
            "- **Objetivos Específicos:** Organizar conteúdos em grupo, preparar atividades práticas, encenações e estratégias de interação com o público, e socializar os conhecimentos na culminância.",
        ])

    if any(k in p for k in ["culminância", "culminancia", "sábado", "sabado", "dia 21", "horário", "horario", "hora", "local", "estande", "onde", "orientadores", "coordenação", "coordenacao", "avaliação", "avaliacao", "nota", "público", "publico"]):
        return "\n".join([
            "### Dados da Culminância — Expanciência 2026",
            "",
            "- **Instituição:** Colégio Expansivo — Educação Infantil, Ensino Fundamental e Ensino Médio (Macapá/AP).",
            "- **Data:** **21 de novembro de 2026**.",
            "- **Horário da Apresentação:** Das **18h às 21h** (montagem do estande das **8h às 12h**).",
            "- **Local:** Estande coletivo localizado na área próxima ao refeitório (área de lazer da Educação Infantil / parquinho).",
            "- **Público Esperado:** Mais de **600 pessoas** (estudantes, professores, pais, familiares, comunidade escolar e convidados externos).",
            "- **Orientadores:** Professores **Deuziana Almeida** e **Malrício França**.",
            "- **Coordenação Pedagógica:** Professoras **Jovelina Souto** e **Andréa Santa Rosa**.",
            "- **Avaliação:** Atividade obrigatória para obtenção de nota no **3º instrumento avaliativo de todas as disciplinas do 3º bimestre** da 1ª série do Ensino Médio.",
        ])

    if any(k in p for k in ["projeto", "subprojeto", "expanciência", "expancia", "1ª série", "1a serie", "primeira série", "primeira serie", "resumo", "sobre o que"]):
        return "\n".join([
            "### Projeto Expanciência 2026 — 1ª Série do Ensino Médio (Colégio Expansivo)",
            "",
            "- **Projeto Geral:** *Expan Ciência: Inteligência Artificial: Transformando o Cotidiano e a Sociedade*.",
            "- **Subprojeto:** *Inteligência Artificial e Inteligência Humana na Prática: Origem e Desenvolvimento da I.A nas Profissões no Brasil*.",
            "- **Orientadores:** Deuziana Almeida e Malrício França | **Coordenação Pedagógica:** Jovelina Souto e Andréa Santa Rosa.",
            "- **Síntese:** O projeto analisa como sistemas de IA processam grandes volumes de dados, reconhecem padrões e transformam as profissões no Brasil, destacando a diferença fundamental entre o processamento computacional e a experiência, emoção, consciência, escuta empática e compreensão subjetiva da inteligência humana.",
            "- **Estrutura em 4 Grupos:**",
            "  1. **Grupo 1:** IA vs. Inteligência Humana e a Psicologia (com a **BEL.IA** e a psicóloga **Cibele Valente**).",
            "  2. **Grupo 2:** História da IA e o Impacto no Design Gráfico (com o designer **Oeslem Maik**).",
            "  3. **Grupo 3:** Peça Teatral autoral *'A I.A. e o Cientista'*.",
            "  4. **Grupo 4:** A IA na Educação e o Quiz Interativo (dados da pesquisa **TALIS 2024**).",
            "- **Culminância:** **21 de novembro de 2026**, das **18h às 21h**, no Colégio Expansivo (Macapá/AP).",
        ])

    return None


def responder_pergunta_de_fora(pergunta: str) -> str:
    if not chave_api:
        return (
            "Essa pergunta é de fora do nosso projeto da Expanciência e a chave GEMINI_API_KEY "
            "não foi encontrada nos Secrets do Streamlit."
        )

    try:
        genai.configure(api_key=chave_api)
        model = genai.GenerativeModel(
            model_name="gemini-3.8-flash",
            system_instruction=(
                "Você é a BEL.IA, uma assistente virtual inteligente, simpática e clara criada pela aluna Graziella Belquis "
                "para a Expanciência 2026 do Colégio Expansivo. Responda a perguntas gerais de fora do projeto de forma "
                "clara, objetiva e útil."
            ),
        )
        response = model.generate_content(
            pergunta,
            generation_config={
                "temperature": 0.6,
                "max_output_tokens": 350,
            },
            request_options={"timeout": 12},
        )
        if response and response.text and response.text.strip():
            return response.text.strip()
        return "A API respondeu vazia no momento. Tente perguntar novamente."
    except Exception as e:
        return f"Não consegui responder agora por este motivo: {type(e).__name__}: {e}"


if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Olá! Eu sou a BEL.IA, a assistente virtual da 1ª série para a Expanciência 2026. Estou pronta para explicar os detalhes do nosso projeto 'Inteligência Artificial e Inteligência Humana na Prática'. O que você gostaria de saber?",
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
        resposta_projeto = responder_por_palavra_chave(prompt)
        if resposta_projeto:
            bot_response = resposta_projeto
        else:
            with st.spinner("Consultando..."):
                bot_response = responder_pergunta_de_fora(prompt)

        st.markdown(bot_response)
        st.session_state.messages.append({"role": "assistant", "content": bot_response})
