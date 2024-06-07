import openai

class atlascloud:
        
    def __init__(self):
            
        self.openai = openai
        self.openai.api_key = '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'
        
    def generate(self, prompt):

        try:

            self.completion = openai.chat.completions.create(
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
    
if __name__ == "__main__":
    at = atlascloud()
    print(at.generate('hi'))