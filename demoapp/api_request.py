import requests

def get_work_list(Token):
    url = 'http://127.0.0.1:8000/api/works/'
    headers = {
        'Authorization': 'Token {Token}'
    }

    response = requests.get(url, headers=headers)
    print(response)
    if response.status_code == 200:
        return response.json()  # This will be a list of works
    else:
        return None  # Handle the error case


