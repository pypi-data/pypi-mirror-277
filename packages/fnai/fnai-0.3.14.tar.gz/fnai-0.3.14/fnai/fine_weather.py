import requests

class FineWeather:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.caiyunapp.com/v2.5"

    def get_weather(self, city):
        url = f"{self.base_url}/{self.api_key}/{city}/weather.json"
        response = requests.get(url)
        data = response.json()
        return data

    def display_weather(self, city):
        weather_data = self.get_weather(city)
        if "status" in weather_data and weather_data["status"] == "ok":
            current_weather = weather_data["result"]["realtime"]["weather"]
            temperature = weather_data["result"]["realtime"]["temperature"]
            print(f"当前天气：{current_weather}，温度：{temperature}℃")
        else:
            print("获取天气信息失败")

if __name__ == "__main__":
    api_key = "YOUR_API_KEY"  # 替换为你的彩云天气API密钥
    city = "北京"  # 要查询的城市
    fine_weather = FineWeather(api_key)
    fine_weather.display_weather(city)
