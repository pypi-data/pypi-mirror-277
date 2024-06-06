import requests
from bs4 import BeautifulSoup
from fpdf import FPDF
from datetime import datetime

def scrape_url(url: str) -> str:
    """
    Scrapes the HTML content from a URL and converts it to Markdown.

    Args:
        url: str
            The URL to scrape.

    Returns:
        str
            The Markdown content.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for non-200 status codes
        soup = BeautifulSoup(response.content, "html.parser")
        markdown_content = ""
        for element in soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6", "p", "li"]):
            if element.name == "h1":
                markdown_content += "# " + element.get_text() + "\n\n"
            elif element.name == "h2":
                markdown_content += "## " + element.get_text() + "\n\n"
            elif element.name == "h3":
                markdown_content += "### " + element.get_text() + "\n\n"
            elif element.name == "h4":
                markdown_content += "#### " + element.get_text() + "\n\n"
            elif element.name == "h5":
                markdown_content += "##### " + element.get_text() + "\n\n"
            elif element.name == "h6":
                markdown_content += "###### " + element.get_text() + "\n\n"
            elif element.name == "p":
                markdown_content += element.get_text() + "\n\n"
            elif element.name == "li":
                markdown_content += "* " + element.get_text() + "\n\n"
        return markdown_content
    except requests.RequestException as e:
        raise Exception(f"Error fetching URL: {e}")

def generate_pdf(markdown_content: str, url: str, scraped_date: str, filename: str) -> None:
    """
    Generates a PDF file from the Markdown content.

    Args:
        markdown_content: str
            The Markdown content.
        url: str
            The URL of the scraped page.
        scraped_date: str
            The date the page was scraped.
        filename: str
            The filename for the PDF file.
    """
    pdf = FPDF()
    pdf.add_page()
    pdf.add_font("DejaVu", "", "DejaVuSans.ttf", uni=True)
    pdf.set_font("DejaVu", size=12)
    pdf.multi_cell(0, 10, f"URL: {url}\nScraped Date: {scraped_date}\n\n")
    for line in markdown_content.split('\n'):
        if len(line) > 0:
            pdf.multi_cell(0, 10, line)
        else:
            pdf.ln()
    pdf.output(filename, "F")

def main():
    all_urls = [
        "https://example.com",  # Replace with actual URLs to scrape
        "https://another-example.com"
    ]
    
    for url in all_urls:
        markdown_content = scrape_url(url)
        scraped_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        filename = f"{url.replace('https://', '').replace('http://', '').replace('/', '_')}.pdf"
        generate_pdf(markdown_content, url, scraped_date, filename)
        print(f"Generated PDF file: {filename}")

if __name__ == "__main__":
    main()
