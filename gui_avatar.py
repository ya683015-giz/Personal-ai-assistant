import tkinter as tk
import cv2
from PIL import Image, ImageTk
import pyttsx3
import speech_recognition as sr

# ---------- Voice ----------
engine = pyttsx3.init()
engine.setProperty("rate", 150)

def speak(text):
    engine.say(text)
    engine.runAndWait()

# ---------- Listen ----------
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        chat.insert(tk.END, "🎤 Listening...\n")
        root.update()
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language="en-IN")
        chat.insert(tk.END, "You: " + text + "\n")
        reply = "Hello, how are you and how was you day."
        chat.insert(tk.END, "AI: " + reply + "\n\n")
        speak(reply)
    except:
        chat.insert(tk.END, "❌ Not Understand\n\n")

# ---------- GUI ----------
root = tk.Tk()
root.title("Anime AI Assistant")
root.geometry("500x700")

video_label = tk.Label(root)
video_label.pack()

chat = tk.Text(root, height=10)
chat.pack()

tk.Button(root, text="🎙 Speak", command=listen).pack(pady=10)

# ---------- Video Play ----------
cap = cv2.VideoCapture("avatar.mp4")

def play_video():
    ret, frame = cap.read()
    if not ret:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        ret, frame = cap.read()

    frame = cv2.resize(frame, (480, 360))
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = ImageTk.PhotoImage(Image.fromarray(frame))
    video_label.imgtk = img
    video_label.configure(image=img)
    root.after(30, play_video)

play_video()
root.mainloop()
