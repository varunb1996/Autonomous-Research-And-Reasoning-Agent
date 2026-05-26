import os
import streamlit as st

from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)


def run_llm(prompt):

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content
