import requests,random

request = "https://api.chucknorris.io/jokes/random"

try:
    response = requests.get(request)
    if response.status_code==200:
        json_response = response.json()
        joke_text= json_response.get("value")
        print(joke_text)


except requests.exceptions.RequestException as e:
    print ("0-0,Sorry :(.The request could not be completed at this time.")
    print (e)