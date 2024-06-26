# Research Companion

![Research Companion](/screenshots/image.png "Research Companion")

This LLM project is to help researchers to find exact information from the research papers and articles without reading the whole document. Researcher can provide the URLs of the research papers and articles and the system will extract the information from the papers and articles according to provided question, and provide the exact information to the researcher. Also when storing the information, the system will store them in a structured format separeting the information into smaller chunks and retrieve only the required information when needed by doing a semantic search on the vectordatabase. This helps to reduce the monthly cost for the LLM services and helps to reduce the time taken to analyze the research papers and articles.

## Used Technologies
- **LangChain🦜️🔗** - A modern framework to connect language models with external data sources.
- **Chroma☁️** - AI-native open-source vector database
- **Gemini-Pro✨** - LLM platform to perform language model tasks.
- **Gemini-Embeddings🧬** - Model to encapsulate information into dense representations in a multi-dimensional space 
- **Python🐍** - Programming language used to develop the system.

## Architecture
![Architecture](/screenshots/architecture.png "Architecture")

## Getting Started
#### 1. Clone the repository
Clone the repository to your local machine using the following command.
```
https://github.com/Irash-Perera/ResearchCompanion.git
```

#### 2. Install the dependencies
Install the dependencies using the following command.
```
pip install -r requirements.txt
```
#### 3. Create an environment file
Create a file called `env.py` in the root directory and add the following code.
```
API_KEY = "<Your API KEY>"
```
You can create your own API key [here](https://aistudio.google.com/app/apikey).

#### 4. Run the application
Run the application using the following command.
```
streamlit run app.py
```
