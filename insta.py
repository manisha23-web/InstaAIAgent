import os
import time

# --- SETUP ---

os.environ["OPENROUTER_API_KEY"] = "YOUR_API_KEY_HERE"

# DroidRun Base Command
BASE_CMD = 'droidrun "{}" --provider OpenRouter --model google/gemini-2.0-flash-exp:free'

def ask_droid(prompt):
    print(f"\n🤖 AI Action: {prompt}")
    os.system(BASE_CMD.format(prompt))

def smart_sleep(seconds):
    print(f"⏳ Loading UI ({seconds}s)...")
    time.sleep(seconds)

def main():
    print("🚀 --- INSTAGRAM HACKATHON AGENT (V2) ---")
    
    
    group_name = input("ENTER Group Name: ")
    try:
        reel_count = int(input("Number of reels to watch: "))
    except ValueError:
        reel_count = 3
        
    print(f"\n🎯 Target: '{group_name}' | Count: {reel_count} | Mode: Recent Shared")
    
    
    ask_droid("Open Instagram app")
    smart_sleep(5)
    

    print("📍 Navigating to Messages (Bottom Center)...")
    ask_droid("Tap on the Message icon located at the bottom center of the screen")
    smart_sleep(4)
    
    
    ask_droid("Tap on the Search bar at the top")
    smart_sleep(2)
    ask_droid(f"Type '{group_name}' and tap the first result")
    smart_sleep(5)
    
    print("🔍 Finding the MOST RECENT shared reel...")
    
    
    ask_droid("Scroll down to the very bottom of the chat to see the latest messages")
    smart_sleep(2)
    
    
    ask_droid("Tap on the most recently shared Reel thumbnail/link in this chat to open it full screen")
    smart_sleep(6) 
    
   
    for i in range(1, reel_count + 1):
        print(f"\n🎬 Watching Reel #{i}...")
    
        
        reaction_prompt = (
            "Check the reel. "
            "If it is funny or interesting, double tap center to Like. "
            "Otherwise do nothing."
        )
        ask_droid(reaction_prompt)
        smart_sleep(3) # Watch time
        
        
        print("⚡ Next Reel...")
        os.system("adb shell input swipe 500 1600 500 400 100")
        smart_sleep(2)

        


def smart_sleep(seconds):

    adjusted_time = seconds + 5 
    print(f"⏳ Waiting {adjusted_time}s (to avoid Rate Limit)...")
    time.sleep(adjusted_time)

    print("\n✅ Task Completed Successfully.")

if __name__ == "__main__":
    main()
