from .koho import fetch_data

def hello():
    print("Hello, World!")

def koho(id, token):
    try:
        data = fetch_data(id, token)
        print(data)
    except Exception as e:
        print(f"An error occurred: {e}")