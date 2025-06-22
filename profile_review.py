import os
import streamlit as st
from openai import OpenAI
from openai import OpenAIError

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY", st.secrets.get("OPENAI_API_KEY")))

@st.cache_data(show_spinner=False)
def review_profile(bio, link, platform):
    prompt = f"""
You are a social media profile design expert. Review the following {platform} profile:

Bio: {bio}
Link in bio: {link}

Give design tips to improve visual appeal, engagement, and click-through.
"""

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.8
        )
        return response.choices[0].message.content.strip()
    except OpenAIError as e:
        return f"❌ Error: {str(e)}"

@st.cache_data(show_spinner=False)
def brand_consultation(description, audience):
    prompt = f"""
You're a brand consultant. A creator describes their content as:

"{description}"

Their target audience is: {audience}

Give recommendations to strengthen their brand image, visual identity, and tone.
"""

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.8
        )
        return response.choices[0].message.content.strip()
    except OpenAIError as e:
        return f"❌ Error: {str(e)}"
