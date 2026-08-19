import streamlit as st
import google.generativeai as genai

# Configuração da página
st.set_page_config(page_title="BEL.IA - Expanciência 2026", page_icon="🤖", layout="centered")

st.title("BEL.IA 🤖")
st.caption("Assistente Virtual da 1ª Série - Expanciência 2026")

# Cole sua chave da API do Gemini dentro das aspas abaixo:
API_KEY = "AQ.Ab8RN6JOnsY6_SSmfYMMZfo2si3fN0ZEEFq7FY9FYMAitJLpSQ"

# Configura o Gemini com a chave de API
genai.configure(api_key=API_KEY)

# Instrução do sistema: Personalidade para a Feira + Assistente Geral
sys_instruction = (
    "Você é a BEL.IA, a assistente virtual oficial da 1ª série de alunos na feira/evento Expanciência 2026. "
    "Sua função principal é ajudar os visitantes e apresentar os projetos da turma da 1ª série na feira, "
    "mas você também é uma assistente virtual inteligente, educada e prestativa. "
    "Você deve responder com clareza, simpatia e entusiasmo a qualquer pergunta ou dúvida geral que o usuário enviar, "
    "seja sobre assuntos escolares, conhecimentos gerais, ciência, tecnologia ou qualquer outro tema."
)

# Inicializa o modelo Gemini
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=sys_instruction
)

# Inicializa o histórico de mensagens
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibe o histórico de mensagens na tela
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Campo de entrada para a pergunta do usuário
if prompt := st.chat_input("Pergunte algo para a BEL.IA..."):
    # Salva e mostra a mensagem do usuário
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Gera e exibe a resposta da IA
    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            try:
                response = model.generate_content(prompt)
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            except Exception as e:
                st.error(f"Erro ao processar resposta: {e}")
