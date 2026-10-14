import streamlit as st
from google import genai

# Configuração da página
st.set_page_config(page_title="BEL.IA - Expanciência 2026", page_icon="🤖", layout="centered")

# --- CSS GLOBAL COM O TOM DE FUNDO, FONTE DEL ROSE E CORES ---
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

# --- LOGO E TÍTULO ---
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

# Avatares
USER_AVATAR = "user.png"  
BOT_AVATAR = "bot.png"    

# Segurança: busca a chave nos Secrets do Streamlit
try:
    API_KEY = st.secrets["GEMINI_API_KEY"].strip()
except Exception:
    st.error("Chave não encontrada nos Secrets do Streamlit!")
    st.stop()

# Inicializa o cliente do Gemini
client = genai.Client(api_key=API_KEY)

# ==========================================
# BASE DE CONHECIMENTO OFICIAL EMBARCADA
# ==========================================
CONTEXTO_OFICIAL_PROJETO = """
- **Nome do Evento**: Expan Ciência 2026: Inteligência Artificial: Transformando o Cotidiano e a Sociedade[span_4](start_span)[span_4](end_span).
- **Subprojeto**: Inteligência Artificial e Inteligência Humana na Prática: Origem e Desenvolvimento da I.A nas Profissões no Brasil[span_5](start_span)[span_5](end_span).
- **Instituição**: Colégio Expansivo, localizado em Macapá, Amapá[span_6](start_span)[span_6](end_span)[span_7](start_span)[span_7](end_span).
- **Professores Orientadores**: Deuziana Almeida e Malrício França[span_8](start_span)[span_8](end_span).
- **Turma**: 1ª série do Ensino Médio[span_9](start_span)[span_9](end_span).
- **Data da Culminância**: 21 de novembro de 2026, das 18h às 21h (montagem das 8h às 12h)[span_10](start_span)[span_10](end_span).
- **Local do Estande**: Próximo ao refeitório (área de lazer da Educação Infantil / parquinho)[span_11](start_span)[span_11](end_span)[span_12](start_span)[span_12](end_span).
- **Estrutura dos 4 Grupos**:
  * **Grupo 1**: Aborda as diferenças entre Inteligência Artificial e Inteligência Humana, utilizando a BEL.IA para demonstração prática e comparando com a profissão de psicólogo (com participação da psicóloga convidada Cibele Valente)[span_13](start_span)[span_13](end_span)[span_14](start_span)[span_14](end_span)[span_15](start_span)[span_15](end_span). Integrantes: Graziella Belquis Gomes Dos Santos, Isadora Gemaque Dos Santos, Carolina Goldim Mira, Erick Kauã Bentes Santos, Sara Yasmin Sales da Silva, José Arthur Sena Fonseca Mendonça e Levi Lima Campos[span_16](start_span)[span_16](end_span).
  * **Grupo 2**: Aborda a história da IA e o impacto no trabalho de designers e designers gráficos (com o designer convidado Oeslem Maik)[span_17](start_span)[span_17](end_span)[span_18](start_span)[span_18](end_span)[span_19](start_span)[span_19](end_span)[span_20](start_span)[span_20](end_span). Integrantes: Gabriel Malcher Gurjão, João Paulo Melo dos Santos Guimarães, Luís Eduardo Marques Amim, Ricardo de Almeida Batista, Pedro Paulo Bentes Souza, Arthur Guedes Mesquita e Miguel Gomes dos Santos[span_21](start_span)[span_21](end_span).
  * **Grupo 3**: Apresenta a peça teatral autoral "A I.A. e o Cientista" sobre o impacto da IA no trabalho de cientistas e pesquisadores[span_22](start_span)[span_22](end_span)[span_23](start_span)[span_23](end_span)[span_24](start_span)[span_24](end_span). Integrantes: Geovana Di Maria Ribeiro Mesquita, Rafaela Ferreira Oliveira (autora do roteiro), Izabella Gonçalves Gazel Yared, Júlia Correia De Carvsalho, Maria Clara Malheiros De Souza, Maria Luisa Dos Santos Duarte e Endy Amanajás Aquino[span_25](start_span)[span_25](end_span)[span_26](start_span)[span_26](end_span)[span_27](start_span)[span_27](end_span).
  * **Grupo 4**: Desenvolve um quiz interativo sobre produções feitas por IA vs humanos, abordando a presença da IA na educação e no trabalho dos professores, com base em dados da TALIS 2024 / OCDE[span_28](start_span)[span_28](end_span)[span_29](start_span)[span_29](end_span)[span_30](start_span)[span_30](end_span). Integrantes: Elen Samilly Paixão Miranda, Samuel Luckas Rodrigues Monteiro, Ana Beatriz Fonseca Vilhena, Lucas Campos Araújo, Fernanda Yasmin Cortês Pimentel, Rúbia Beatriz Siqueira Mendonça e Pedro Oliveira Bueno[span_31](start_span)[span_31](end_span).
"""

# Instrução principal da BEL.IA
sys_instruction = (
    "Você é a BEL.IA, a assistente virtual oficial dos alunos da 1ª série na feira Expanciência 2026[span_32](start_span)[span_32](end_span). "
    "Sua função é responder dúvidas sobre o projeto utilizando estritamente e com exatidão as informações oficiais fornecidas abaixo[span_33](start_span)[span_33](end_span). "
    "REGRAS DE OURO: "
    "1. Responda de forma imediata (com máxima velocidade), clara, inteligente e com um tamanho equilibrado (nem rasa demais, nem longa demais), ideal para os jurados da feira[span_34](start_span)[span_34](end_span). "
    "2. NUNCA se apresente novamente e NUNCA use frases automáticas no final. "
    "3. Nunca invente dados que não estejam no contexto oficial. "
    "4. Responda sempre em português.\n\n"
    f"--- CONTEÚDO OFICIAL DO PROJETO ---\n{CONTEXTO_OFICIAL_PROJETO}"
)

# MENSAGEM INICIAL AUTOMÁTICA DA BEL.IA AO ABRIR O SITE
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Olá! Eu sou a BEL.IA, a assistente virtual da 1ª série para a Expanciência 2026[span_35](start_span)[span_35](end_span). Estou pronta para explicar todos os detalhes e o contexto do nosso projeto para você. O que gostaria de saber?"
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
            try:
                response = client.models.generate_content(
                    model="gemini-3.6-flash",
                    contents=prompt,
                    config={"system_instruction": sys_instruction}
                )
                bot_response = response.text
            except Exception as e:
                bot_response = "O projeto da 1ª série foca na Inteligência Artificial e Inteligência Humana na Prática para a Expanciência 2026[span_36](start_span)[span_36](end_span)!"

            st.markdown(bot_response)
            st.session_state.messages.append({"role": "assistant", "content": bot_response})
