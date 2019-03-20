import requests
import xml.etree.ElementTree as ET
# API Key - 8f610bb4852b8bced12ced716a5f71ba
# https://docs.python.org/2/library/xml.etree.elementtree.html 

response = requests.get("https://www.opensecrets.org/api/?method=candContrib&cid=N00007360&cycle=2018&apikey=8f610bb4852b8bced12ced716a5f71ba")

data = ET.fromstring(response.text)

for child in data:
    print(child.attrib)
    for evenChilder in child:
        print(evenChilder.attrib)

