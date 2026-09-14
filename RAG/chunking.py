sample_text = """Artificial Intelligence is rapidly evolving.
It is transforming industries such as healthcare, finance, and education. Maachine learning, a subset of AI, involves training models on vast amounts of data.

Natural Language Processing allows computers to understand human language. This has led to the rise of advanced chatbots and virtual assistants."""

# --------------loading document -----------------
from langchain_community.document_loaders import PyPDFLoader

file_path = r'D:\IT\AI\teaching\GenAI_module_1\RAG\LLM_Comprehensive_Guide.pdf'

pdf_loader = PyPDFLoader(file_path)
documents = pdf_loader.load()

# ------------------------------------------ SPLITTERS -----------------------------
# from langchain_text_splitters import CharacterTextSplitter
# chunker = CharacterTextSplitter(
#     chunk_size=90,
#     chunk_overlap=10,
#     length_function = len,
#     separator=""
# )

# chunks = chunker.split_text(sample_text)

# print(chunks)

# print(len(chunks))

# from langchain_text_splitters import RecursiveCharacterTextSplitter
# recursive_chunker = RecursiveCharacterTextSplitter(
#     chunk_size=90,
#     chunk_overlap=10,
#     length_function=len,
#     separators = ['\n\n','\n'," ",""]
# )

# chunks = recursive_chunker.split_text(sample_text)
# print(chunks)
# print(len(chunks))


from langchain_text_splitters import TokenTextSplitter

token_chunker = TokenTextSplitter(
    chunk_size = 300,
    chunk_overlap = 50,
    encoding_name="cl100k_base", # The encoding used by GPT-4 and GPT-3.5
)

chunks = token_chunker.split_documents(documents)
print(len(chunks))
print(chunks)