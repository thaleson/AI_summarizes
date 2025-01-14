import streamlit as st  # type: ignore
from app.utils.env_loader import load_env
from app.services.llm_service import LLMService

# Configuração da página principal
st.set_page_config(page_title="Resumo de Textos e Livros", page_icon="📚")

st.markdown(
    f"""
    <style>
    {open("static/styles.css").read()}
    </style>
    """,
    unsafe_allow_html=True
)

# Carregar configurações do ambiente
env = load_env()
api_key = env["API_KEY"]
model_url = env["MODEL_URL"]

# Inicializar serviço LLM
llm_service = LLMService(api_key=api_key, model_url=model_url)

# Interface do usuário
st.title("Resumo de Textos e Livros 📖")
st.write("Insira o texto ou a página do livro abaixo para gerar um resumo.")

# Entrada de texto do usuário
user_text = st.text_area("Texto ou Página", height=300, placeholder="Cole aqui o texto ou página do livro...")

# Idioma desejado para o resumo
target_language = st.selectbox(
    "Escolha o idioma do resumo:",
    ["Português", "Inglês", "Espanhol", "Francês", "Alemão", "Italiano", "Chinês", "Japonês"]
)

# Botão para gerar o resumo
if st.button("Gerar Resumo"):
    if user_text.strip():
        # Contexto para o modelo
        system_message = {
            "role": "system",
            "content": (
                "Você é um especialista em geração de resumos curtos e claros. "
                "Faça um resumo conciso do texto fornecido e traduza-o para o idioma especificado pelo usuário."
            )
        }
        user_message = {"role": "user", "content": f"### Texto para resumo:\n\n{user_text}\n\nIdioma: {target_language}"}
        messages = [system_message, user_message]

        # Consultar LLM
        with st.spinner("Gerando resumo..."):
            try:
                response = llm_service.chat_completion(
                    messages=messages,
                    max_tokens=300,  # Limitar tamanho do resumo
                    temperature=0.5,  # Balancear criatividade e precisão
                    top_p=0.9
                )
        
                st.write("---")  # Separador para visualizar melhor o resumo
                st.chat_message("human").markdown(f"### Resumo do Texto em: {target_language}")
                st.chat_message("ai").markdown(response)(response.content)
          
            except Exception as e:
                st.error(f"Erro ao consultar o modelo: {e}")
    else:
        st.warning("Por favor, insira o texto para gerar o resumo.")
