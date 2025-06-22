import os
from openai import OpenAI
from openai import OpenAIError
import streamlit as st

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY", st.secrets.get("OPENAI_API_KEY")))

@st.cache_data(show_spinner=False)
def generate_post(topic, platform, tone, length="Medium", include_emojis=False, include_hashtags=False, include_cta=False):
    extras = []

    if include_emojis:
        extras.append("Include appropriate emojis.")
    if include_hashtags:
        extras.append("Add relevant and trending hashtags.")
    if include_cta:
        extras.append("Add a call-to-action at the end of the post.")
    if platform.lower() == "linkedin":
        extras.append("Use Markdown formatting where appropriate (e.g., bold headings or bullet points).")

    length_map = {
        "Short": "Keep the post under 30 words.",
        "Medium": "Keep the post around 50 words.",
        "Long": "Write a detailed post of up to 100 words."
    }
    length_instruction = length_map.get(length, "")

    prompt = f"""Write a {tone.lower()} {platform.lower()} post about "{topic}". 
Include a strong hook and make it engaging. {length_instruction} {' '.join(extras)}"""

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant who writes great social media content."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        return response.choices[0].message.content.strip()

    except OpenAIError as e:
        return f"❌ OpenAI API Error: {str(e)}"
