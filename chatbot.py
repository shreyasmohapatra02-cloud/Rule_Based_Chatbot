"""
Rule-Based Chatbot Core Logic
Author: Shreyas Mohapatra
"""
import random
from datetime import datetime

class ChatBot:
    def __init__(self):
        self.botname = "Smart ChatBot"
        self.jokes = [
            "My brain said work hard, but my body replied, let's sleep first and discuss tomorrow.",
            "Why do programmers prefer dark mode? Because light attracts bugs.",
            "I asked my computer why it was slow. It said, Too many problems are running in the background… just like you.",
        ]
    # EMOTION WORD LISTS
        self.happy_words = ["happy","great", "awesome", "amazing", "excellent", "fantastic", "wonderful", "joy", "glad", "excited", "cheerful", "smile", "smiling"]
        self.sad_words = ["sad", "down", "upset", "unhappy", "depressed", "cry", "crying", "lonely", "hurt", "heartbroken", "bad day", "terrible", "not okay", "low", "miserable"]
        self.angry_words = ["angry", "mad", "furious", "annoyed", "frustrated", "irritated", "hate", "rage"]
        self.stress_words = ["stress", "stressed", "pressure", "overwhelmed", "tension", "worried", "anxious", "panic", "nervous"]
        self.tired_words = ["tired", "sleepy", "exhausted", "fatigue", "weak", "drained", "lazy"]
        self.bored_words = ["bored", "boring", "nothing to do", "idle", "free", "alone"]
        self.fear_words = ["afraid", "scared", "fear", "frightened", "terrified", "nervous"]

    def get_response(self, message):
        user = message.lower().strip()
        
        # GREETINGS FIRST
        if user=="good morning":
            return "Good morning! Have a wonderful day ahead."
        elif user=="good afternoon":
            return "Good afternoon! Hope you're having a great day."
        elif user=="good evening":
            return "Good evening! How was your day?"
        elif user=="good night":
            return "Good night! Sleep well and have sweet dreams."
        elif "hello" in user or "hi" in user:
            return "Hello! It's nice to see you. How can I help you today?"
        elif user=="what's up":
            return "Not much! How are you doing today?"

        # TIME AND DATE RULES
        elif "time" in user:
            current_time = datetime.now().strftime("%I:%M %p")
            return f"The current time is {current_time}"
        elif "date" in user or "today" in user:
            today_date=datetime.now().strftime("%d %B %Y")
            today_day=datetime.now().strftime("%A")
            return f"Today is {today_day}, {today_date}"
        elif "day" in user:
            today_day=datetime.now().strftime("%A")
            return f"Today is {today_day}"

        # EMOTION DETECTION
        elif any(word in user for word in self.happy_words):
            return "I'm glad you're feeling happy! Keep smiling."
        elif any(word in user for word in self.sad_words):
            return "I'm sorry you're feeling sad. Would you like to tell me what happened?"
        elif any(word in user for word in self.angry_words):
            return "I understand you're angry. Would you like to talk about it?"
        elif any(word in user for word in self.stress_words):
            return "You seem stressed. Try to relax for a moment. I'm here if you want to talk."
        elif any(word in user for word in self.tired_words):
            return "You sound tired. Make sure to get some rest."
        elif any(word in user for word in self.bored_words):
            return "Let's do something fun! We can chat or play a quiz."
        elif any(word in user for word in self.fear_words):
            return "I'm sorry you're feeling scared. Would you like to tell me what's worrying you?"

        # SPECIFIC EMOTIONS
        elif user=="how are you":
            return "I am doing well. Thank you for asking. How are you?"
        elif user=="i am fine":
            return "That's great to hear! How can I help you today?"
        elif user=="i am happy":
            return "That's wonderful! I'm glad you're feeling happy."
        elif user=="i am sad":
            return "I'm sorry you're feeling sad. Would you like to tell me what happened?"
        elif user=="i am excited":
            return "That's awesome! What are you excited about?"
        elif user=="i am angry":
            return "I'm sorry you're feeling angry. Would you like to talk about it?"
        elif user=="i am stressed":
            return "I'm sorry you're feeling stressed. Take a deep breath. How can I help?"
        elif user=="i am worried":
            return "I understand. What are you worried about?"
        elif user=="i am tired":
            return "You should get some rest if you can. Is there anything I can help you with?"
        elif user=="i am bored":
            return "Let's do something fun! We can chat, play a game, or learn something new."

        # Q&A
        elif user=="what is your name":
            return "My name is Rule Based ChatBot. Nice to meet you!"
        elif user=="who created you":
            return "I was created by Shreyas Mohapatra using Python as a chatbot project."
        elif user=="what is python":
            return "Python is an easy programming language used to create software, websites, artificial intelligence, automation, and many other applications."
        elif "father of python" in user:
            return "Guido van Rossum is the creator of Python."
        elif user=="what is ai" or user == "what is artificial intelligence":
            return "Artificial Intelligence is a technology that helps computers learn, solve problems, and make decisions like humans."
        elif "father of ai" in user or "father of artificial intelligence" in user:
            return "John McCarthy is known as the father of Artificial Intelligence."
        elif user=="what is computer":
            return "A computer is an electronic device that accepts data, processes it, and gives useful information."
        elif user=="what is chatbot":
            return "A chatbot is a computer program that communicates with users and answers their questions."
        elif user=="what is hardware":
            return "Hardware is the physical parts of a computer like the keyboard, mouse, monitor, and CPU."
        elif user=="what is software":
            return "Software is a collection of programs that tells a computer what to do."
        elif user=="what is cpu":
            return "CPU stands for Central Processing Unit. It is called the brain of the computer."
        elif user=="what is ram":
            return "RAM stands for Random Access Memory. It stores temporary data while the computer is running."
        elif user=="what is internet":
            return "The Internet is a worldwide network that connects millions of computers."
        elif user=="what is machine learning":
            return "Machine learning is a part of Artificial Intelligence that allows computers to learn from data."
        elif user=="what is cybersecurity":
            return "Cybersecurity protects computers, networks, and data from cyber attacks."
        elif user=="what can you do":
            return "I can answer questions, tell time, date, and detect how you're feeling."
        elif user=="who are you":
            return "I am Smart ChatBot. I am here to help you."
        elif user=="what is your purpose":
            return "My purpose is to answer your questions and help you learn."

        # FUN
        elif "joke" in user:
            joke = random.choice(self.jokes)
            return joke
        elif user=="thank you" or user=="thanks" or user=="thank you so much" or user=="many many thanks":
            return "You're welcome. Happy to help."
        elif user=="bye":
            return "Goodbye. Have a nice day."
        else:
            return "Sorry, I don't know the answer to that question."