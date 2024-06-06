import requests
from bs4 import BeautifulSoup

description = 'Getting Information about current weather in hamilton, new zealand'


def data_extract():
    """
        Time:
        Temp:
        Location:
        Rain:
        Wind:
        Humidex:
        Humidity:
        Pressure:
        :return:
        """

    # catch error
    try:
        r = requests.get('https://www.weatherwatch.co.nz/forecasts/Hamilton')
    except Exception as e:
        print(e)
        return None

    if r.status_code == 200:
        # create BeautifulSoup object to parsing html tag
        soup = BeautifulSoup(r.text, 'html.parser')

        parent = soup.find('div', {'class': 'jsx-3204536004 current-conditions grid-item grid-width-4'})

        result_header = parent.findChild('h4')
        header = result_header.text

        result_temp = parent.find('div', {'class': 'jsx-3024714417 temp'})
        temp = result_temp.text

        result_location = parent.find('div', {'class': 'jsx-3024714417 location'})
        location = result_location.text

        result_observe = parent.find('div', {'class': 'jsx-3024714417 summary'})
        observe = result_observe.text

        new_parent = parent.find('div', {'class': 'jsx-3024714417 details grid-item grid-width-2'})
        children = new_parent.findChildren('span')

        rain = children[0].text
        wind = children[1].text
        humidex = children[2].text
        humidity = children[3].text
        pressure = children[4].text

        data_result = {
            'time': header,
            'temp': temp,
            'location': location,
            'observe': observe,
            'rain': rain,
            'wind': wind,
            'humidex': humidex,
            'humidity': humidity,
            'pressure': pressure,
        }

        return data_result

    else:
        return None


def show_data(data_result):
    if data_result is None:
        print('Data not found')
        return
    else:
        for res in data_result:
            print(f'{res}: {data_result[res]}')


if __name__ == '__main__':
    print('main app')
    print(f'description: {description}')

    result = data_extract()
    show_data(result)
