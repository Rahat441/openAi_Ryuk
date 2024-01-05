# OpenAiRyuk

Simple script to use ChatGPT on your own files.

Here's the [YouTube Video](https://youtu.be/9AXP7tCI9PI).

## Installation
``install dependencies as needed
Install [Langchain](https://github.com/hwchase17/langchain) and other required packages.
```
pip install langchain openai chromadb tiktoken unstructured
```
Modify `constants.py.default` to use your own [OpenAI API key](https://platform.openai.com/account/api-keys), and rename it to `constants.py`.

Place your own data into `data/data.txt`.

## Example usage
Test reading `data/data.txt` file.
```
  $ python chatgpt.py "what is my dog's name"
Your dog's name is Sunny.
```
## Running Script
Activate Env
conda activate new_gptenv

## Run flask for UI
 $ python app.py
## Without UI
  ``Look at example ussage 
## to expose Server 
  ``install dependencies as needed
  $ ngrok http 5000
# openAi_Ryuk
