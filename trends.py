import os
import streamlit as st
from openai import OpenAI
from openai import OpenAIError

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY", st.secrets.get("OPENAI_API_KEY")))

@st.cache_data(show_spinner=False)
def find_trends(niche):
    prompt = f"""
You are a social media trend forecaster. What are the top 3 current and upcoming content trends for:

Niche: {niche}

Give practical trend names and how to apply them.
"""

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except OpenAIError as e:
        return f"❌ Error: {str(e)}"
