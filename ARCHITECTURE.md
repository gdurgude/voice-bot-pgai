# Architecture

## How It Works

The voice bot is built on three components working together: Twilio for telephony, Flask for webhook handling, and the Anthropic Claude API for generating realistic patient responses.

When `main.py` runs, it iterates through 12 patient scenarios and uses the Twilio REST API to initiate outbound calls to the Pretty Good AI test number (+1-805-439-8008). Twilio is configured to hit our Flask server's `/answer` webhook when the call connects. The `/answer` route returns TwiML — Twilio's XML-based call control language — that speaks the patient's opening line using text-to-speech and opens a `<Gather>` block to listen for the agent's response via speech recognition. When the agent responds, Twilio transcribes the speech and POSTs the text to our `/respond` webhook. That route passes the transcribed text to Claude Haiku via the Anthropic API, which generates a natural, contextually appropriate patient reply. The reply is spoken back using Twilio's Alice voice and the loop continues until the conversation concludes with a goodbye. Every turn is saved to a transcript file, and Twilio's call recording feature captures the full audio as an MP3.

## Key Design Choices

I chose Twilio over Vonage and other providers because of its reliable webhook architecture, built-in call recording, and clean TwiML format that makes it easy to control conversation flow. For the AI patient, I used Claude Haiku rather than a larger model because latency matters in real-time voice — Haiku responds fast enough that the conversation doesn't feel awkward. I deliberately kept the patient persona simple and natural (1-2 sentence responses, goal-driven) so it behaves like a real caller rather than a scripted bot. ngrok is used to expose the local Flask server to Twilio's webhooks during development, which keeps the setup lightweight without requiring cloud deployment. Scenarios are defined separately in `scenarios.py` so they can be extended or modified independently of the core bot logic.
