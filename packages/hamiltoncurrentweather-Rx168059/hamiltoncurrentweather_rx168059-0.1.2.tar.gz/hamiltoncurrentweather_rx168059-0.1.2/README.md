# Hamilton-Current-Weather
This package will get information about current weather in hamilton from weatherwatch website

## How It Works
This package will scrap data from [weatherwatch](https://www.weatherwatch.co.nz/forecasts/Hamilton) to get information about current weather in hamilton

This package used BeautifulSoup4 and Requests to generate JSON output that'll be used for web or mobile apps

## How to Run
```
import hamiltoncurrentweather as hct

if __name__ == '__main__':
    hamilton_weather = hct.CurrentWeather('https://www.weatherwatch.co.nz/forecasts/Hamilton')
    print('main app')
    print(f'description: {hamilton_weather.description}')
    hamilton_weather.run()
```

# Author
Muhammad Dwi Reza
