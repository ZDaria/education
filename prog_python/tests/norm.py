def normalize_url(url_string):
    if url_string[:len("https:")] == "https:":
        return url_string
    elif url_string[:len("http:")] == "http:":
        return url_string.replace("http://", )
    # 'https://yandex.ru'
    else: "https\:\/\/" + url_string


print(normalize_url('yandex.ru'))
