
# importing the required modules:

import csv
import requests
import xml.etree.ElementTree as ET
import pandas as pd
from flask import Flask, render_template 

def loadRSS():

    # url of rss feed
    url = 'http://www.ynet.co.il//Integration//StoryRss1854.xml'

    # creating HTTP response object from given url
    resp = requests.get(url)

    # saving the xml file of the rss
    with open('topnewsfeed.xml', 'wb') as f:
        f.write(resp.content)
        

def parseXML(xmlfile):
  
    # create element tree object
    tree = ET.parse(xmlfile)
  
    # get root element
    root = tree.getroot()
  
    # create empty list for news items
    newsitems = []
  
    # iterate news items
    for item in root.findall('./channel/item'):
  
        # empty news dictionary
        news = {}
        
  
        # iterate child elements of item
        for child in item:
  
            # special checking for namespace object content:media
            if child.tag == '{http://www.ynet.co.il/articles/0}content':
                news['media'] = child.attrib['url']
            else:
                try:
                    
                    news[child.tag] = child.text
                except AttributeError:
                    continue
  
        # append news dictionary to news items list
        newsitems.append(news)
      
    # return news items list
    return newsitems

# specifying the fields for csv file
headings = ['category', 'title', 'description', 'link', 'pubDate', 'guid']

def savetoCSV(newsitems, filename):

    # writing to csv file
    with open(filename, 'w') as csvfile:

        # creating a csv dict writer object
        writer = csv.DictWriter(csvfile, fieldnames = headings)

        # writing headers (field names)
        writer.writeheader()

        # writing data rows
        writer.writerows(newsitems)

app = Flask(__name__)
@app.route('/')
def main():
    # load rss from web to update existing xml file
    loadRSS()

    # parse xml file
    newsitems = parseXML('topnewsfeed.xml')

    # store news items in a csv file
    savetoCSV(newsitems, 'topnews.csv')

    a = pd.read_csv("topnews.csv",encoding='hebrew')
    
    with open("topnews.csv") as f:
                data=[tuple(line) for line in csv.reader(f) if len(tuple(line))>0]
                          
    return render_template("table.html", headings=headings, data=data[1:])
    
    
if __name__ == "__main__":
        app.run(host='0.0.0.0' , debug=True)

#To run the app go to any browser and enter this link: http://127.0.0.1:5000/
