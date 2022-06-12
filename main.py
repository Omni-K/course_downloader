from pywebcopy import save_webpage
import os
import requests
from bs4 import BeautifulSoup
print(download_folder := os.path.curdir+'/downloads/')
for n in range(1, 7+1):
    url = f'https://chanceforchange.ru/kurs-dengi-{n}-lekciya/'
    html = requests.request(method='GET', url=url).text
    save_webpage(url=url,
                 project_folder=download_folder, project_name=url.split('/')[3],
                 bypass_robots=True, open_in_browser=False,
                 )
    soup = BeautifulSoup(html, "html.parser")

    for idx, tag in enumerate(soup.find_all('source'), start=1):
        link = tag.get('src')
        file = requests.get(link, stream=True)
        if file.status_code == 200:
            save_file = open(f'{download_folder}{n}-{idx}.mp3', 'wb')
            save_file.write(file.content)
            save_file.close()

