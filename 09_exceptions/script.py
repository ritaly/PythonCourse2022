class WeatherError(Exception):
    '''custom error'''
    pass

def get_weather():
    # pobiera z api infomarcje o pogodzie
    # jeśli dostaniemy błąd
    # -- zwróć własny błąd
    # return pogodę

    weather = input(' -> sun / rain ')

    if weather == 'sun':
        return '🌤'
    elif weather == 'rain':
        return '🌧'
    else:
        raise WeatherError('Unknown weather')

def main():
    print('Hello!')
    print('⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡')
    print(WeatherError.__base__)

    current_weather = get_weather()
    print(current_weather)



    # try:
    #     current_weather = get_weather()
    # except TypeError as err:
    #     print(err)
    # else:
    #     print(current_weather)

if __name__ == '__main__':
    main()