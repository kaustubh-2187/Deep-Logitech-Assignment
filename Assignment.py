import requests
from bs4 import BeautifulSoup
import json

url="https://time.com/"

r = requests.get(url)
htmlContent = r.content

soup = BeautifulSoup(htmlContent, 'html.parser')

# This list will eventually contain each article's title and link
data=[]

# Finding all the <li> with the class name of 'featured-voices__list-item'
lis=soup.find_all("li", {'class': 'featured-voices__list-item'})
# Looping through all the <li> tags to access each <li> tag for the <a> and <h3> tag
for li in lis:
    # Finding the <a> tag which is a children tag of each <li> tag
    articleLink=li.findChildren("a", recursive=False)[0]
    # Finding the <h3> tag which is a children tag of each <a> tag
    articleTitle = articleLink.findChildren("h3", recursive=False)[0].string
    link=url+str(articleLink.get('href'))
    #Appending the title and link into the data list
    data.append({
        "title" : articleTitle,
        "link" : link
    })
    
# Converting the data list into a String
jsonString = json.dumps(data)
# Converting the String into a JSON Object
jsonObject = json.loads(jsonString)
print(jsonObject)
