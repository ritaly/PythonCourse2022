import webbrowser


class URLError(Exception):
    """ custom error for url """
    pass


def is_url(url):
    prefixes = ('http://', 'https://', 'www')
    suffixes = ('.pl', '.com')

    if not url.startswith(prefixes): # http , https,  www
        raise URLError('prefix incorrect')

    if not url.endswith(suffixes):   # .com / .pl
        raise URLError('sufix incorrect')

    return url


def open_url(url_address):
    try:
        url = is_url(url_address)
        webbrowser.open(url)
    except URLError as err:
        print('URL incorrect -> reason: ', err)
    else:
        print('OK!')


def main():
    url = input('Podaj adres www:')
    open_url(url)


if __name__ == "__main__":
    main()