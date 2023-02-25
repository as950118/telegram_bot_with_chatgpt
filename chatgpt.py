import openai
import argparse

YOUR_API_KEY = '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'

def chatGPT(prompt, API_KEY=YOUR_API_KEY):

    # set api key
    openai.api_key = API_KEY

    # Call ChatGPT API
    completion = openai.Completion.create(
        model = "text-davinci-003",
        prompt = prompt,
        temperature = 0.5,
        max_tokens = 2**10,
        top_p = 1,
        frequency_penalty = 0,
        presence_penalty = 0
        )
    ret = completion['choices'][0]['text']
    return ret

if __name__ == "__main__":
    prompt = input("사용자 : ")
    completion = chatGPT(prompt).strip()
    print(f"ChatGPT : {completion}")




    
