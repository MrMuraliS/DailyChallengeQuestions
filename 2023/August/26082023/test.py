import requests
from bs4 import BeautifulSoup


def fetch_weather_data(location):
    base_url = f"https://www.weather.com/en-IN/weather/today/l/{location}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    response = requests.get(base_url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    weather = soup.find("div", class_="today_nowcard-phrase").get_text()
    temperature = soup.find("div", class_="today_nowcard-temp").get_text()

    return {"weather": weather, "temperature": temperature}


def display_weather(data):
    print(f"Weather: {data['weather']}")
    print(f"Temperature: {data['temperature']}")


if __name__ == "__main__":
    location = input("Enter location or city name: ").replace(" ", "-").lower()
    weather_data = fetch_weather_data(location)
    display_weather(weather_data)
