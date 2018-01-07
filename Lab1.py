import re
import requests


t = requests.get('http://www.mosigra.ru/').text
a = re.findall('[a-zA-Z0-9_.+-]+@[a-zA-Z0-9_.+-]+\.[a-zA-Z0-9_.+-]', t)
a = set(a)
print(a)
