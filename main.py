from weatherapp import WeatherApp


class Main:

    def call_weather_app(self):

        end_point = "http://localhost:8080/addvans"
        weather_app = WeatherApp(end_point)
        print(weather_app.api_call_vans())


if __name__ == '__main__':
    main = Main()
    main.call_weather_app()



