import streamlit as st
import joblib

model = joblib.load("model.pkl")

st.title("Twitter Sentiment Analyzer")

tweet = st.text_area("Enter a tweet")

if st.button("Analyze"):
    if tweet:
        result = model.predict([tweet])[0]
        st.success(f"Sentiment: {result}")
    else:
        st.warning("Please enter text")