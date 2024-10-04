import openai
from openai import OpenAI

openai.api_key = '' # placeholder
client = OpenAI(api_key=openai.api_key)

def createGenericContract(api_specification: str, api_type: str):    
    query = f"You are a helpful assistant and an expert in RESTful API Design and RAML. Given this uploaded {api_type} file, you will parse it into metadata, base URL, consumes, produces, paths, parameters, responses, input and output models, and authentication. You will always respond in JSON."

    response = client.chat.completions.create (
            model="gpt-4o-mini",
            messages=[{"role": "system", "content": query}]
        )
    return response


def createGenericCode(code: str):
    response = '' # placeholder for code from Manish that generates the parsed code from the original source code file
    return response