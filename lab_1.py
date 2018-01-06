import requests
import re

def main():
	base_url='http://mosigra.ru'
	r = requests.get(base_url)
	t=r.text
	a=re.findall('[a-zA-Z0-9_.+-]+@[a-zA-Z0-9.+-]+\.[a-zA-Z0-9.]+',t)
	print(a)

main()