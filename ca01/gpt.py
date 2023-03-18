'''
Demo code for interacting with GPT-3 in Python.

To run this you need to 
* first visit openai.com and get an APIkey, 
* which you export into the environment as shown in the shell code below.
* next create a folder and put this file in the folder as gpt.py
* finally run the following commands in that folder

On Mac
% pip3 install openai
% export APIKEY="......."  # in bash
% python3 gpt.py

On Windows:
% pip install openai
% $env:APIKEY="....." # in powershell
% python gpt.py
'''
import openai


class GPT():
    ''' make queries to gpt from a given API '''
    def __init__(self,apikey):
        ''' store the apikey in an instance variable '''
        self.apikey=apikey
        # Set up the OpenAI API client
        openai.api_key = apikey

        # Set up the model and prompt
        self.model_engine = "text-davinci-003"

    def getResponse(self,prompt):
        ''' Generate a GPT response '''
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.8,
        )

        response = completion.choices[0].text
        return response
    
    def get_refactor(self, code):
        ''' Generate a GPT response for code refactoring '''
        prompt = "Refactor the following Python program so that all functions have fewer than 5 lines of code:\n\n" + code
        return self.getResponse(prompt)

if __name__=='__main__':
    '''// run bash secret.sh 'python3 gpt.py'
    '''
    import os
    g = GPT(os.environ.get("APIKEY"))
    # print(g.getResponse("what does openai's GPT stand for?"))
    code = '''def my_function():
    print("This function has more than 5 lines of code.")
    print("This is another line of code.")
    print("And another one.")
    print("And another one.")
    print("And another one.")
    print("And yet another one.")'''
    response = g.get_refactor(code)
    print(response)

