import openai

def generate_response(prompt, tone):
    if tone == 'neutral':
        prefix = "You are a software engineer responding in a work setting, please respond to the following conversation chain in a business professional tone:"
    elif tone == 'affirming':
        prefix = "Two friends are talking about life/making plans/cracking jokes, please respond in a natural human way in the conversation chain:"
    elif tone == 'affirming_funny':
        prefix = "Two friends are having a playful conversation, please respond in a lighthearted and humorous tone:"
    elif tone == 'disagreeing':
        prefix = "You are a manager in a business meeting, and you respectfully disagree with the previous speaker. Please provide an alternative perspective and suggest a potential solution in a professional tone:"
    elif tone == "informative":
        prefix = "You are writing an informative article, please respond in a factual and informative tone: "
    elif tone == "persuasive":
        prefix = "You are trying to persuade someone to your point of view, please respond in a persuasive and convincing tone: "
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
    return response.choices[0].text


print(generate_response("When are you leaving to the party Chuck?", "informative"))