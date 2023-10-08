import os
import json

from langchain import hub
from langchain.schema import Document
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.schema.messages import BaseMessageChunk
from langchain.text_splitter import CharacterTextSplitter
from langchain.schema.runnable import RunnablePassthrough

from config import DB_PATH


def custom_load(dataset_path: str) -> list[Document]:
    """"""

    with open(dataset_path, "r") as f:
        docs = json.load(f)

    return [
        Document(
            page_content=qa['Question_original'],
            metadata={"answer": qa['Answer_plain_text']}
        )
        for qa in docs
    ]


def get_answer(api_token: str, question: str) -> BaseMessageChunk:

    llm = ChatOpenAI(
        model_name="gpt-3.5-turbo-16k",
        openai_api_key=api_token,
        temperature=0.5,
        max_tokens=2048
    )
    embeddings = OpenAIEmbeddings(openai_api_key=api_token)

    documents = custom_load("./static/FAQ.json")
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    splits = text_splitter.split_documents(documents=documents)

    if not os.path.exists(DB_PATH):
        vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings, persist_directory=DB_PATH)
    else:
        vectorstore = Chroma(persist_directory=DB_PATH, embedding_function=embeddings)

    retriever = vectorstore.as_retriever()

    rag_prompt = hub.pull("rlm/rag-prompt")

    rag_chain = (
            {"context": retriever, "question": RunnablePassthrough()}
            | rag_prompt
            | llm
    )

    return rag_chain.invoke(question)


if __name__ == "__main__":
    """Testing Purposes"""
