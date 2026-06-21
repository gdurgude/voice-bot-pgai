# Pretty Good AI — Voice Bot Challenge

An automated AI voice bot that calls the Pretty Good AI test line, simulates realistic patient scenarios, records conversations, and identifies bugs in the agent's responses.

## Setup

### 1. Install dependencies
```bash
pip install flask twilio anthropic requests
```

### 2. Install and start ngrok
```bash
ngrok http 5000
```
Copy the HTTPS URL — you'll need it for `NGROK_URL` in your `.env`.

### 3. Configure environment variables
Copy `.env.example` to `.env` and fill in your credentials:
```bash
cp .env.example .env
```

### 4. Start the Flask server
```bash
python bot.py
```

### 5. Run all scenarios (in a separate terminal)
```bash
python main.py
```

This will automatically:
- Make 12 calls to the test number
- Record each conversation as an MP3
- Save transcripts to the `recordings/` folder

## Project Structure
```
voice-bot/
├── bot.py          # Flask server + Twilio webhooks + Anthropic AI patient
├── main.py         # Runs all scenarios sequentially
├── scenarios.py    # 12 patient test scenarios
├── config.py       # Credentials (do not commit)
├── .env.example    # Required environment variables
└── recordings/     # Auto-generated transcripts and MP3s
```

## Requirements
- Python 3.8+
- Twilio account (upgraded, not trial)
- Anthropic API key with credits
- ngrok account (free tier works)
