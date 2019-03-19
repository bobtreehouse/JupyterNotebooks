##Webscrape Project #
#Here is a webscraper I wrote to pull text only from page 1 of NY Times and WSJ#

#this delievers the text only in a cleaned-version'#

import bs4 as bs
import urllib.request 

sauce = urllib.request.urlopen('https://www.nytimes.com/').read()
soup = bs.BeautifulSoup(sauce, 'lxml')
sauce2 = urllib.request.urlopen('https://www.wsj.com/').read()
soup2 = bs.BeautifulSoup(sauce2, 'lxml')

nav = soup.nav  
body = soup.body
text = soup.text
table= soup.table
div = soup.div
nav2 = soup2.nav  
body2 = soup2.body
text2 = soup2.text
table2 = soup2.table
div2 = soup2.div
url = soup.url
url2 = soup2.url

filename = 'NYTimesWSJheadlines.txt'
f = open(filename, "w") 
body = soup.body
text = soup.text   
for paragraph in body.find_all('h2'):
    f.write(paragraph.text)
    f.write('\n')
       #f.write("")   
for paragraph in body2.find_all('h3'):
    f.write(paragraph.text)
    f.write('\n')
f.close()

def wordCounter(in_name):
    f_in=open(in_name, 'r', encoding="cp1252")
    lines=f_in.readlines()
    f_in.close()

    D={} 
    
    for line in lines:
        line=line.strip()
        line=line.lower()
        for mark in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~':
            line=line.replace(mark,'')    
        words=line.split()
        for word in words:
            if word in D:
                D[word]+=1
            else:
                D[word]=1
                
    L=list(D.items())
    return sorted(L,key=lambda x:x[1],reverse=True)
    
    def text_cleaner(in_name, out_name, punc=list('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')):
    f_in = open(in_name, 'r')
    f_out = open(out_name, 'w')
    lines=f_in.readlines()
    f_in.close()
    for line in lines:
        line=line.lower()
        for mark in punc:
            line=line.replace(mark, '')
        f_out.write(line)
    f_out.close()
    print(out_name, 'has been written')
