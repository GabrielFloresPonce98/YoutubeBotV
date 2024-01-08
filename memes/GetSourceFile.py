from icrawler.builtin import GoogleImageCrawler

class GetSourceFile:
    def __init__(self, search, quantity):
        self.search = search
        self.quantity = quantity

    def search_imag(self):
        google_crawler = GoogleImageCrawler(storage={'root_dir': 'C:\\Users\\ARRMEED\\Documents\\Projectos\\YoutubeBotV\\resources\\images'})
        google_crawler.crawl(keyword=self.search, max_num= self.quantity)
        
