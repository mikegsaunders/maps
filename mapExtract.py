import os
from bs4 import BeautifulSoup
import requests

# SECRETS #
apiKey = os.environ['API_KEY_SAND']
# apiKey = os.environ['API_KEY_PROD']

# SOURCE FILES #
bibList = open("bibList.txt").read().splitlines()
holdList = open("holdList.txt").read().splitlines()


for bibID, holdID in zip(bibList, holdList):
    url = f'https://api-eu.hosted.exlibrisgroup.com/almaws/v1/bibs/{bibID}?view=full&expand=None&' \
          f'apikey={apiKey}'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'xml')
