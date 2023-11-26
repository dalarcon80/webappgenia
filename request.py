import requests

# master
# api_key = "U30v1c5GOju3Yj2BXrvz2hYUgz-xx5S9mnNWsLHxVqCEAzFuOlxwxA=="

# default
api_key = "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"

url = f'https://func-llm-ecp-sbx.azurewebsites.net/api/HttpTrigger1_API?code={api_key}'


while True:
    query = input("\nPrompt: ")

    payload = {
        'query': query + ". Responde en español y especifica el source."
    }

    print("\nCargando respuesta ...  \n")

    # Conexión a API de Azure Function
    response = requests.post(url, json=payload)
      
    if response.status_code == 200:
        data = response.json()
        print('Respuesta:', data['response'])
        # print(response.text)
    else:
        print('Error:', response.text)