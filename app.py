import streamlit as st
from textblob import TextBlob

# Page setup
st.set_page_config(page_title="Sentiment Analyzer", page_icon="😊")

# Title
st.title("😊 Sentiment Analyzer")
st.write("Type any text and I will tell you if it is Positive, Negative, or Neutral!")

# Text input
user_text = st.text_area("Enter your text here:", height=150)

# Analyze button
if st.button("Analyze Sentiment"):
    if user_text == "":
        st.warning("Please enter some text first!")
    else:
        # Analyze sentiment
        blob = TextBlob(user_text)
        score = blob.sentiment.polarity

        # Show result
        if score > 0:
            st.success("✅ Positive Sentiment 😊")
        elif score < 0:
            st.error("❌ Negative Sentiment 😠")
        else:
            st.info("➡️ Neutral Sentiment 😐")

        # Show score
        st.write(f"Confidence Score: {round(score, 2)}")