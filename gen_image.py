import requests
import together

url = "https://api.together.xyz/inference"

payload = {
    "model": "togethercomputer/togethercomputer/RedPajama-INCITE-7B-Chat",
    "prompt": "Correct this to standard English:\nI no Sandwich want.",
    "max_tokens": 256,
    "stop": ".",
    "temperature": 0.1,
    "top_p": 0.7,
    "top_k": 50,
    "repetition_penalty": 1
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "Authorization": "Bearer <780f8e5708ef56deb90e56df8f8527562624089aee1b700fe9ce653f93e12a71>",
  	"User-Agent": "<YOUR_APP_NAME>",
}    

response = requests.post(url, json=payload, headers=headers)

print(response.text)
