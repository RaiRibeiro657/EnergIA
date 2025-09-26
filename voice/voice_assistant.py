import speech_recognition as sr
import pyttsx3
import requests

API_URL = "http://127.0.0.1:5000"  

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("🎤 Diga um comando...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio, language="pt-BR")
        print(f"Você disse: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Desculpe, não entendi.")
        return None
    except sr.RequestError:
        speak("Erro no serviço de reconhecimento de voz.")
        return None

def process_command(command):
    if "status" in command:
        response = requests.get(f"{API_URL}/status").json()
        speak(f"Bateria em {response['battery_level']} porcento. "
              f"Carga crítica está {'ligada' if response['carga_critica'] else 'desligada'}. "
              f"Carga secundária está {'ligada' if response['carga_secundaria'] else 'desligada'}.")
    
    elif "desligar carga secundária" in command:
        response = requests.post(f"{API_URL}/update", json={"carga_secundaria": False}).json()
        speak("Carga secundária desligada.")
    
    elif "ligar carga secundária" in command:
        response = requests.post(f"{API_URL}/update", json={"carga_secundaria": True}).json()
        speak("Carga secundária ligada.")
    
    elif "desligar carga crítica" in command:
        response = requests.post(f"{API_URL}/update", json={"carga_critica": False}).json()
        speak("Carga crítica desligada.")
    
    elif "ligar carga crítica" in command:
        response = requests.post(f"{API_URL}/update", json={"carga_critica": True}).json()
        speak("Carga crítica ligada.")
    
    else:
        speak("Comando não reconhecido.")

def main():
    speak("Assistente de energia iniciado.")
    while True:
        command = listen()
        if command:
            if "sair" in command or "parar" in command:
                speak("Encerrando o assistente.")
                break
            process_command(command)

if __name__ == "__main__":
    main()