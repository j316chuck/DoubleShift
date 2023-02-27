import openai
import re

def filter_conversation(ocr_text):
    # Split the OCR text into individual lines
    lines = ocr_text.split('\n')
    
    # Use a regular expression to find the first line that contains a name and a message
    pattern = re.compile(r"^[A-Za-z ]+[:][\s\S]+$")
    for line in lines:
        if pattern.match(line):
            break
    
    # Remove any lines before the first matched line
    lines = lines[lines.index(line):]
    
    # Use OpenAI's GPT-3 to filter out any irrelevant lines
    filtered_lines = []
    prompt = "Prompt: Filter the following conversation for the most coherent conversation thread.\
        You may need to stitch together separate parts of the text from different regions because this text is generated from an ocr recognition system.\
        Please keep track of who is saying what in the conversation chain and try to derive where the conversation is coming from:\n\n" + '\n'.join(lines)
    response = openai.Completion.create(
        prompt=prompt,
        temperature=0.3,
        max_tokens=100,
        n=1,
        stop=None,
        presence_penalty=0,
        frequency_penalty=0,
        model="text-davinci-002",
    )
    filtered_text = response.choices[0].text
    
    # Return the filtered text
    
    return filtered_text

text = open('extracted_text.txt', 'r').read()
print(filter_conversation(text))
