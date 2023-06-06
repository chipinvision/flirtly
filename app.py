from flask import Flask, jsonify
import random

app = Flask(__name__)

pickup_lines = [
    "Are you a magician? Because whenever I look at you, everyone else disappears.",
    "Do you have a name, or can I call you mine?",
    "Is your name Google? Because you have everything I've been searching for.",
    "Excuse me, but I think you dropped something: my jaw.",
    "Is your dad a baker? Because you're a cutie pie!",
    "Do you believe in love at first sight, or should I walk by again?",
    "If you were a vegetable, you'd be a cute-cumber.",
    "Is your dad a boxer? Because you're a knockout!",
    "Can I follow you home? Cause my parents always told me to follow my dreams.",
    "Are you a parking ticket? Because you've got 'FINE' written all over you.",
    "Tired of being an adult? Then by my baby",
    "I seem to have lost my phone number. Can I have yours?",
    "If looks could kill, you\’d be a weapon of mass destruction.",
    "Is your name Wi-Fi? Because I am really started to feel a connection.",
    "Are you a dictionary? Cause you’re adding meaning to my life.",
    "You must be debt, because my interest in you is growing.",
    "i wanna c_ddle and k_ss. But u and i aren't together",
    "Aside from being sexy, what do you do for a living?",
    "Are you chocolate pudding? 'Cause i want to spoon you.",
    "Are you a camera? Because every time I see you I smile",
    "You don’t need keys to drive me crazy.",
    "You’re so beautiful you made me forget my pickup line.",
    "My doctor said, I'm lacking Vitamin U",
    "Your pussy seems so dry, can i make it wet using my cum",
]

@app.route('/pickup', methods=['GET'])
def get_pickup_line():
    random_line = random.choice(pickup_lines)
    return jsonify({'line': random_line})

if __name__ == '__main__':
    app.run()