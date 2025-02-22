import LinkManager
import os
from colorama import Fore

def rel_path(rel):
    return os.path.normpath(os.path.join(os.path.dirname(__file__), rel))

IN_PATH = rel_path('../input/catalog.txt')
OUT_PATH = rel_path('../output')

with open(IN_PATH, 'r') as file:
    catalog = [i.strip('\n') for i in file.readlines()]

links = []
for link in catalog:
    links.append(LinkManager.link(link, OUT_PATH))

for count, link in enumerate(links):
    print(f'{Fore.BLUE}@@@{Fore.MAGENTA}{count}/{len(links)}')
    print(Fore.RESET)
    link.download()
    print(f'{Fore.BLUE}@@@{Fore.GREEN}Downloaded {link.name}')
    print(Fore.RESET)