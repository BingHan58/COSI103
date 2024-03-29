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

        # created by Tianling Hou
    def get_tech_chef_challenge(self, text):
        ''' Generate a GPT response with a given prompt '''
        prompt = "If software development was a cooking show, what kind of ingredients would each programming language bring to the table? For each language, describe a food ingredient that represents its characteristics; Bonus points for including cooking techniques and a celebrity chef host."
        full_prompt = prompt + text
        return self.getResponse(full_prompt)

      # created by Bing Han
    def getPoem(self, text):  
        ''' Generate a GPT response with a given prompt '''
        prompt = "Write a poem about coding. I want the audience to know that I love coding and my favorite programming language is: "
        full_prompt = prompt + text
        return self.getResponse(full_prompt)

        # created by Feifan He
    def get_leetcode_questions(self, text):
        '''Randomly choose desired number of LeetCode questions for practice.'''
        prompt = "Give me some LeetCode questions for practice today, and the number of questions I will do today is: "
        full_prompt = prompt + text
        return self.getResponse(full_prompt)

      #created by Yingshan Hu
    def getJoke(self, text):
        ''' Generate a GPT response for a joke about a given topic/prompt '''
        prompt = "Tell me a joke about the given topic"
        full_prompt = prompt + text
        return self.getResponse(full_prompt)

if __name__=='__main__':
    '''// run bash secret.sh 'python3 gpt.py'
    '''
    import os
    g = GPT(os.environ.get("APIKEY"))
    # print(g.getResponse("what does openai's GPT stand for?"))

     # the prompt for get_refactor()
    code = '''def my_function():
    print("This function has more than 5 lines of code.")
    print("This is another line of code.")
    print("And another one.")
    print("And another one.")
    print("And another one.")
    print("And yet another one.")'''
    # response = g.get_refactor(code)
    # print(response)
    
    text = "Requirements: Choose 2 programming languages; For each language, describe a food ingredient that represents its characteristics; Bonus points for including cooking techniques and a celebrity chef host"
    text1 = "give an output as examples"
    text_leetcode = "5"
    text_joke = "give one input and output as an example"
    # the prompt for get_tech_chef_challenge()
    response = g.get_tech_chef_challenge(text)
    # the prompt for getPoem()
    response_poem = g.getPoem(text1)
    # the prompt for get_leetcode_questions()
    response_leetcode = g.get_leetcode_questions(text_leetcode)
    # the prompt for getJoke()
    response_joke =g.getJoke(text_joke)

    print("\nString response:\n")
    print(response)

    print("\nPoem response:\n")
    print(response_poem)

    print("\nLeetCode response:\n")
    print(response_leetcode)
    
    print("\nJoke response:\n")
    print(response_joke)
