import streamlit as st
from content_generator import generate_post
from utils import suggest_hashtags
from strategy import revamp_strategy, generate_activity_plan

st.set_page_config(page_title="Soli – AI Social Media Manager", page_icon="📱")

st.title("📱 Soli – Your AI Social Media Manager")
st.subheader("Let Soli write posts, boost your strategy, and grow your presence")

st.markdown("## ✍️ Create Social Media Posts")

# Post input section
platform = st.selectbox("Choose a platform", ["Instagram", "Facebook", "LinkedIn", "Twitter (X)"])
tone = st.selectbox("Select tone", ["Professional", "Casual", "Funny", "Inspirational", "Bold"])
length = st.selectbox("Select post length", ["Short", "Medium", "Long"])
topic = st.text_input("What is your post about?")

# Feature toggles
col1, col2, col3 = st.columns(3)
with col1:
    use_emojis = st.checkbox("Add Emojis")
with col2:
    use_hashtags = st.checkbox("Add Hashtags")
with col3:
    use_cta = st.checkbox("Include Call-To-Action")

# Generate post
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

            if isinstance(result, str) and result.startswith("❌"):
                st.error(result)
            else:
                st.success("✅ Here's your post:")
                st.markdown(result)

                if use_hashtags:
                    hashtags = suggest_hashtags(topic)
                    if hashtags:
                        st.markdown("**Suggested Hashtags:**")
                        st.write(" ".join(hashtags))

# Divider for new tools
st.markdown("---")
st.header("🧠 Soli's Strategy & Growth Tools")

# Strategy Revamp Tool
with st.expander("📈 Revamp Your Social Media Strategy"):
    st.markdown("Get personalized advice to improve your content approach and reach more people.")
    current_strategy = st.text_area("Describe your current strategy", placeholder="e.g. I post 2x/week using carousels and reels")
    goals = st.text_area("What are your goals?", placeholder="e.g. Gain 5k followers, boost link clicks, increase reach")
    platform_choice = st.selectbox("Platform for strategy advice", ["Instagram", "Facebook", "LinkedIn", "Twitter (X)"])

    if st.button("Revamp Strategy"):
        if not current_strategy or not goals:
            st.warning("Please complete all fields.")
        else:
            with st.spinner("Soli is rethinking your strategy..."):
                new_strategy = revamp_strategy(current_strategy, goals, platform_choice)
                st.success("🔄 Soli's Strategy Suggestion:")
                st.write(new_strategy)

# Activity Plan Tool
with st.expander("🚀 Boost Your Activity with a Weekly Plan"):
    st.markdown("Get a 7-day content & engagement schedule tailored to your goals.")
    act_goals = st.text_area("What do you want to achieve this week?", placeholder="e.g. Increase comments, boost story views")
    act_platform = st.selectbox("Platform for activity plan", ["Instagram", "Facebook", "LinkedIn", "Twitter (X)"])

    if st.button("Generate Activity Plan"):
        if not act_goals:
            st.warning("Please enter your goals.")
        else:
            with st.spinner("Soli is creating your weekly activity plan..."):
                plan = generate_activity_plan(act_platform, act_goals)
                st.success("📅 Weekly Social Media Activity Plan:")
                st.write(plan)

# Footer
st.markdown("---")
st.caption("✨ Powered by OpenAI · Created by You · Soli is always improving.")
