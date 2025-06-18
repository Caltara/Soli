import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_post(topic, platform, tone):
    prompt = f"""Write a {tone.lower()} {platform.lower()} post about "{topic}". 
Include a strong hook and make it engaging. Keep it short and optimized for {platform}.
Do not include hashtags or emojis."""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant who writes great social media content."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    
    return response['choices'][0]['message']['content'].strip()
