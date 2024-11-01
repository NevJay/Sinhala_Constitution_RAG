from langchain_community.embeddings.ollama import OllamaEmbeddings
# from :class:`~langchain_ollama import OllamaEmbeddings


def get_embedding_function(platform, model_type):
    if platform == "ollama":
        if model_type == "gemma":
            model_name = "gemma2:27b-instruct-q4_0"
        if model_type == "llama3":
            model_name = "llama3.2:3b"
        
        embeddings = OllamaEmbeddings(
            model = model_name,
            # num_gpu=-1,
            # num_thread=6,
            show_progress=False
        )

        return embeddings
    
    # if platform == "llama_index":
    #     if model_type == "bert":
    #         model_name = "NLPC-UOM/SinBERT-large"
    #     if model_type == "roberta":
    #         model_name = "d42kw01f/Sinhala-RoBERTa"

    #     embedings = HuggingFaceEmbedding(
    #         model_name = model_name,
    #         max_length=512
    #     )

        # def get_text_embedding(text, embeddings):
        #     embedded = embeddings.embed_query(text)
        #     return embedded

        return embeddings


if __name__ == "__main__":

    embed_model = get_embedding_function(platform = "ollama", model_type = "gemma")

    print("Model: ", embed_model.get_text_embeddings("වෘත්තීය සමිති පිහිටුවීමේ සහ වෘත්තීසමිතිවලට බැඳීමේ නිදහසක් ව්‍යවස්ථාවෙන් ලබා දී ඇත්තේ වරප්‍රසාද ලත් පිරිසකට පමණක් ද?"))