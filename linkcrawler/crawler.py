from downloader import Downloader
from spider import Spider
from link import Link
from queue import Queue
import sys
import os
import logging

clear = None
if sys.platform == 'win32':
    clear = lambda : os.system('cls')
else:
    clear = lambda : os.system('clear')


class Crawler(object):
    """description of class"""

    lookup = None
    q = None
    feed = None
    MAT_RETREIS = 5
    INFO_LOG = logging.INFO
    ERROR_LOG = logging.ERROR
    DEBUG_LOG = logging.DEBUG

    def __init__(self, link,**kwargs):
        super(Crawler, self).__init__()
        self.lookup = {}
        self.q = Queue()
        self.feed = link.replace('https://','http://')
        if self.feed.endswith('/'):
            self.feed = self.feed[0:len(self.feed) - 1]
        self.downloader = Downloader(verify=kwargs.get('verify', True))
        link = link.replace('http://','')
        link = link.replace('https://','')
        self.path = kwargs.get('output_path',os.path.join(os.path.expanduser('~'),link.translate({ord(c): "" for c in "<>:/\\\"|?*"}) + '.txt'))    
        self. links_count = 0
        self.parser = Spider()
        log_level = kwargs.get('LOG', Crawler.INFO_LOG)
        if not os.path.exists(os.path.join(os.path.expanduser('~'),'.crawler')):
             os.makedirs(os.path.join(os.path.expanduser('~'),'.crawler'))
        logging.basicConfig(filename = os.path.join(os.path.expanduser('~'),'.crawler', link.translate({ord(c): "" for c in "<>:/\\\"|?*"}) +'.log'), 
                            format='%(asctime)s %(levelname)s %(message)s', 
                            level = log_level)
        logging.getLogger().addHandler(logging.StreamHandler())

    def __enter__(self):
        if len(self.lookup) == 0:
            self.lookup[self.feed] = Link()
            self.q.put(self.feed)
            self.file = open(self.path,'w+')
            self.file.write(self.feed+'\n')
            self.links_count = 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        logging.info("Links are saved at " + self.path)
        logging.info("Logs are saved at " +os.path.join(os.path.expanduser('~'),'.crawler'))


    def get__stats(self):
        return self.lookup


    def crawl(self, count=-1):
        try:
            while not self.q.empty():
                link = self.q.get()
                if not self.lookup[link].crawled:
                    clear()
                    logging.info("Links extracted : " 
                                + str(self.links_count))
                    if self.links_count >= count and count > 0:
                        return
                    logging.debug(link + ' being crawled')
                    self.__get_links(link)
        except KeyboardInterrupt:
            sys.exit()

    def crawl_next(self):
       while not self.q.empty():
            link = self.q.get()
            if not self.lookup[link].crawled:  
                logging.debug(link + ' being crawled')
                self.__get_links(link)
                links = self.lookup.keys()
                yield links


    def __get_links(self,link):
        try:
            response = self.downloader.getContent(link)
            if response.status_code == 200:
                self.lookup[link].crawled = True               
                links = self.parser.parseLinks(response.text)
                logging.debug(link + ' crawled' + str(len(links)))
                self.lookup[link].extracted_links_count = len(links)                           
                for link in links:                    
                    self.q.put(link)
                    if not link in self.lookup:
                        self. links_count += 1
                        self.file.write(link + '\n')
                        self.lookup[link] = Link()
            else:
                logging.error(link + ' failed to get response with code '+ str(response.status_code))
                self.lookup[link].res_code = response.status_code
                self.lookup[link].attempts += 1
                if self.lookup[link].attempts < Crawler.MAT_RETREIS:
                    self.q.put(link)
                else:
                    logging.error(link + ' MAX_RETRIES Exceeded')           
        except Exception as err:
             logging.error(err)


if __name__ == "__main__":
    with Crawler("https://www.example.com",output_path='D://sample.txt', LOG=Crawler.DEBUG_LOG) as crawler:
        crawler.crawl()