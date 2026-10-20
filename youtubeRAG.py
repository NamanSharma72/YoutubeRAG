# We see that we have very long youtube videos and we sometimes see it all , 
# SO we will create a rag system for youtube , so that we can get the information of any video on youtube , its summary , what happened in the video
# what questions were asked , what were the answers etc.

# Plan of action:

# 1) Download the youtube video transcript , contains the written conversation of the video in written format
# for this we will use youtube api 

# 2) Then using a text splitter we will create chunks of the transcript because it can be too long

# 3) Then we will create the embedding vectors for each chunk

# 4) The put these embeddings into the vector store 

# 5) Then whenever the user sends us a query , it goes to the retriever , retriever with the help of vector store converts the query to embeddings and makes the 
# vector store to perform a similarity search 

# 6) Once we get the relevant chunks we give it to the llm along with the query and llm gives us the answer.

from youtube_transcript_api import YouTubeTranscriptApi , TranscriptsDisabled
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_groq import ChatGroq
from langchain_chroma import Chroma
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

video_id = "p4qPp_3_f2Y"
api = YouTubeTranscriptApi()

try:
    fetched_transcript = api.fetch(video_id , languages=["en"])
    transcript_list = fetched_transcript.to_raw_data()
    transcript = " ".join(chunk["text"] for chunk in transcript_list)
    print(transcript_list)
except TranscriptsDisabled:
    print("No captions available for this video")


