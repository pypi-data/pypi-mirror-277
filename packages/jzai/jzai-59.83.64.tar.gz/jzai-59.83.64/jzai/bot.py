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

# Ensure necessary NLTK data is downloaded
nltk.download('punkt')
nltk.download('stopwords')


class Bot:
    def __init__(self, name):
        self.name = name
        self.engine = pyttsx3.init()
        self.users = {}
        self.current_user = None
        self.conversations = self.load_conversations("conversations.json")

    def preprocess_text(self, text):
        # Correct spelling mistakes using TextBlob
        corrected_text = str(TextBlob(text).correct())

        # Tokenization
        tokens = word_tokenize(corrected_text)

        # Stopword removal and remove non-alphabetic characters
        stop_words = set(stopwords.words('english'))
        tokens = [re.sub(r'[^a-zA-Z]', '', token).lower() for token in tokens if token.lower() not in stop_words]

        # Remove empty tokens
        tokens = [token for token in tokens if token]

        return tokens

    def generate_response(self, user_input):
        max_similarity = 0
        best_response = None
        try:
            for entry in self.conversations:
                question = entry["question"]
                question_tokens = self.preprocess_text(question)
                user_input_tokens = self.preprocess_text(user_input)
                common_tokens = set(question_tokens) & set(user_input_tokens)

                # Check for division by zero
                if len(question_tokens) == 0 or len(user_input_tokens) == 0:
                    similarity = 0
                else:
                    similarity = len(common_tokens) / max(len(question_tokens), len(user_input_tokens))

                if similarity > max_similarity:
                    max_similarity = similarity
                    best_response = entry.get("answers", ["I'm sorry, I don't have a response for that."])

            if best_response:
                return random.choice(best_response)
            else:
                return "I'm sorry, I didn't understand your question."

        except BaseException as e:
            return f"Error: {e}"

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def load_conversations(self, file_name):
        try:
            package_dir = os.path.dirname(__file__)
            file_path = os.path.join(package_dir, file_name)
            with open(file_path, 'r') as file:
                return json.load(file)
        except Exception as e:
            print(f"Error loading {file_name}: {e}")
            return None



bot = Bot(name="JZ")

try:
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        else:
            bot.process_input(user_input)
except KeyboardInterrupt:
    print("\nExiting...")
finally:
    bot.engine.stop()