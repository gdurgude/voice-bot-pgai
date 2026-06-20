import os
import json
import anthropic
import requests as req
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse, Gather
from flask import Flask, request
from config import (
    TWILIO_ACCOUNT_SID,
    TWILIO_AUTH_TOKEN,
    TWILIO_PHONE_NUMBER,
    ANTHROPIC_API_KEY,
    TEST_NUMBER,
    NGROK_URL
)

app = Flask(__name__)
twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
anthropic_client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

conversation_history = {}
active_scenarios = {}

SCENARIOS = [
    "I need to schedule an appointment for a routine checkup next week.",
    "I need to refill my prescription for lisinopril.",
    "I want to cancel my appointment on Friday.",
    "What are your office hours and do you accept Blue Cross insurance?",
    "I need an urgent appointment, I have chest pain.",
]

current_scenario_index = 0


def generate_patient_response(agent_said, scenario):
    message = anthropic_client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=100,
        system=f"""You are a patient calling a medical office.
Your goal: {scenario}
Keep responses to 1-2 sentences. Sound natural and human.
If your goal is complete, say 'Thank you, goodbye.'""",
        messages=[
            {"role": "user", "content": f"The agent just said: {agent_said}\nYour response:"}
        ]
    )
    return message.content[0].text.strip()


@app.route("/answer", methods=["GET", "POST"])
def answer():
    call_sid = request.values.get("CallSid", "unknown")
    scenario = active_scenarios.get(call_sid, SCENARIOS[current_scenario_index % len(SCENARIOS)])
    conversation_history[call_sid] = {"turns": [], "scenario": scenario}

    response = VoiceResponse()
    gather = Gather(
        input="speech",
        action=f"{NGROK_URL}/respond",
        method="POST",
        timeout=10,
        speech_timeout="5",
        language="en-US"
    )
    gather.say("Hello, I'd like to schedule an appointment please.", voice="alice")
    response.append(gather)

    return str(response), 200, {"Content-Type": "text/xml"}


@app.route("/respond", methods=["GET", "POST"])
def respond():
    call_sid = request.values.get("CallSid", "unknown")
    agent_said = request.values.get("SpeechResult", "")

    print(f"Agent said: {agent_said}")

    history = conversation_history.get(call_sid, {"scenario": SCENARIOS[0]})
    scenario = history.get("scenario", SCENARIOS[0])

    patient_reply = generate_patient_response(agent_said, scenario)
    print(f"Patient reply: {patient_reply}")

    save_transcript(call_sid, agent_said, patient_reply)

    response = VoiceResponse()

    if "goodbye" in patient_reply.lower() or "bye" in patient_reply.lower():
        response.say(patient_reply, voice="alice")
        response.hangup()
    else:
        gather = Gather(
            input="speech",
            action=f"{NGROK_URL}/respond",
            method="POST",
            timeout=10,
            speech_timeout="5",
            language="en-US"
        )
        gather.say(patient_reply, voice="alice")
        response.append(gather)

    return str(response), 200, {"Content-Type": "text/xml"}


def save_transcript(call_sid, agent_said, patient_said):
    os.makedirs("recordings", exist_ok=True)
    filename = f"recordings/transcript-{call_sid}.txt"
    with open(filename, "a") as f:
        f.write(f"AGENT: {agent_said}\n")
        f.write(f"PATIENT: {patient_said}\n\n")


@app.route("/recording", methods=["GET", "POST"])
def recording():
    recording_url = request.values.get("RecordingUrl")
    call_sid = request.values.get("CallSid")
    print(f"Recording available: {recording_url}")

    import time
    time.sleep(2)
    audio = req.get(f"{recording_url}.mp3", auth=(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN))
    os.makedirs("recordings", exist_ok=True)
    filename = f"recordings/call-{call_sid}.mp3"
    with open(filename, "wb") as f:
        f.write(audio.content)
    print(f"Recording saved: {filename}")
    return "OK", 200


@app.route("/status", methods=["GET", "POST"])
def status():
    print(f"Call status: {request.values.get('CallStatus')} | SID: {request.values.get('CallSid')}")
    return "OK", 200


def make_call(scenario_index=0):
    global current_scenario_index
    current_scenario_index = scenario_index
    call = twilio_client.calls.create(
        to=TEST_NUMBER,
        from_=TWILIO_PHONE_NUMBER,
        url=f"{NGROK_URL}/answer",
        status_callback=f"{NGROK_URL}/status",
        status_callback_method="POST",
        record=True,
        recording_status_callback=f"{NGROK_URL}/recording"
    )
    print(f"Call started: {call.sid}")
    return call.sid


class VoiceBot:
    def __init__(self):
        self.client = twilio_client

    def make_call(self, scenario):
        call = twilio_client.calls.create(
            to=TEST_NUMBER,
            from_=TWILIO_PHONE_NUMBER,
            url=f"{NGROK_URL}/answer",
            status_callback=f"{NGROK_URL}/status",
            status_callback_method="POST",
            record=True,
            recording_status_callback=f"{NGROK_URL}/recording"
        )
        active_scenarios[call.sid] = scenario
        print(f"Call started: {call.sid}")
        return call.sid

    def save_conversation_log(self, call_id, log):
        os.makedirs("recordings", exist_ok=True)
        filename = f"recordings/log-{call_id}.json"
        with open(filename, "w") as f:
            json.dump(log, f, indent=2)
        print(f"Log saved: {filename}")


if __name__ == "__main__":
    print("Starting Twilio Voice Bot server...")
    print(f"Webhook URL: {NGROK_URL}/answer")
    app.run(port=5000, debug=True)