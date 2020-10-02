import sys
import os
import requests
from bs4 import BeautifulSoup
from colorama import init, Fore

init(autoreset=True)

# write your code here
path = sys.argv[1]
if not os.path.exists(path):
    os.makedirs(path)

site = ""
prev = ""
stack = []

while True:
    if site != "":
        prev = site
    site = input()
    if site == 'exit':
        break
    elif '.' not in site and site != 'back':
        print("Error: please enter a valid URL")
        continue
    elif site == 'back':
        print(stack.pop())
        continue
    else:
        idx = site.rfind('.')
        file = site[:idx]
        if site[:8] != 'https://':
            url = 'https://' + site
        else:
            url = site

    file_path = f'{path}/{file}'
    if os.path.exists(file_path):
        with open(file_path, 'r') as content:
            print(content.read())
    else:
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        tags = soup.find_all(['p', 'a', '^h[1-6$', 'ol', 'ul', 'li'])
        with open(file_path, 'a') as content:
            for element in tags:
                text = element.text
                if element.name == 'a':
                    print(Fore.BLUE + text)
                    content.write(Fore.BLUE + text)
                else:
                    print(text)
                    content.write(text)
    if prev:
        stack.append(prev)
