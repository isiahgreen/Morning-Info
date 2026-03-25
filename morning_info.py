import requests
import random
from datetime import datetime

# --- Weather Setup ---
location = "Atlanta,GA"
url = f"https://wttr.in/{location}?format=j1"

try:
    weather_data = requests.get(url).json()
    celsius = int(weather_data["current_condition"][0]["temp_C"])
    fahrenheit = round((celsius * 9/5) + 32)
    weather_desc = weather_data["current_condition"][0]["weatherDesc"][0]["value"]
except Exception as e:
    fahrenheit = "N/A"
    weather_desc = "Unavailable"
    print(f"Weather fetch failed: {e}")

# --- Daily Quote Setup ---
quotes = [
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "Do something today that your future self will thank you for.",
    "Learning never exhausts the mind.",
    "Stay curious and keep exploring!"
]
daily_quote = random.choice(quotes)

# --- Cybersecurity / Networking Tip Setup ---
tips = [
    "Remember the TCP 3-way handshake.",
    "Always check firewall logs.",
    "Use least privilege access.",
    "Practice ping, tracert, netstat daily."
]
daily_tip = random.choice(tips)

# --- Greeting Setup ---
hour = datetime.now().hour
if hour < 12:
    greeting = "Good morning!"
elif hour < 18:
    greeting = "Good afternoon!"
else:
    greeting = "Good evening!"

# --- Print Everything ---
print(greeting)
print(f"{location}: {fahrenheit}°F, {weather_desc}")
print(f"Quote of the day: {daily_quote}")
print(f"Cyber Tip: {daily_tip}")
print("\nStay productive and keep learning!")

# --- Keep terminal open if run via Task Scheduler ---
input("\nPress Enter to exit...")