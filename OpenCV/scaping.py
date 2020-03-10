import bs4
import requests
url ='http://localhost/progect/Final/cd.php'
data = requests.get(url)
soup=bs4.BeautifulSoup(data.text,'html.parser')
#print (soup.prettify()) #print all the html in the page
# for para in soup.find_all('li'): # To print the li item only 
#     print(para.text)
for links in soup.find_all('a'):
    link = links.get('href') #get all the link in the pages
    # if link[0:3]=="../" and link! ='#':
    #     print("http://localhost/progect/Final/cd.php" +link[2:len(link)])
    # elif link[0]='/' and link!='#':
    #     print("http://localhost/progect/Final/cd.php" +link)
    # elif link!='#':
    #     print(link)
    if link != '#':
        print("http://localhost/progect/Final/cd.php/" +link)




