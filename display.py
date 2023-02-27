import tkinter as tk
import pyperclip

def display_response(responses):
    window = tk.Tk()
    window.title("OpenAI Response")
    window.geometry("800x400")

    for i, response in enumerate(responses):
        response_label = tk.Label(window, text=f"Response {i+1}: {response}", font=("Arial", 12), wraplength=600, justify='left')
        response_label.grid(row=i+1, column=0, padx=10, pady=10)

        copy_button = tk.Button(window, text="Copy", font=("Arial", 12), command=lambda response=response: pyperclip.copy(response))
        copy_button.grid(row=i+1, column=1, padx=10, pady=10)

    close_button = tk.Button(window, text="Close", font=("Arial", 12), command=window.destroy)
    close_button.grid(row=len(responses)+1, column=0, padx=0, pady=10)
    window.mainloop()

responses = [
    "I'm sorry, I can't make it to the party tonight.",
    "I'm leaving in 30 minutes, see you there!",
    "I'm not sure yet, I need to check my schedule.",
    "I decided not to go to the party, thanks for the invite though!"
]

display_response(responses)