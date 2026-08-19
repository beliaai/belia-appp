import streamlit as st
import urllib.request
import json

# Configuração da página
st.set_page_config(page_title="BEL.IA - Expanciência 2026", page_icon="🤖", layout="centered")

st.title("BEL.IA 🤖")
st.caption("Assistente Virtual da 1ª Série - Expanciência 2026")

# Cole sua chave da API do Gemini dentro das aspas abaixo:
API_KEY = "AQ.Ab8RN6JOnsY6_SSmfYMMZfo2si3fN0ZEEFq7FY9FYMAitJLpSQ"

# Instrução do sistema
sys_instruction = (
    "Você é a BEL.IA, a assistente virtual oficial da 1ª série de alunos na feira Expanciência 2026. "
    "Sua função principal é ajudar os visitantes e apresentar os projetos da turma, "
    "mas você também é uma assistente virtual inteligente e prestativa para qualquer dúvida geral."
)

# Inicializa o histórico
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibe histórico
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Entrada do usuário
if prompt := st.chat_input("Pergunte algo para a BEL.IA..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            try:
                # Remove espaços em branco acidentais da chave
                clean_key = API_KEY.strip()
                url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={clean_key}"
                
                payload = {
                    "contents": [{
                        "parts": [{"text": prompt}]
                    }],
                    "systemInstruction": {
                        "parts": [{"text": sys_instruction}]
                    }
                }
                
                data = json.dumps(payload).encode('utf-8')
                req = urllib.request.Request(
                    url, 
                    data=data, 
                    headers={"Content-Type": "application/json"}
                )
                
                with urllib.request.urlopen(req) as response:
                    res_body = response.read().decode('utf-8')
                    res_json = json.loads(res_body)
                    bot_response = res_json["candidates"][0]["content"]["parts"][0]["text"]
                    
                    st.markdown(bot_response)
                    st.session_state.messages.append({"role": "assistant", "content": bot_response})
            except Exception as e:
                st.error(f"Erro ao processar resposta: {e}")
