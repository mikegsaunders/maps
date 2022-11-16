from bs4 import BeautifulSoup
import requests

# SOURCE FILES #
bibList = open("bibList.txt").read().splitlines()
holdList = open("holdList.txt").read().splitlines()
apiKey = '12345xert'

for bibID, holdID in zip(bibList, holdList):
    url = f'https://api-eu.hosted.exlibrisgroup.com/almaws/v1/bibs/{bibID}?view=full&expand=None&' \
          f'apikey={apiKey}'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'xml')
