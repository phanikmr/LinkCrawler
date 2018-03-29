import re


class Spider(object):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def parseLinks(self,html):
         return [link[0] for link in re.findall('"((http|ftp)s?://.*?)"', html)]