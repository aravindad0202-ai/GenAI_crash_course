# n---------------------- TEXT FILE LOADER ----------------------

# from langchain_community.document_loaders import TextLoader

# file_path = r'D:\IT\AI\teaching\GenAI_module_1\RAG\LLM_Comprehensive_Guide.txt'
# loader = TextLoader(file_path)

# documents = loader.load()

# print(documents[0])


# ------------------------ PDF LOADER -------------------------
from langchain_community.document_loaders import PyPDFLoader

file_path = r'D:\IT\AI\teaching\GenAI_module_1\RAG\LLM_Comprehensive_Guide.pdf'

pdf_loader = PyPDFLoader(file_path)
documents = pdf_loader.load()

for i in documents:
    print(i)
    print('-------------------`')