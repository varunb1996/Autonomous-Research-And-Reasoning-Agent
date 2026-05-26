import os
import streamlit as st

from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()

client = TavilyClient(
    api_key=st.secrets["TAVILY_API_KEY"]
)


def search_web(query):

    response = client.search(
        query=query,
        search_depth="advanced",
        max_results=5
    )

    return response["results"]
