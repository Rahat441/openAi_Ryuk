import requests

api_key = "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"
# "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"
url = "https://api.openai.com/v1/models"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",  # Include if needed
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("It works")
else:
    print("No")

print(f"Status Code: {response.status_code}")
# print("Headers:")
# print(response.headers)
# print("Response Body:")
# print(response.text)
