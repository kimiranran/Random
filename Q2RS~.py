#“I have not given or received any unauthorized assistance on this assignment.”
#ranran shi
#dsc430
#question2


from urllib.request import urlopen
from html.parser import HTMLParser
from urllib.parse import urljoin
from collections import Counter

class Collector(HTMLParser):
    '''collects hyperlink URLs into a list'''

    def __init__(self, url):
        '''initializes parser, the url, and a list'''
        HTMLParser.__init__(self)
        self.url = url
        self.links = []
        self.words = []

    def handle_starttag(self, tag, attrs):
        '''collects hyperlink URLs in their absolute format'''
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    # construct absolute URL
                    absolute = urljoin(self.url, attr[1])
                    if absolute[:4] == 'http': # collect HTTP URLs
                        self.links.append(absolute)

    def handle_data(self, data):
        new_words = Counter(data.split()).most_common()
        for word, count in new_words:
            if word.isalpha():
                for wcpair in self.words:
                    if word == wcpair[0]:
                        wcpair[1] += count
                        return
                self.words.append([word, count])

                        
    def getLinks(self):
        '''returns hyperlinks URLs in their absolute format'''
        return self.links

    def getWords(self):
        return self.words

    def get25Words(self):
        list = sorted(self.words, key=lambda x: x[1], reverse=True)
        return list[:25]

visited = set() # initialize visited to an empty set
most_common_words = []

def analyze(url):

    global most_common_words
    
    print('\n\nVisiting', url)           # for testing

    # obtain links in the web page
    content = urlopen(url).read().decode().lower()
    collector = Collector(url)
    collector.feed(content)
    urls = collector.getLinks()          # get list of links

    # compute word frequencies
    freq = collector.getWords()
    #print(collector.getWords())
    for [word, count] in freq:
        added = False
        for wcpair in most_common_words:
            if word == wcpair[0]:
                wcpair[1] += count
                added = True
        if not added:
            most_common_words.append([word, count])
    output = sorted(most_common_words, key=lambda x: x[1], reverse=True)
    output = output[:25]

    # print the frequency of every text data word in web page
    print('\n{:20} {:10}'.format('word', 'count'))
    for [word, count] in output:
        print('{:20} {:10}'.format(word, count))

    return urls

def crawl2(url):
    '''a recursive web crawler that calls analyze()
       on every visited web page'''

    # add url to set of visited pages
    global visited     # warns the programmer 
    if len(visited) > 500:
        return
    visited.add(url)

    # analyze() returns a list of hyperlink URLs in web page url 
    links = analyze(url)

    # recursively continue crawl from every link in links
    for link in links:
        # follow link only if not visited
        if 'https://www.cdm.depaul.edu/' in link:
            if link not in visited:
                try:
                    crawl2(link)
                except:
                    pass

crawl2('https://www.cdm.depaul.edu/')

'''
result from running this code on 500 pages
word                       count     
var                       10119
the                        9178
and                        6446
csc                        4846
web                        4774
cdm                        3858
to                         3686
admission                  2643
meeting                    2576
graduate                   2518
fall                       2370
depaul                     2352
spring                     2290
academic                   2276
winter                     2260
view                       2112
section                    1996
class                      1994
faculty                    1855
undergraduate              1840
function                   1791
student                    1669
credits                    1664
in                         1590
course                     1523
'''

