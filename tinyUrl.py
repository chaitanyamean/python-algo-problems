
import random
import string


d = {}

def shortURL(longUrl):
    l = random.randint(6,10)
    print(l)

    chars = string.ascii_lowercase
    shortURL = ''.join(random.choice(chars) for i in range(l))
    print(shortURL)

    if shortURL in d:
        return shortURL(longUrl)
    else:
        d[shortURL] = longUrl
    
    print(d)
    r = 'https://www.shortURL.com/' + shortURL
    return r


print(shortURL('https://www.google.com'))


