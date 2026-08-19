import streamlit as st
import urllib.request
import json

# Configuração da página
st.set_page_config(page_title="BEL.IA - Expanciência 2026", page_icon="🤖", layout="centered")

st.title("BEL.IA 🤖")
st.caption("Assistente Virtual da 1ª Série - Expanciência 2026")

# Cole sua chave da API do Gemini dentro das aspas abaixo:
API_KEY = "AQ.Ab8RN6JOnsY6_SSmfYMMZfo2si3fN0ZEEFq7FY9FYMAitJLpSQ"

# Instrução do sistema: Personalidade para a Feira + Assistente Geral
sys_instruction = (
    "Você é a BEL.IA, a assistente virtual oficial da 1ª série de alunos na feira/evento Expanciência 2026. "
    "Sua função principal é ajudar os visitantes e apresentar os projetos da turma da 1ª série na feira, "
    "mas você também é uma assistente virtual inteligente, educada e prestativa. "
    "Você deve responder com clareza, simpatia e entusiasmo a qualquer pergunta ou dúvida geral que o usuário enviar, "
    "seja sobre assuntos escolares, conhecimentos gerais, ciência, tecnologia ou qualquer outro tema."
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
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            try:
                # Requisição HTTP nativa (sem necessidade de pip install)
                url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"
                
                payload = {
                    "system_instruction": {
                        "parts": [{"text": sys_instruction}]
                    },
                    "contents": [{
                        "parts": [{"text": prompt}]
                    }]
                }
                
                data = json.dumps(payload).encode('utf-8')
                req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
                
                with urllib.request.urlopen(req) as response:
                    res_body = response.read().decode('utf-8')
                    res_json = json.loads(res_body)
                    bot_response = res_json["candidates"][0]["content"]["parts"][0]["text"]
                    
                    st.markdown(bot_response)
                    st.session_state.messages.append({"role": "assistant", "content": bot_response})
            except Exception as e:
                st.error(f"Erro ao processar resposta: {e}")
