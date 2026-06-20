from flask import Flask, request
from bot import VoiceBot
import os

app = Flask(__name__)
bot = VoiceBot()

@app.route("/incoming-call", methods=["POST"])
def incoming_call():
    """Handle incoming calls"""
    call_sid = request.values.get("CallSid")
    from_number = request.values.get("From")
    to_number = request.values.get("To")
    
    print(f"\n📞 Incoming call: {from_number} to {to_number}")
    
    twiml = bot.handle_incoming_call(call_sid, from_number, to_number)
    return twiml

@app.route("/handle-speech", methods=["POST"])
def handle_speech():
    """Handle speech recognition results"""
    call_sid = request.args.get("call_sid")
    speech_result = request.values.get("SpeechResult")
    
    print(f"🎤 User said: {speech_result}")
    
    twiml = bot.handle_incoming_call(call_sid, None, None, speech_result)
    return twiml

if __name__ == "__main__":
    app.run(debug=True, port=5000)