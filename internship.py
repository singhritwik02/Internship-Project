from email import header
import requests
from bs4 import BeautifulSoup

def getOverView(singleLink):
    singleR = requests.get(url = singleLink,headers = headerS)
    singleBSoup = BeautifulSoup(singleR.content,'html5lib')
    overView = singleBSoup.find('span',{'class':'detl lng_commn_all'}).text.strip()
    return overView


#getting the search string from user
searchString = input("Enter Search String:- ")
#creating the search url

URL = "https://www.justdial.com/Mumbai/search?q="+searchString
#adding the browser agent

headerS = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
print(URL)

#getting the content from the url
r = requests.get(url = URL,headers=headerS)
#printing the content

bSoup = BeautifulSoup(r.content,'html5lib')
table = bSoup.findAll('li', {'class': 'cntanr'})

for single in table:
    for n in range(0,3):
        print()
    #getting and printing the name 
    name = single.find('span', {'class':'jcn'}).a.attrs['title']
    print("Name = "+name)
    #getting and printing the address
    address = single.find('span',{'class':'cont_fl_addr'}).text.strip()
    print("Address = "+address)
    #getting the single link of the page to fetch overview
    link = single.find('span',{'class':'jcn'}).a.attrs['href']
    #printing the overview
    print()
    print("OverView of "+name)
    for n in range(0,200):
        
        if(n == 100):
            print()
            print()
            print(getOverView(link))
        else:
            print("+",end = '')
    print()
    


