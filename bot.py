from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.schema import (
    HumanMessage,
)

app = Flask(__name__)
chat = ChatOpenAI(temperature=0.5, model_name="gpt-3.5-turbo")

@app.route('/webhook', methods=['POST'])
def whatsapp_webhook():
    # from_number = request.values.get('From', '')

    # Extract the message
    incoming_message = request.values.get('Body', '')

    # Define the prompt
    prompt = PromptTemplate(
        input_variables=["message"],
        template = "JSON translate '{message}': English if Portuguese, else Portuguese. Message: {message} "
    )

    # Translate the message
    ai_response = chat([HumanMessage(content=prompt.format(message=incoming_message))])
    translated_message = ai_response.content

    # Create a Twilio response
    response = MessagingResponse()
    response.message(translated_message)
    return str(response)

if __name__ == '__main__':
    app.run(port=8000)  # run the app on port 8000
