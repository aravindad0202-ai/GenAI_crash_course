from dotenv import load_dotenv


load_dotenv(r'D:\Aravind\GenAI_crash_course\.env')
import os


from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from google import genai


print('Initiating Gemini Models')
embedder = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001", api_key=os.getenv('GEMINI_API_KEY'))
client = genai.Client()
print('embedding model loaded')


class IngestionPipeline:
    def __init__(self, file_path: str):
        self.file_path = file_path


    def load_document(self):
        print('--------------------- Document loading initiated ---------------')
        loader = PyPDFLoader(self.file_path)
        self.documents = loader.load()
        print('--------------------- Document loaded successfully ---------------')


    def chunking(self):
        print('--------------------- Document chunking initiated ---------------')
        chunker = RecursiveCharacterTextSplitter(
            separators=['\n\n', '\n', ' ', ''],
            chunk_size = 250,
            chunk_overlap = 100,
            length_function = len
        )
        self.chunks = chunker.split_documents(self.documents)
        print('--------------------- Document Chunked Successfully ---------------')


    def load_VDb(self):
        print('--------------------- Load data into Vector DB initiated ---------------')
        namespace = 'rag-demo'
        vdb = Chroma.from_documents(
            documents=self.chunks,
            embedding=embedder,
            collection_name=namespace,
            persist_directory=r'D:\Aravind\GenAI_crash_course\Projects\Project 5'
        )
        print('---------------------- Data loaded successfully ---------------------')


    def ingest_document(self):
        print('------------------------------- START DATA INGESTION -------------------------')
        self.load_document()
        self.chunking()
        self.load_VDb()
        print('------------------------------- DATA INGESTION SUCCESSFULL -------------------------')


class RetrieverPipeline:

    def load_vectors(self):
        self.VDb = Chroma(
            embedding_function=embedder,
            collection_name='rag-demo',
            persist_directory=r'D:\Aravind\GenAI_crash_course\Projects\Project 5'
        )

    def retriever(self):
        self.retrived_documents = self.VDb.similarity_search_with_score(query=self.query, k=3)

    def construct_prompt(self):
        base_prompt = """Assume that you are a helpful AI assistant. you need to answer the query given in triple backticks.
        based on the source document given below.
        your output must be only based on Source document you are not allowed to answer the query by your own.
       
        ```
        {query}
        ```
       
        # SOURCE DOCUMENT:
        {sources}
        """
        retrived_document_formated: str = ''
        for docs in self.retrived_documents:
            retrived_document_formated = retrived_document_formated + docs.page_content
            retrived_document_formated = retrived_document_formated + '\n --------------------------------- \n'


        self.prompt = base_prompt.format(query = self.query, sources = retrived_document_formated)

        print('=================== PROMPT =================================')
        print(self.prompt)

    def generate(self):
        output = client.models.generate_content(
            model = "gemini-3.5-flash",
            content = self.prompt
        )
        print('=================== OUTPUT =================================')
        print(output.text)

    def rag(self, query):
        self.query = query
        self.load_vectors()
        self.construct_prompt()
        self.generate()




# --------------------------------------- DATA INGESTION --------------------------------
ingester = IngestionPipeline(r'D:\Aravind\GenAI_crash_course\Projects\Project 5\docs\LLM_Comprehensive_Guide.pdf')
ingester.ingest_document()


# --------------------------------------- DATA RETREIVEL --------------------------------
# retriever = RetrieverPipeline()
# retriever.rag('Explain how to call the llm.')
