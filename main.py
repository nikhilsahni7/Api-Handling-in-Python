import requests

def fetch_results():
    url = "https://v2.jokeapi.dev/joke/Dark?amount=6" 
    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            jokes = data['jokes']
            for joke in jokes:
                if 'setup' in joke:
                    print("Setup: " + joke['setup'] + "\n" + "Delivery: " + joke['delivery'] + "\n")
                elif 'joke' in joke:
                    print("Joke: " + joke['joke'] + "\n")
        else:
            print(f"Error: {response.status_code}")
            print(response.text)  # Print response text for more information
            return None

    except requests.RequestException as e:
        print(f"Request Error: {str(e)}")
        return None

def main():
    fetch_results()

if __name__ == "__main__":
    main()
