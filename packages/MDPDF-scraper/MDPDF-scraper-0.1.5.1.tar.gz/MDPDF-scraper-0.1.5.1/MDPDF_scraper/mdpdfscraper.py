from .util.indexer import sitemap
from .util.webtoPDF import scrape_url, generate_pdf
from datetime import datetime
import os
import concurrent.futures

class WebToPDF_Scraper:
    def __init__(self, sitemap_url, pdf_folder):
        self.sitemap_url = sitemap_url
        self.pdf_folder = pdf_folder

    def process_url(self, url):
        markdown_content = scrape_url(url)
        scraped_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        filename = f"{url.replace('https://', '').replace('http://', '').replace('/', '_')}.pdf"
        return markdown_content, url, scraped_date, filename

    def save_pdf(self, result):
        markdown_content, url, scraped_date, filename = result
        filename = os.path.join(self.pdf_folder, filename)
        generate_pdf(markdown_content, url, scraped_date, filename)
        print(f"Generated PDF file: {filename}")

    def scrape(self):
        all_urls = sitemap(self.sitemap_url)
        print("URLs found in sitemap:")
        for url in all_urls:
            print(url)

        os.makedirs(self.pdf_folder, exist_ok=True)

        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = {executor.submit(self.process_url, url): url for url in all_urls}
            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                self.save_pdf(result)

def main(sitemap_url, pdf_folder):
    scraper = WebToPDF_Scraper(sitemap_url, pdf_folder)
    scraper.scrape()

if __name__ == "__main__":
    sitemap_url = "https://python.langchain.com/sitemap.xml"
    pdf_folder = "pdfs"
    main(sitemap_url, pdf_folder)
