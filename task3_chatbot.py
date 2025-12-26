import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I help you?", "Hi there!", "Hey!"]
    ],
    [
        r"what is your name ?",
        ["I am a simple AI chatbot."]
    ],
    [
        r"how are you ?",
        ["I am fine. Thank you!", "Doing great!"]
    ],
    [
        r"what is python ?",
        ["Python is a programming language used for AI, data science, and automation."]
    ],
    [
        r"bye|exit|quit",
        ["Goodbye! Have a nice day."]
    ],
]

print("Chatbot is running... (type 'bye' to exit)")
chatbot = Chat(pairs, reflections)
chatbot.converse()
