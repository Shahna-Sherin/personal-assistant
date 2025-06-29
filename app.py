import datetime
import requests
import gradio as gr

def get_weather():
    latitude = 9.9312
    longitude = 76.2673
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    try:
        response = requests.get(url)
        data = response.json()
        weather = data['current_weather']
        return f"🌤 Temp: {weather['temperature']}°C\n💨 Wind: {weather['windspeed']} km/h"
    except:
        return "❌ Weather unavailable."

def ai_assistant(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return "👋 Hello! I'm your assistant."
    elif "time" in user_input or "date" in user_input:
        now = datetime.datetime.now()
        return f"⏰ {now.strftime('%Y-%m-%d %H:%M:%S')}"
    elif "weather" in user_input:
        return get_weather()
    elif "your name" in user_input:
        return "🤖 I'm your Personal AI Assistant!"
    else:
        return "I didn't understand that. Try asking time, weather, or say hi."

gr.Interface(
    fn=ai_assistant,
    inputs=gr.Textbox(label="Ask something..."),
    outputs=gr.Text(label="Assistant Response"),
    title="🧠 Personal Assistant Web App",
    description="Ask me about time, weather, or just say hello!"
).launch()
