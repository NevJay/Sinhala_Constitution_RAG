import argparse
from langchain.vectorstores.chroma import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama
from get_embedding_function import get_embedding_function

CHROMA_PATH = "./database"
DATA_PATH = "./sources"
SUFFIX_PATH = "./sources/Sri Lanka Constitution-Sinhala_SR.txt"
PLATFORM = "ollama"
MODEL_TYPE = "gemma"
MODEL_NAME = "gemma2:27b-instruct-q4_0"
# MODEL_NAME = "llama3.2:3b"

PROMPT_TEMPLATE = """
You are an AI assistant. You can understand English But You can only respond in Sinhala Language. Your goal is to answer questions based on the constitution of Sri Lanka based on the following context provided:'

{context}

Answer the following question using only the context given above. Do not include your opinions. Keep the answer clear. Give reasons for yes or no questions. Keep answers short:

{question}

"""

def main(query=None):
    # parser = argparse.ArgumentParser()
    # parser.add_argument("query_text", type=str, help="The query text")
    # args = parser.parse_args()
    # query_text = args.query_text
    return query_rag(query)


def query_rag(query_text:str):
    embedding_function = get_embedding_function(model_type=MODEL_TYPE, platform=PLATFORM)
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)
    suffix_removed = suffix_removal(query_text)
    # query_text = embedding_function.embed_query(query_text)
    results = db.similarity_search_with_score(suffix_removed, k=5)
    # print("*"*100, query_text, "*"*100)
    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)

    print(prompt)

    # model = "mapler/gpt2"
    model = Ollama(
        model=MODEL_NAME,
        num_gpu=-1,
        verbose=True
    )

    response_text = model.invoke(prompt)

    sources = [doc.metadata.get("page_content", None) for doc, _score in results]
    formatted_response = f"Response: {response_text}\nSources: {sources}"

    print(formatted_response)
    return response_text

    # print(prompt)


def suffix_removal(question):
    with open(SUFFIX_PATH, "r", encoding="utf8") as file:
        suffixes = file.read()

    question = question.split(" ")

    new_text = []
    for word in question:
        for suffix in suffixes:
            if word.lower().endswith(suffix.lower()):
                word = word[0:-len(suffix)]
        new_text.append(word)

    concatenated_string = ' '.join(new_text)
    return concatenated_string


if __name__ == "__main__":
    main()
