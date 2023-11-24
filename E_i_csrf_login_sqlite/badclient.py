# mauvais_client.py
import requests

def get_users():
    response = requests.get("http://localhost:5000/users")
    return response.json()

def main():
    result = get_users()
    print(result)

if __name__ == "__main__":
    main()
