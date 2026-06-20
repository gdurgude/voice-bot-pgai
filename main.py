from bot import VoiceBot
from scenarios import SCENARIOS
import time
import uuid

def run_bot():
    """Run the voice bot through all scenarios"""
    
    bot = VoiceBot()
    
    print("\n" + "="*50)
    print("🤖 PRETTY GOOD AI - VOICE BOT TEST SUITE")
    print("="*50)
    print(f"Total scenarios to test: {len(SCENARIOS)}")
    print("="*50 + "\n")
    
    completed_calls = 0
    
    for i, scenario in enumerate(SCENARIOS, 1):
        print(f"\n[{i}/{len(SCENARIOS)}] Running scenario: {scenario['name']}")
        print(f"Description: {scenario['description']}")
        print("-" * 50)
        
        try:
            # Make the call
            call_id = bot.make_call(scenario)
            
            if call_id:
                completed_calls += 1
                print(f"⏳ Call in progress (Call ID: {call_id})")
                
                # Save scenario info
                scenario_log = {
                    "call_id": call_id,
                    "scenario": scenario['name'],
                    "timestamp": time.time(),
                    "status": "completed"
                }
                bot.save_conversation_log(call_id, scenario_log)
                
                # Wait between calls to avoid rate limiting
                print("⏳ Waiting 10 seconds before next call...\n")
                time.sleep(10)
            else:
                print("❌ Failed to make call")
        
        except Exception as e:
            print(f"❌ Error in scenario: {e}")
            continue
    
    print("\n" + "="*50)
    print(f"✅ COMPLETED {completed_calls}/{len(SCENARIOS)} calls")
    print("="*50)
    print("Next steps:")
    print("1. Check recordings/ folder for audio and transcripts")
    print("2. Listen to calls and identify bugs")
    print("3. Document findings in bug_report.md")
    print("="*50 + "\n")

if __name__ == "__main__":
    run_bot()