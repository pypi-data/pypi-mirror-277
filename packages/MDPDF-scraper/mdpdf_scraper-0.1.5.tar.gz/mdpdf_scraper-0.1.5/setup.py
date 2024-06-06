from setuptools import setup, find_packages

setup(
    name="MDPDF-scraper",
    version="0.1.5",
    author="Hashan Wickramasinghe",
    author_email="hashanwickramasinghe@gmail.com",
    description="A tool to scrape websites and generate PDFs from sitemap URLs.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/hashangit/MDPDF-scraper",
    packages=find_packages(include=['MDPDF_scraper', 'MDPDF_scraper.*']),
    install_requires=[
        "requests",
        "beautifulsoup4",
        "fpdf2",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'mdpdf-scraper=MDPDF_scraper.mdpdfscraper:main',
        ],
    },
    include_package_data=True,
    package_data={
        'MDPDF_scraper': ['DejaVuSans.ttf'],
    },
)
