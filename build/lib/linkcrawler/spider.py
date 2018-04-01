import re


class Spider(object):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def parseLinks(self,html):
         return [self.__remove_s(link[0]) for link in re.findall('"((http|ftp)s?://.*?)"', html)]

    def __remove_s(self,st):
         if st.startswith('https'):
            st = st.replace('https://','http://',1)
         if st.endswith('/'):
            return st[0:len(st)-1]
         return st

if __name__ == "__main__":
    sp = Spider()
    print(sp.parseLinks(""" <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <title>17.4. concurrent.futures — Launching parallel tasks — Python 3.6.5 documentation</title>
    <link rel="stylesheet" href="../_static/pydoctheme.css" type="text/css">
    <link rel="stylesheet" href="../_static/pygments.css" type="text/css">
    <script type="text/javascript">
      var DOCUMENTATION_OPTIONS = {
        URL_ROOT:    '../',
        VERSION:     '3.6.5',
        COLLAPSE_INDEX: false,
        FILE_SUFFIX: '.html',
        HAS_SOURCE:  true,
        SOURCELINK_SUFFIX: '.txt'
      };
    </script>
    <script type="text/javascript" src="../_static/jquery.js"></script>
    <script type="text/javascript" src="../_static/underscore.js"></script>
    <script type="text/javascript" src="../_static/doctools.js"></script>
    <script type="text/javascript" src="../_static/sidebar.js"></script>
    <link rel="search" type="application/opensearchdescription+xml" title="Search within Python 3.6.5 documentation" href="../_static/opensearch.xml">
    <link rel="author" title="About these documents" href="../about.html">
    <link rel="index" title="Index" href="../genindex.html">
    <link rel="search" title="Search" href="../search.html">
    <link rel="copyright" title="Copyright" href="../copyright.html">
    <link rel="next" title="17.5. subprocess — Subprocess management" href="subprocess.html">
    <link rel="prev" title="17.3. The concurrent package" href="concurrent.html">
    <link rel="shortcut icon" type="image/png" href="../_static/py.png">
    <link rel="canonical" href="https://docs.python.org/3/library/concurrent.futures.html/">
    
    <script type="text/javascript" src="../_static/copybutton.js"></script>
    <script type="text/javascript" src="../_static/switchers.js"></script>
    
    
 

  </head>"""))