# 📚 Resumo de Textos e Livros - LLM Assistant 🤖

Este projeto é uma aplicação web criada com **Streamlit** 🌐 e **Hugging Face Inference API** 🔥, que permite gerar **resumos de textos** e **páginas de livros** em diversos idiomas 🌍, utilizando um modelo de linguagem (LLM - Large Language Model) para a geração e tradução de resumos. O modelo LLM é especializado em resumir textos e traduzi-los para o idioma solicitado pelo usuário. 📝✨

## 🚀 Funcionalidades

- **📝 Geração de Resumos**: O assistente gera resumos concisos de textos ou páginas de livros inseridos pelo usuário.
- **🌐 Tradução Automática**: O modelo traduz o resumo gerado para o idioma escolhido pelo usuário.
- **👨‍💻 Interface Interativa**: Criada com **Streamlit**, onde o usuário pode facilmente inserir o texto ou página e escolher o idioma de saída para o resumo.

## 🏗️ Arquitetura

O código foi desenvolvido utilizando os seguintes conceitos:
- **SOLID**: O código foi estruturado de forma a seguir os princípios SOLID, com classes e funções bem definidas 💡.
- **Hugging Face LLM**: O modelo de linguagem é acessado via API do **Hugging Face** 🔑.
- **Streamlit**: A interface foi construída com o framework Streamlit para facilitar a interação com o usuário 💻.

## ⚙️ Pré-Requisitos

Antes de rodar o projeto, é necessário ter as seguintes ferramentas instaladas:

- Python 3.7 ou superior 🐍
- `pip` ou `conda` para gerenciar as dependências 📦
- Conta no [Hugging Face](https://huggingface.co) e chave de API para acessar o modelo 🔑

## 💻 Instalação

### 🖥️ Windows

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/thaleson/AI_summarizes
   cd resumo-textos-llm
   ```

2. **Instale o Python**:
   Baixe e instale o Python 3.7 ou superior a partir de [python.org](https://www.python.org/downloads/) 🧑‍💻.

3. **Crie um ambiente virtual** (opcional, mas recomendado):
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate
   ```

4. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Defina as variáveis de ambiente**:
   Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:
   ```bash
   API_KEY=<sua-chave-huggingface>
   MODEL_URL=<url-do-modelo>
   ```

6. **Execute o aplicativo**:
   ```bash
   streamlit run main.py
   ```

### 🍏 MacOS / 🐧 Linux

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/resumo-textos-llm.git
   cd resumo-textos-llm
   ```

2. **Instale o Python**:
   - Para macOS: Use o [Homebrew](https://brew.sh/) ou baixe do [python.org](https://www.python.org/downloads/) 🍏.
   - Para Linux: Use o `apt` ou `dnf` para instalar o Python 🐧.

3. **Crie um ambiente virtual** (opcional, mas recomendado):
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

4. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Defina as variáveis de ambiente**:
   Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:
   ```bash
   API_KEY=<sua-chave-huggingface>
   MODEL_URL=<url-do-modelo>
   ```

6. **Execute o aplicativo**:
   ```bash
   streamlit run main.py
   ```

## 🤖 Como Funciona

1. **📝 Geração de Resumo**: O usuário insere um texto ou uma página de livro na interface. O assistente gera um resumo conciso e claro do conteúdo.
2. **🌐 Tradução**: O usuário pode escolher o idioma em que o resumo será gerado. O modelo faz a tradução automática para o idioma selecionado.
3. **📲 Exibição do Resultado**: O resumo traduzido é exibido na interface de forma clara e estruturada.

### ⚙️ Exemplo de Fluxo

1. O usuário insere um texto ou página de livro 📚.
2. O usuário escolhe o idioma do resumo (exemplo: "Inglês") 🌎.
3. O modelo gera o resumo e o traduz para o idioma escolhido 🌐.
4. O resumo gerado é mostrado na interface 🖥️.

## 💡 Detalhes do Modelo LLM

O modelo utilizado para gerar os resumos e traduções é um modelo pré-treinado de **Hugging Face**. Este modelo foi treinado para processar e gerar textos de alta qualidade, com uma capacidade especial para resumir grandes volumes de texto e realizar traduções automáticas.

### 🔧 Configuração do LLM

1. **API do Hugging Face**: O modelo é acessado via API do Hugging Face. Para utilizar a API, você precisa de uma chave de API, que pode ser obtida ao criar uma conta no Hugging Face e gerar a chave através do painel de controle 🔑.
2. **Parâmetros Ajustáveis**: A aplicação permite ajustar parâmetros como `max_tokens`, `temperature`, e `top_p` para controlar o comportamento das respostas do modelo. Estes parâmetros ajudam a garantir resumos mais curtos, coerentes e precisos 💬.

## 🤝 Contribuições

Sinta-se à vontade para contribuir para o projeto! Se você encontrar um bug 🐞 ou quiser sugerir melhorias 💡, crie um **issue** ou envie um **pull request** 🚀.

---

