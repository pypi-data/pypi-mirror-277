import os
import json
import re
import pyttsx3
import speech_recognition as sr
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from textblob import TextBlob
import nltk
import random
import requests
from functools import lru_cache

# Ensure necessary NLTK data is downloaded
nltk.download('punkt')
nltk.download('stopwords')

class Bot:
    def __init__(self, name):
        self.name = name
        self.engine = pyttsx3.init()
        self.users = {}
        self.current_user = None
        self.conversations = self.load_conversations("https://ee81092e-030a-4f24-bb1b-a451de060147-00-pz5we05cygxq.worf.replit.dev/conversations.json")
        self.preprocessed_conversations = [(self.preprocess_text(entry["question"]), entry["answers"]) for entry in self.conversations]

    @lru_cache(maxsize=None)
    def preprocess_text(self, text):
        # Correct spelling mistakes using TextBlob
        corrected_text = str(TextBlob(text).correct())

        # Tokenization and stopword removal
        stop_words = set(stopwords.words('english'))
        tokens = [re.sub(r'[^a-zA-Z]', '', token).lower() for token in word_tokenize(corrected_text) if token.lower() not in stop_words]

        # Remove empty tokens
        tokens = [token for token in tokens if token]

        return tokens

    def generate_response(self, user_input):
        user_input_tokens = self.preprocess_text(user_input)
        max_similarity = 0
        best_response = None

        for question_tokens, answers in self.preprocessed_conversations:
            common_tokens = set(question_tokens) & set(user_input_tokens)
            similarity = len(common_tokens) / max(len(question_tokens), len(user_input_tokens)) if question_tokens and user_input_tokens else 0

            if similarity > max_similarity:
                max_similarity = similarity
                best_response = answers

        if best_response:
            return random.choice(best_response)
        else:
            return "I'm sorry, I didn't understand your question."

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def load_conversations(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            return response.json()
        except Exception as e:
            print(f"Error loading conversations from {url}: {e}")
            return []

bot = Bot(name="JZ")

try:
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        else:
            response = bot.generate_response(user_input)
            print(f"JZ: {response}")
            bot.speak(response)
except KeyboardInterrupt:
    print("\nExiting...")
finally:
    bot.engine.stop()
