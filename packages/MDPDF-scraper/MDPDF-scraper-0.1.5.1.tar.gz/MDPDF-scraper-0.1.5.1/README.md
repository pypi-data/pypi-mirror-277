# MDPDF Web Scraper

A Python package for scraping websites and generating PDFs from their content.

## What it does

This package allows you to scrape a website's sitemap, extract the HTML content from each URL, convert it to Markdown, and generate a PDF file for each URL. The package uses concurrent futures for asynchronous processing, making it efficient and fast.

## How to use

### Installation

You can install the package using pip:

```
pip install MDPDF-scraper
```

### Usage

To use the package, simply import the `WebToPDF_Scraper` function and pass the URL of the website's sitemap as an argument:

```
from MDPDF_scraper.mdpdfscraper import WebToPDF_Scraper

if __name__ == "__main__":
    sitemap_url = "https://www.example.com/sitemap.xml"
    pdf_folder = "pdfs"
    scraper = WebToPDF_Scraper(sitemap_url, pdf_folder)
    scraper.scrape()
```
This will scrape the website's sitemap, extract the HTML content from each URL, convert it to Markdown, and generate a PDF file for each URL. The PDF files will be saved in a directory named "pdfs".

## Configuration

You can change the directory where the PDF files are saved by modifying the `pdf_folder` variable.

## Requirements

The package requires the following dependencies:

- `requests`
- `beautifulsoup4`
- `fpdf2`

## License

This package is licensed under the MIT License.

Hashan Wickramasinghe
InferQ
hashan@inferencequotient.com
