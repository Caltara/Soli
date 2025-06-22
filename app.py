import streamlit as st
from content_generator import generate_post
from utils import suggest_hashtags

st.set_page_config(page_title="📱 Social Media Manager AI", page_icon="📱")

st.title("📱 Social Media Manager AI")
st.subheader("Let AI write engaging posts for you in seconds!")

# User input
platform = st.selectbox("Choose a platform", ["Instagram", "Facebook", "LinkedIn", "Twitter (X)"])
tone = st.selectbox("Select tone", ["Professional", "Casual", "Funny", "Inspirational", "Bold"])
length = st.selectbox("Select post length", ["Short", "Medium", "Long"])
topic = st.text_input("What is your post about?")

# Extra options
col1, col2, col3 = st.columns(3)
with col1:
    use_emojis = st.checkbox("Add Emojis")
with col2:
    use_hashtags = st.checkbox("Add Hashtags")
with col3:
    use_cta = st.checkbox("Include Call-To-Action")

# Generate button
if st.button("Generate Post"):
    if not topic.strip():
        st.warning("Please enter a topic.")
    else:
        with st.spinner("Writing your post..."):
            result = generate_post(
                topic=topic,
                platform=platform,
                tone=tone,
                length=length,
                include_emojis=use_emojis,
                include_hashtags=use_hashtags,
                include_cta=use_cta
            )

            if isinstance(result, dict) and "error" in result:
                st.error(result["error"])
            else:
                st.success("✅ Here's your post:")
                st.markdown(result)

                if use_hashtags:
                    hashtags = suggest_hashtags(topic)
                    if hashtags:
                        st.markdown("**Suggested Hashtags:**")
                        st.write(" ".join(hashtags))
