from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Predefined responses based on common inquiries
responses = {
    "services": "We offer a range of digital marketing services including SEO, content marketing, PPC, and social media management.",
    "pricing": "Our pricing varies depending on the service and scope. Please provide more details or talk to one of our agents for a custom quote.",
    "timeline": "Timelines depend on the project complexity. For example, an SEO campaign may take 3-6 months to show results.",
    "support": "Please describe the issue you're facing, and I'll do my best to assist you or connect you with a human agent.",
    "escalation": "I’m escalating your issue to a human agent. Please wait while I connect you."
}

# Home route to serve the chatbot interface
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle user messages and return appropriate responses
@app.route('/get_response', methods=['POST'])
def get_bot_response():
    user_message = request.form['message'].lower()  # Get user input and convert it to lowercase
    
    # Basic keyword matching to determine the response
    if "services" in user_message:
        response = responses["services"]
    elif "pricing" in user_message or "cost" in user_message:
        response = responses["pricing"]
    elif "timeline" in user_message or "time" in user_message:
        response = responses["timeline"]
    elif "support" in user_message or "issue" in user_message:
        response = responses["support"]
    elif "escalation" in user_message or "escalate" in user_message:
        response = responses["escalation"]
    else:
        response = "I'm sorry, I didn't understand that. Could you please clarify or rephrase your question?"

    return jsonify({"response": response})  # Return the response as JSON

if __name__ == '__main__':
    app.run(debug=True)
