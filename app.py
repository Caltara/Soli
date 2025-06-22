import os
import streamlit as st
from openai import OpenAI
from openai import OpenAIError

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY", st.secrets.get("OPENAI_API_KEY")))

@st.cache_data(show_spinner=False)
def revamp_strategy(current_strategy, goals, platform="Instagram"):
    prompt = f"""
You are a top-tier social media consultant. A user is currently doing this on {platform}:

Current Strategy: {current_strategy}

Goals: {goals}

Provide a detailed, improved strategy with actionable steps to improve reach, engagement, and follower growth.
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
def generate_activity_plan(platform, goals):
    prompt = f"""
You are an expert social media manager. Based on the following platform and user goals, create a weekly activity plan to boost presence:

Platform: {platform}
Goals: {goals}

Give a 7-day schedule with post ideas, interaction strategies, and time-of-day suggestions.
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
