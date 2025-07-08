Sentiment Classification of IMDB Movie Reviews

This project is a text classification app that uses TF-IDF vectorization and Scikit-learn models to classify movie reviews as either positive or negative. The focus is on building a clean preprocessing pipeline and leveraging traditional machine learning to deliver reliable sentiment predictions.

The initial corpus had over 214,000 unique tokens. By limiting the feature space to the most informative 5,000 tokens using max_features=5000, we were able to significantly reduce noise and improve the model’s performance by approximately 1% in accuracy.
📂 Dataset Source

IMDB Dataset of 50K Movie Reviews

This dataset consists of 50,000 highly polarized movie reviews for binary sentiment classification.
▶️ How to Run the App

    Clone the repository

git clone <your-repo-url>

Navigate to the app directory

cd app

Run the Streamlit app

    streamlit run main.py

Tech Stack

    Python

    Pandas

    Scikit-learn

    NLTK

    BeautifulSoup

    Streamlit