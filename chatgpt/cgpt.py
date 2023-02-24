
import openai
import os
os.environ['OPENAI_Key']="YOUR_API"
openai.api_key=os.environ['OPENAI_Key']

keep_prompting=True
while keep_prompting:
    prompt=input('Ask the question : exit when you done ')
    if prompt=='exit':
        keep_prompting=False
    else:
        response=openai.Completion.create(engine='text-davinci-003',prompt=prompt,max_tokens=200)
        print(response['choices'][0]['text'])

        

