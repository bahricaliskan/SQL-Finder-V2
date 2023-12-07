import requests
from bs4 import BeautifulSoup
from termcolor import colored

class LinkScanner:
    def __init__(self, target_url):
        self.target_url = target_url

    def scan_links(self):
        try:
            response = requests.get(self.target_url)
            soup = BeautifulSoup(response.text, 'html.parser')

            links = soup.find_all('a', href=True)

            for link in links:
                if 'id=' in link['href']:
                    print(colored(f"SQL Açığı Bulundu: {link['href']}", 'green'))
        except requests.RequestException as e:
            print(f"Hata: {str(e)}")

if __name__ == "__main__":
    print(colored("***************************************", 'blue'))
    print(colored("**         SQL SCANNER 1 PROJECT             **", 'blue'))
    print(colored("***************************************\n", 'blue'))

    target_url = input(colored("Hedef linki girin: ", 'yellow'))
    link_scanner = LinkScanner(target_url)
    link_scanner.scan_links()
