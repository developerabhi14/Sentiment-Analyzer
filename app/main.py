import streamlit as st
import joblib

model=joblib.load("model.pkl")
vectorizer=joblib.load("tfidf.pkl")

st.title("Sentiment Analyzer")

user_input=st.text_area("Enter your review here")
if st.button("Analyze"):
    x=vectorizer.transform([user_input])
    prediction=model.predict(x)
    st.write(f"**Sentiment:**{prediction[0]}")
