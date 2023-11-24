from flask import Flask, render_template, request
from datetime import datetime
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.tree import DecisionTreeClassifier
from nltk.stem import WordNetLemmatizer
import nltk.chat.util
import scipy.sparse

app = Flask(__name__)

# Load the model and the vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Define a function to preprocess the input symptoms
def preprocess(symptoms):
    words = symptoms.split()
    lemmatizer = WordNetLemmatizer()
    lemmas = [lemmatizer.lemmatize(word) for word in words]
    return " ".join(lemmas)

def postprocess(disease):
    return disease.title()

greetings = [
    (r"hi|hello|hey", ["Hello, I am a health care chatbot. How can I help you?", "Hey, I am a health care chatbot. How can I help you?"]),
    (r"how are you|how do you do", ["I am fine, thank you.", "I am doing well, thank you.", "I am good, thank you."]),
    (r"what is your name|who are you", ["I am a health care chatbot.", "My name is HealthBot.", "I am HealthBot, a health care chatbot."]),
    (r"you are amazing|you are awesome|you are great", ["Thank you for your kind words.", "You are too kind.", "You made my day."]),
    (r"thank you|thanks|thankyou", ["You are welcome.", "It's my pleasure.", "No problem."]),
    (r"bye|goodbye|see you", ["Bye for now.", "Goodbye, take care.", "See you soon."])
]

greetbot = nltk.chat.util.Chat(greetings)

def is_greeting(input_symptoms):
    return greetbot.respond(input_symptoms) is not None

def get_greeting_response(input_symptoms):
    return greetbot.respond(input_symptoms)

you = []
bot = ["Hello I am a bot Happy to see you , tell me your problem ."]
time = []

@app.route('/')
def index():
    return render_template('chatbot.html')

@app.route('/get', methods=["GET", "POST"])
def chatbot():
    if request.method == "POST":
        time_now = datetime.now().strftime("%H:%M")
        input_symptoms = request.form.get('names')
        if len(input_symptoms) != 0:
            you.append(input_symptoms)
            if is_greeting(input_symptoms):
                output_disease = get_greeting_response(input_symptoms)
            else:
                processed_symptoms = preprocess(input_symptoms)
                input_vector = vectorizer.transform([processed_symptoms])
                output_disease = model.predict(input_vector)[0]
                output_disease = postprocess(output_disease)
            bot.append(output_disease)
            time.append(time_now)
        return render_template('chatbot.html', results=zip(you, bot, time))
    else:
        you.clear()
        bot.clear()
        return render_template('chatbot.html')

if __name__ == '__main__':
    app.run(debug=True)
