import pytesseract
import logging
import pyautogui
import openai
import tkinter as tk

from pynput import keyboard


def screenshot_to_text():
    screenshot = pyautogui.screenshot()
    screenshot.save('./outputs/screenshot.png')
    text = pytesseract.image_to_string(screenshot)
    print("Screenshot to text", text)
    # write text to file
    with open('./outputs/extracted_text.txt', 'w') as f:
        f.write(text)
    return text

def generate_response(prompt, tone):
    if tone == 'neutral':
        prefix = "You are a software engineer responding in a work setting, please respond to the following conversation chain in a business professional tone:"
    elif tone == 'affirming':
        prefix = "Two friends are talking about life/making plans/cracking jokes, please respond in a natural, light human way in the conversation chain:"
    elif tone == 'disagreeing':
        prefix = "You are a manager in a business meeting, and you respectfully disagree with the previous speaker. Please provide an alternative perspective and suggest a potential solution in a professional tone:"
    elif tone == "informative":
        prefix = "You are writing an informative article, please respond in a factual and informative tone: "
    else:
        raise ValueError("Invalid tone. Choose one of: neutral, affirming, affirming_funny, disagreeing")
        
    prompt = prefix + '\n\n' + prompt + '\n\n'

    # Use the OpenAI GPT-3 API to generate a response based on the prompt and tone
    response = openai.Completion.create(
        prompt=prompt,
        temperature=0.5,
        max_tokens=50,
        n=1,
        stop=None,
        presence_penalty=0,
        frequency_penalty=0,
        model="text-davinci-002",
    )
    print("Response text", response.choices[0].text)
    return response.choices[0].text


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


def on_press(key):
    try:
        if key == keyboard.Key.shift:
            # Store the previous key if it was also a tab
            if hasattr(on_press, "prev_key") and on_press.prev_key == keyboard.Key.shift:
                print("User invoked autocomplete with 'tab tab'")
                # Convert the screenshot to text using OCR
                ocr_text = screenshot_to_text()
                # Generate 4 canned responses using OpenAI completion in an affirming tone, affirming funny tone, negating tone, and neutral tone.
                response_types = ["affirming", "disagreeing"]
                responses = [generate_response(ocr_text, response_type) for response_type in response_types]
                # Provide a simple interface for the user to select one of the four responses.
                display_response(responses)
        on_press.prev_key = key
    except AttributeError:
        print("ERROR")
        pass

def on_release(key):
    pass

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
