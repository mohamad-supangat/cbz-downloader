""" An example of a module file

To create a new module:

* Copy this to the cbzdl/modules folder
* Flesh out your copy of the file
* Edit ComicEngine.py and add your module to the list
"""

# https://mangasusuku.xyz/komik/milf-hunting-in-another-world/
#     https://mangasusuku.xyz/milf-hunting-in-another-world-chapter-23/

import web
import util
import re
import feedback
import ComicEngine
import base64

# Edit this to list the valid domains for the site
valid_domains = ['mangasusuku.xyz']
recommended_delay = 0

class ComicSite(web.WebResource):

    def __init__(self, url):
        url = self.validateUrl(url)

        web.WebResource.__init__(self, url)
        self.domain = web.getUrlComponents(url, 2)

    def validateUrl(self, url):
        """ If you want to rewrite the URL before accessing it, modify this section
        """
        return re.sub("^http:","https:",url)

class Comic(ComicSite):

    def __init__(self, url):
        ComicSite.__init__(self, url)

        # ubah url
        self.url = url
        self.name = self.getComicLowerName()

    def getComicLowerName(self):
        # ubah path
        return util.regexGroup("https://%s/komik/([^/]+)" % self.domain, self.url)

    def getChapterUrls(self):
        doc = self.getDomObject()

        # dapatkan url chapther
        chapters = doc.cssselect("#chapterlist > ul a")

        urls = []

        for elem_a in chapters:
            path = elem_a.attrib['href']

            # regex untuk validasi url chapter
            if re.match("/ch/%s-chapter-[0-9.]+" % self.name, path):
                urls.append(path)
                # urls.append("https://%s%s"%(self.domain, path) )

        # lakukan reverse url agar urutan tidak terbalik
        urls.reverse()
        # util.naturalSort(urls, ".+/ch-chapter-([0-9.]+)$")

        # print(urls)

        return urls

class Chapter(ComicSite):

    def __init__(self, url):
        ComicSite.__init__(self, url)

    def getChapterLowerName(self):
        return "%s-chapter-%s" % (
            util.regexGroup("https://%s/([^/]+)" % self.domain, self.url),
            self.getChapterNumber().zfill(4)
            )

    def getChapterNumber(self):
        return util.regexGroupSearch(r'chapter-(\d+)', self.url)

    def getPageUrls(self):
        doc = self.getDomObject()

        image_nodes = doc.cssselect("#Baca_Komik img")

        page_urls = []
        # All pages are in one page - encode them and stuff them in a bogus query string
        i = 1
        for img in image_nodes:
            imgurl = img.attrib['src']
            feedback.debug(imgurl)
            pagenum = i
            i += 1

            page_urls.append(imgurl)

        # print(page_urls)
        return page_urls

class Page(ComicSite):

    def __init__(self, url):
        ComicSite.__init__(self, url)

    def getPageNumber(self):
        return util.regexGroupSearch(r'(\d+)\.(jpg|jpeg|png|gif|webp)$', self.url, 1)

    def getImageUrl(self):
        return self.url
