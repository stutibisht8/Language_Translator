from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from googletrans import Translator
from gtts import gTTS
from playsound import playsound
from playsound import playsound
import sounddevice as sd
import soundfile as sf
import speech_recognition as sr
import numpy as np
import os

# -------------------- Window --------------------
window = Tk()
window.title("Language Translator")
window.geometry("750x550")
voice_file = "voice.mp3"

# -------------------- Background --------------------
try:
    bg = PhotoImage(file="background.png")
    bg_label = Label(window, image=bg)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
except:
    window.config(bg="black")

# -------------------- Heading --------------------
heading = Label(
    window,
    text="🌍 Language Translator",
    font=("Arial",22,"bold"),
    bg="black",
    fg="white"
)
heading.pack(pady=10)

# -------------------- Text Input --------------------
Label(
    window,
    text="Enter Text",
    bg="black",
    fg="white",
    font=("Arial",12,"bold")
).pack()

e1 = Text(
    window,
    width=50,
    height=6,
    font=("Arial",14)
)

e1.pack(pady=10)

# -------------------- Languages --------------------
languages = {
    "English":"en",
    "Hindi":"hi",
    "Spanish":"es",
    "French":"fr",
    "German":"de",
    "Italian":"it",
    "Japanese":"ja",
    "Chinese":"zh-cn",
    "Arabic":"ar",
    "Russian":"ru"
}

selected_language = StringVar()
selected_language.set("Select Language")

drop = OptionMenu(window, selected_language, *languages.keys())
drop.config(font=("Arial",12), width=20)
drop.pack()

translator = Translator()

# -------------------- Status --------------------
status = Label(
    window,
    text="Status: Ready",
    bg="black",
    fg="yellow",
    anchor="w",
    font=("Arial",16)
)

# -------------------- Voice Input --------------------
def voice_input():
    try:
        status.config(text="Listening...")
        window.update()
        duration = 5      # Record for 5 seconds
        fs = 16000        # Sample rate
        audio = sd.rec(
            int(duration * fs),
            samplerate=fs,
            channels=1,
            dtype='int16'
        )
        sd.wait()
        sf.write("voice_input.wav", audio, fs)
        recognizer = sr.Recognizer()
        with sr.AudioFile("voice_input.wav") as source:
            audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)
        e1.delete("1.0", END)
        e1.insert(END, text)
        status.config(text="Voice Captured Successfully")
        os.remove("voice_input.wav")
    except Exception as e:
        messagebox.showerror("Voice Error", str(e))
        status.config(text="Ready")

# -------------------- Translate --------------------
def convert_language():

    text = e1.get("1.0", END).strip()

    if text == "":
        messagebox.showwarning("Warning","Please Enter Text")
        return

    if selected_language.get() == "Select Language":
        messagebox.showwarning("Warning","Please Select Language")
        return

    code = languages[selected_language.get()]

    try:

        status.config(text="Detecting Language...")
        window.update()

        detected = translator.detect(text)

        status.config(
            text=f"Detected : {detected.lang.upper()} | Translating..."
        )

        result = translator.translate(
            text,
            src=detected.lang,
            dest=code
        )

        translated = result.text

        label_2.config(text=translated)

        if os.path.exists(voice_file):
            os.remove(voice_file)

        tts = gTTS(
            text=translated,
            lang=code,
            slow=False
        )

        tts.save(voice_file)

        status.config(
            text=f"Completed | Source : {detected.lang.upper()}"
        )

    except Exception as e:

        print(e)

        messagebox.showerror(
            "Error",
            "Translation Failed"
        )

        status.config(text="Error")

# -------------------- Listen --------------------
def listen():

    if os.path.exists(voice_file):

        playsound(voice_file)

    else:

        messagebox.showinfo(
            "Info",
            "Translate text first."
        )

# -------------------- Clear --------------------
def clear():

    e1.delete("1.0", END)

    label_2.config(
        text="Translation will appear here"
    )

    selected_language.set(
        "Select Language"
    )

    status.config(text="Ready")

    if os.path.exists(voice_file):

        os.remove(voice_file)

# -------------------- Copy Text --------------------
def copy_text():

    translated = label_2.cget("text")

    if translated == "Translation will appear here":
        messagebox.showwarning("Warning", "Nothing to Copy")
        return

    window.clipboard_clear()
    window.clipboard_append(translated)
    window.update()

    status.config(text="Translation Copied")

# -------------------- Swap Language --------------------
def swap_language():

    input_text = e1.get("1.0", END).strip()

    translated = label_2.cget("text")

    if translated == "Translation will appear here":
        return

    e1.delete("1.0", END)
    e1.insert("1.0", translated)

    label_2.config(text=input_text)

    status.config(text="Languages Swapped")

# -------------------- Share Translation --------------------
def share_translation():

    translated = label_2.cget("text")

    if translated == "Translation will appear here":
        messagebox.showwarning("Warning", "Nothing to Save")
        return

    file = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text File","*.txt")]
    )

    if file:

        with open(file,"w",encoding="utf-8") as f:
            f.write(translated)

        status.config(text="Translation Saved")

# -------------------- Buttons --------------------
frame = Frame(window,bg="black")
frame.pack(pady=15)
Button(
    frame,
    text="Translate",
    bg="red",
    fg="white",
    width=12,
    font=("Arial",12,"bold"),
    command=convert_language
).pack(side=LEFT,padx=5)

Button(
    frame,
    text="🎤 Voice",
    bg="purple",
    fg="white",
    width=12,
    font=("Arial",12,"bold"),
    command=voice_input
).pack(side=LEFT,padx=5)

Button(
    frame,
    text="🔊 Listen",
    bg="blue",
    fg="white",
    width=12,
    font=("Arial",12,"bold"),
    command=listen
).pack(side=LEFT,padx=5)

Button(
    frame,
    text="📋 Copy",
    bg="#ff9800",
    fg="white",
    width=12,
    font=("Arial",12,"bold"),
    command=copy_text
).pack(side=LEFT,padx=5)

Button(
    frame,
    text="🔄 Swap",
    bg="#9c27b0",
    fg="white",
    width=12,
    font=("Arial",12,"bold"),
    command=swap_language
).pack(side=LEFT,padx=5)

Button(
    frame,
    text="📤 Share",
    bg="#009688",
    fg="white",
    width=12,
    font=("Arial",12,"bold"),
    command=share_translation
).pack(side=LEFT,padx=5)

Button(
    frame,
    text="Clear",
    bg="green",
    fg="white",
    width=12,
    font=("Arial",12,"bold"),
    command=clear
).pack(side=LEFT,padx=5)

status.pack(pady=(10,8))

Label(
    window,
    text="Translated Text",
    bg="black",
    fg="white",
    font=("Arial", 16, "bold")
).pack(pady=(15,5))

# -------------------- Output --------------------
label_2 = Label(
    window,
    text="Translation will appear here",
    bg="black",
    fg="white",
    wraplength=800,
    justify="center",
    font=("Arial",22,"bold")
)
label_2.pack(pady=20)

footer = Label(
    window,
    text="© 2026 | Made with using Python ❤️",
    font=("Arial",14,"italic"),
    bg="black",
    fg="white"
)
footer.pack(side=BOTTOM)
# -------------------- Run --------------------
window.mainloop()

