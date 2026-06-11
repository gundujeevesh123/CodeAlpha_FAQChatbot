
from flask import Flask, render_template, request, jsonify
import re
import string

app = Flask(__name__)

products = {

    "iPhone 15": {

        "sample_faqs": [

            ["Do iPhone 14 cases fit iPhone 15?", "No, iPhone 14 cases may not fit perfectly because camera alignment and dimensions changed slightly."],

            ["What does 5G icon mean?", "The 5G icon indicates your device is connected to a 5G cellular network."],

            ["How does AirDrop work?", "AirDrop allows wireless sharing of files, photos, and videos between Apple devices."]
        ],

        "knowledge": {

            "case cover fit compatible": "iPhone 14 cases may not fit properly on iPhone 15 due to camera and design changes.",

            "5g network icon signal": "The 5G icon means the phone is connected to a 5G cellular network for faster internet speeds.",

            "airdrop share transfer file": "AirDrop allows fast wireless file transfer between nearby Apple devices.",

            "apple intelligence ai": "Apple Intelligence features are gradually rolling out depending on region and iOS version.",

            "apple card payment finance": "Apple Card can be managed using the Wallet app for payments, tracking, and billing.",

            "apple cash money transfer": "Apple Cash allows peer-to-peer money transfer directly through Apple Wallet.",

            "battery backup life": "iPhone 15 provides up to 20 hours of video playback battery backup.",

            "insurance warranty applecare": "AppleCare+ provides accidental damage coverage and hardware service support."
        }
    },

    "MacBook Air M3": {

        "sample_faqs": [

            ["Why does MacBook Air M3 slow under heavy load?", "Because the MacBook Air M3 uses a fanless design, thermal throttling can occur during heavy workloads."],

            ["Is 8GB RAM enough?", "8GB RAM is fine for normal tasks, but 16GB is recommended for heavy multitasking and editing."],

            ["Can I charge using USB-C?", "Yes, the MacBook Air M3 supports charging through both MagSafe and USB-C."]
        ],

        "knowledge": {

            "thermal heating hot throttle": "MacBook Air M3 uses a fanless design, so performance may reduce slightly during heavy workloads to control heat.",

            "8gb ram multitasking memory": "8GB RAM works for regular tasks, but 16GB RAM is better for programming, editing, and multitasking.",

            "macos sequoia update support": "MacBook Air M3 fully supports macOS Sequoia updates and Apple ecosystem features.",

            "magsafe usb c charging": "The MacBook Air M3 supports charging through both MagSafe and USB-C ports.",

            "battery backup life": "MacBook Air M3 offers up to 18 hours of battery backup under optimized usage.",

            "durability build quality": "The aluminum body provides strong durability and premium build quality.",

            "coding programming development": "MacBook Air M3 is excellent for coding, software development, and AI-related workflows."
        }
    }
}

def preprocess(text):

    text = text.lower()

    text = text.translate(str.maketrans('', '', string.punctuation))

    words = re.findall(r'\b\w+\b', text)

    return words

@app.route("/")
def home():

    return render_template("index.html", products=products)

@app.route("/ask", methods=["POST"])
def ask():

    data = request.get_json()

    question = data.get("question", "").lower()

    product = data.get("product", "")

    if not question:

        return jsonify({
            "answer": "Please ask a valid question."
        })

    user_words = preprocess(question)

    best_match = None
    best_score = 0

    for keywords, answer in products[product]["knowledge"].items():

        keyword_list = keywords.split()

        score = 0

        for word in user_words:

            if word in keyword_list:

                score += 1

        if score > best_score:

            best_score = score
            best_match = answer

    if best_match:

        return jsonify({
            "answer": best_match
        })

    return jsonify({
        "answer": f"I could not find an exact answer, but {product} is generally known for premium performance and modern features."
    })

if __name__ == "__main__":
    app.run(debug=True, port=8002)
