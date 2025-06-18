import streamlit as st
from content_generator import generate_post
from utils import suggest_hashtags

st.set_page_config(page_title="Social Media Manager AI", page_icon="📱")

st.title("📱 Social Media Manager AI")
st.subheader("Let AI write engaging posts for you!")

platform = st.selectbox("Choose a platform", ["Instagram", "LinkedIn", "Twitter (X)"])
tone = st.selectbox("Select tone", ["Professional", "Casual", "Funny", "Inspirational", "Bold"])
topic = st.text_input("What is your post about?")

if st.button("Generate Post"):
    if topic.strip() == "":
        st.warning("Please enter a topic.")
    else:
        with st.spinner("Generating post..."):
            post = generate_post(topic, platform, tone)
            hashtags = suggest_hashtags(topic)
            st.success("Here’s your post:")
            st.write(post)
            st.markdown("**Suggested Hashtags:**")
            st.write(" ".join(hashtags))
