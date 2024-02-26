import requests

def get_current_weather(city):
    try:
        api_key = "57e7f4bd73b842fea74103246240802"
        url=f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
        response = requests.get(url)
        data = response.json()
    except :
        print("rong api key")
    

    print("temrature is :",data["current"]["temp_f"])
    print(data["current"]["temp_c"])

    print("error")

if __name__ == "__main__":
    pass
    
    # city = input("Enter city name: ")
    # get_current_weather( city)
