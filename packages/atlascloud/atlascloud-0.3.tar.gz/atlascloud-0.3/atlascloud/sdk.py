import openai
import requests
import json

class atlascloud:
        
    def __init__(self, api_key='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'):
            
        self.openai = openai
        self.requests = requests
        self.json = json
        self.openai.api_key = api_key
        
    def generate(self, prompt):

        try:

            self.completion = self.openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    },
                ],
            )
            self.output = self.completion.choices[0].message.content
            
        except Exception as e:
            return False, "Error: " + str(e)

        return self.output
    
    def generate_openrouter(self, prompt, api_key = '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'):

        self.response = self.requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}"
        },
        data=self.json.dumps({
            "model": "meta-llama/llama-3-70b", # Optional
            "messages": [
            { "role": "user", "content": prompt }
            ]
        })
        )
        
        return self.response
        
    
if __name__ == "__main__":
    at = atlascloud()
    print(at.generate_openrouter('introduce cuda'))