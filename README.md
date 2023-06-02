# whatsapp-translator-bot
Basically a wrapper around the ChatGPT API for Whatsapp using twilio.

# How it Works
I have a phone number hosted on Twilio that has a Whatsapp business account.
When the number receives a message, it makes a POST request to my flask web server.

The script pulls out the message text and sends a prompt to CHatGPT (very easy with LangChain).
In this case, the prompt is asking for a translation, but this could be anything.

When ChatGPT returns an answer, that answer is sent back to Twilio, who then sends it as a reply from my hosted number.
