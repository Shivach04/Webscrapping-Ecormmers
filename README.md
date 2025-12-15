# Webscrapping-Ecormmers

## Project

Web Scraping Flipkart: Data Cleaning, Visualization, and Insights

This repository contains a Jupyter Notebook and dataset for scraping smart TV product listings from Flipkart, cleaning the scraped data, and producing exploratory visualizations and insights.

## Structure

- `TV/Webscrapping-Smart-tv.ipynb` — Jupyter notebook that performs the web scraping, data cleaning, simple feature extraction (display type, model id, launch year, sound output), and visualizations.
- `TV/Flipkart_SmartTV_Data.csv` — Resulting CSV produced by the notebook (saved from the notebook). Contains the cleaned TV dataset.

## Summary of what the notebook does

- Scrapes Flipkart search result pages for "Smart TVs" (paging loop present).
- Extracts product name, price, rating, display type (LED/QLED/OLED/etc.), launch year, sound output, and model id where available.
- Cleans and normalizes text fields and numeric price values.
- Builds a pandas DataFrame and saves it to `TV/Flipkart_SmartTV_Data.csv`.
- Includes univariate and bivariate visualizations using seaborn/matplotlib.

## Requirements

- Python 3.8+ recommended
- Packages used in the notebook:
	- requests
	- beautifulsoup4
	- pandas
	- matplotlib
	- seaborn
	- lxml (optional, for faster/parsing robustness)

You can install the common requirements with pip (run from project root):

```powershell
python -m venv .venv; .\.venv\Scripts\Activate; pip install --upgrade pip
pip install requests beautifulsoup4 pandas matplotlib seaborn lxml
```

## How to run

1. Open `TV/Webscrapping-Smart-tv.ipynb` in Jupyter Notebook, Jupyter Lab, or VS Code's notebook UI.
2. Inspect the top cells for headers and the scraping loop. If you want to re-run scraping, run the cells that perform requests and parsing.
	 - Note: the notebook contains a loop over pages and a polite `time.sleep(1)` between page requests. Respect Flipkart's terms and robots.txt.
3. The notebook will create or overwrite `TV/Flipkart_SmartTV_Data.csv` when it reaches the saving cell.
4. Run the downstream cleaning and visualization cells to reproduce charts and analysis.

## Data (columns)

The saved CSV contains at least the following columns:

- `TV Name` — cleaned product name
- `Price` — numeric price (float)
- `Display Type` — extracted display type (LED, QLED, OLED, NanoCell, or Unknown)
- `Rating` — text rating scraped from the listing
- `Launch Year` — extracted or parsed launch year when available
- `Sound Output` — parsed sound information
- `Model ID` — model identifier when available

## Notes & Best Practices

- Scraping sites may be subject to terms of service and legal restrictions. Use this code responsibly and only against pages you are permitted to crawl.
- Respect rate limits and introduce delays to avoid overwhelming servers.
- Flipkart may change HTML structure; if scraping stops working, inspect the page and update the selectors in the notebook.
- The notebook's parsing uses simple heuristics — consider adding more robust extraction (regex improvements, fallback strategies) for production use.

## Possible improvements / next steps

- Add robust error handling and retries for failed requests.
- Use `requests.Session()` and connection pooling.
- Add unit tests for parsing/extraction functions.
- Export a cleaned dataset to additional formats (Parquet) and add basic EDA automation.

## Author

Shivach04

## License

This repository does not include an explicit license file. Add a license (e.g., MIT) if you want others to reuse your work.
