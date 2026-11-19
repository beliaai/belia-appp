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


def responder_por_palavra_chave(pergunta: str) -> str | None:
    p = pergunta.lower()

    if any(k in p for k in ["grupo 1", "grupo um", "psicologia", "psicólogo", "psicologo", "cibele", "transformer", "attention", "nome", "bel.ia", "belquis", "graziella", "criou", "criação"]):
        return (
            "### GRUPO 1: Inteligência Artificial vs. Inteligência Humana e a Psicologia\n\n"
            "- **Abordagem:** Estuda as diferenças entre IA e inteligência humana, explicando o funcionamento básico de sistemas computacionais, e utiliza a **BEL.IA** para uma demonstração prática interativa.\n"
            "- **Problematização Profissional:** Utiliza a profissão de **Psicólogo**. Uma IA pode reconhecer padrões de conversação e gerar respostas coerentes, mas não possui consciência, sentimentos, escuta empática, construção de vínculos ou responsabilidade ética e subjetiva.\n"
            "- **Convidada Especial:** Psicóloga **Cibele Valente**.\n"
            "- **Referência Teórica Principal:** Artigo *'Attention Is All You Need'* (Vaswani et al., 2017) sobre a arquitetura Transformer e mecanismos de atenção.\n"
            "- **Sobre a BEL.IA:** Criada por **Graziella Belquis Gomes dos Santos** ao longo de **4 meses de estudo e muita pesquisa**. O nome **BEL.IA** vem diretamente da junção de **'Bel'** (de Belquis) com **'IA'** (Inteligência Artificial).\n"
            "- **Integrantes do Grupo 1:** Graziella Belquis Gomes Dos Santos, Isadora Gemaque Dos Santos, Carolina Gondim Mira, Erick Kauã Bentes Santos, Sara Yasmin Sales da Silva, José Arthur Sena Fonseca Mendonça e Levi Lima Campos."
        )

    if any(k in p for k in ["grupo 2", "grupo dois", "design", "gráfico", "grafico", "história", "historia", "oeslem", "generativa", "autoria"]):
        return (
            "### GRUPO 2: História da IA e o Impacto no Design Gráfico\n\n"
            "- **Abordagem:** Analisa a origem, evolução e marcos históricos da Inteligência Artificial até o cenário atual de IA generativa.\n"
            "- **Problematização Profissional:** Relaciona a evolução da IA ao trabalho de designers e designers gráficos, discutindo as mudanças na criação, edição de imagens, prototipagem, autoria, criatividade e originalidade.\n"
            "- **Convidado Especial:** Designer gráfico **Oeslem Maik**.\n"
            "- **Referência Teórica Principal:** E-book *'Introdução à Inteligência Artificial'* (Cegraf UFG, 2025).\n"
            "- **Integrantes do Grupo 2:** Gabriel Malcher Gurjão, João Paulo Melo dos Santos Guimarães, Luís Eduardo Marques Amim, Ricardo de Almeida Batista, Pedro Paulo Bentes Souza, Arthur Guedes Mesquita e Miguel Gomes dos Santos."
        )

    if any(k in p for k in ["grupo 3", "grupo três", "grupo tres", "peça", "peca", "teatro", "teatral", "cientista", "laboratório", "laboratorio", "ruth salles", "enredo", "elenco"]):
        return (
            "### GRUPO 3: Peça Teatral 'A I.A. e o Cientista' e o Trabalho Científico\n\n"
            "- **Abordagem:** Investiga os impactos da IA na vida e no trabalho de cientistas e pesquisadores através de uma peça teatral autoral.\n"
            "- **Enredo da Peça:** Um cientista genial, criativo, porém solitário e inseguro, cria uma IA para auxiliar em suas pesquisas. No início
