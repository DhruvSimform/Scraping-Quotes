# Quotes Scraper

This Python script scrapes quotes, authors, and tags from [Quotes to Scrape](http://quotes.toscrape.com) website and saves the data into a CSV file.

---

## Features

- Scrapes multiple pages automatically until no more quotes are found
- Extracts quote text, author name, and associated tags
- Saves all collected data into a CSV file (`quotes.csv`)
- Handles network errors and stops gracefully
- Built with modern Python practices

---

## Requirements

- Python 3.8+
- [uv](https://github.com/astral-sh/uv) package manager

### Dependencies

- `requests` - For HTTP requests
- `beautifulsoup4` - For HTML parsing
- `pandas` - For data manipulation and CSV export

---

## Installation

### 1. Install uv (if not already installed)

**macOS/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows:**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. Clone or download this project

```bash
git clone <your-repo-url>
cd quotes-scraper
```

### 3. Install dependencies using uv

```bash
# Add dependencies to your project
uv run

# Or install them directly
uv pip install requests beautifulsoup4 pandas
```

---

## Usage

Run the script:

```bash
uv run scrape_quotes.py
```

The script will:
1. Start scraping from the first page
2. Continue page by page until there are no more quotes
3. Display progress information in the console
4. Save the results in a CSV file named `quotes.csv` in the script directory

### Example Output
```
Scraping page 1...
Found 10 quotes on page 1
Scraping page 2...
Found 10 quotes on page 2
...
Scraping page 10...
Found 10 quotes on page 10
Scraping page 11...
No quotes found on page 11. Scraping complete.
Total quotes scraped: 100
Data saved to quotes.csv
```

---

## Script Explanation

- **Pagination:** Uses a `while True` loop with page number increment until no quotes or HTTP error occurs
- **Data Extraction:** Parses the HTML content using BeautifulSoup to extract quote text, author, and tags
- **Data Storage:** Stores all results in a list of dictionaries, then converts to a Pandas DataFrame
- **CSV Export:** Saves the DataFrame to `quotes.csv` with UTF-8 encoding
- **Error Handling:** Gracefully handles network errors and missing elements

---

## Sample Output

### CSV Format
The generated `quotes.csv` file will have the following structure:

| text | author | tags |
|------|--------|------|
| "The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking." | Albert Einstein | change,deep-thoughts,thinking,world |
| "It is our choices, Harry, that show what we truly are, far more than our abilities." | J.K. Rowling | abilities,choices |

### File Structure
```
quotes-scraper/
├── README.md
├── scraper.py
├── quotes.csv (generated after running)
└── pyproject.toml (if using uv project)
```

---

## Development

### Setting up a uv project (recommended)

```bash
# Initialize a new uv project
uv init quotes-scraper
cd quotes-scraper

# Add dependencies
uv add requests beautifulsoup4 pandas

# Run the script
uv run scraper.py
```

### Virtual Environment (alternative)

```bash
# Create virtual environment with uv
uv venv

# Activate it
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
uv pip install requests beautifulsoup4 pandas
```

---

## Notes

- This script scrapes data from a publicly available website designed for practice scraping
- Always respect website policies and robots.txt files
- Do not scrape websites without permission
- Consider adding delays between requests for production use

### Potential Enhancements

- Add user-agent headers for better compatibility
- Implement delays between requests to be respectful
- Add support for JavaScript-rendered content with Selenium
- Include data validation and cleaning
- Add command-line arguments for customization
- Implement logging for better debugging

---

## Contributing

Feel free to contribute by:
1. Forking the repository
2. Creating a feature branch
3. Making your changes
4. Submitting a pull request

---

## Author

**Dhruv**

For questions, issues, or suggestions, please open an issue in the repository.

---

## License

This project is open source and available under the [MIT License](LICENSE).