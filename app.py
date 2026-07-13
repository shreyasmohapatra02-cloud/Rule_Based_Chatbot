"""
Rule-Based Chatbot Web
Author: Shreyas Mohapatra
Internship: CodSoft AI Internship - Task 1
"""
from flask import Flask, render_template, request, jsonify
from chatbot import ChatBot

app = Flask(__name__)
bot = ChatBot()

@app.route("/")
def home():
    return render_template("index.html", botname=bot.botname)

@app.route("/get", methods=["POST"])
def chatbot_response():
    user_message = request.form["msg"]
    if user_message.lower().strip() == "exit":
        return jsonify({"response": "Chat closed successfully. Goodbye."})
    response = bot.get_response(user_message)
    return jsonify({"response": response})

if __name__=="__main__":
    app.run(debug=True)