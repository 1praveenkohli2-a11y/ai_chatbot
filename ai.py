from tkinter import *
from google import genai

# API
client = genai.Client(api_key="AIzaSyC9pd5BSbc-N4nWpn74pkLZyBzvvAnj2NI")

# Window
root = Tk()
root.title("AI Chatbot")
root.geometry("500x600")

# Chat area
chat = Text(root, font=("Arial", 12))
chat.pack(padx=10, pady=10, fill=BOTH, expand=True)

# Message box
entry = Entry(root, font=("Arial", 14))
entry.pack(padx=10, pady=10, fill=X)

entry.bind("<Return>",lambda event:send())

# Send function
def send():
    msg = entry.get()

    if msg == "":
        return

    chat.insert(END, "You: " + msg + "\n")

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=msg
    )

    chat.insert(END, "Bot: " + response.text + "\n\n")

    entry.delete(0, END)

# Send button
btn = Button(root, text="Send", command=send)
btn.pack(pady=5)

# Run app
root.mainloop()