import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer, PorterStemmer



st.header("Text Analysis")



def load_data():
    return pd.read_csv("WomensClothingE-CommerceReviews - WomensClothingE-CommerceReviews.csv")



data = load_data();


sample_data = data.head(20);

st.write(sample_data["Review Text"])

st.write("Info about the Sample Data")
st.write(sample_data.info())

st.write(sample_data.describe())

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()

def preprocess_text(text):
    words = word_tokenize(text.lower())
    words = [word for word in words if word.isalpha() and word.lower() not in stop_words] 
    words = [lemmatizer.lemmatize(word) for word in words]
    words = [stemmer.stem(word) for word in words]  
    return words


sample_data['preprocessed_text'] = sample_data['Review Text'].apply(preprocess_text)


st.write("Preprocessed Text for First 5 Reviews:")
for i in range(5):
    st.write(f"Review {i + 1}: {sample_data['preprocessed_text'][i]}")
    st.write()
    st.write()

def tokenize(text):
    return word_tokenize(text)

text1 = sample_data['Division Name'].apply(preprocess_text)
text2 = sample_data['Division Name'].apply(preprocess_text)
print(text1, text2)
vectorizer = TfidfVectorizer()
vector1 = vectorizer.fit_transform(sample_data['Division Name'])
vector2 = vectorizer.transform(sample_data['Division Name'])
cosine_similarity_score = cosine_similarity(vector1, vector2)
st.write(f"Cosine Similarity Score: {cosine_similarity_score}" )
st.write(f"sum: {cosine_similarity_score}")

def jaccard_similarity(set1, set2):
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / union


jaccard_similarities = []
for t1 in text1:
    for t2 in text2:
        set1 = set(t1)
        set2 = set(t2)
        similarity_score = jaccard_similarity(set1, set2)
        jaccard_similarities.append(similarity_score)
st.write(f"Jaccard Similarity Scores: {jaccard_similarities}")

