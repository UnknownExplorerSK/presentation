import openai
import time

var = input("Please enter your api key: ")
openai.api_key = var

# prompt1 = "Write a random greeting"

completion = openai.Completion.create(engine="ada", prompt="Write a random greeting")

# print the completion
print(completion.choices[0].text)
# response = openai.Completion.create(
#      engine="text-davinci-001", 
#      prompt=prompt1, 
#      max_tokens=12)

# print(response.choices[0].text)

# prompt2 = str("Translate this into French ") + str(response)
# print(prompt2)

# time.sleep(1)

# response2 = openai.Completion.create(
#     engine="text-davinci-001", 
#     prompt=prompt2,
#     max_tokens=6
# )

# print(response2)
