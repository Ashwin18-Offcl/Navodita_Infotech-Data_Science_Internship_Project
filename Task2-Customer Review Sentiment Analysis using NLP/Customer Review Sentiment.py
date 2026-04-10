import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import os
print(os.getcwd())
# Load dataset
df = pd.read_csv(r"F:\Navodita_Infotech-Data_Science_Internship_Project\Task2-Customer Review Sentiment Analysis using NLP\reviews.csv")

# Features & Labels
X = df['review']
y = df['sentiment']

# Convert text to numeric
vectorizer = TfidfVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2)

# Model
model = LogisticRegression()
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))