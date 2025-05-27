import requests
import pandas as pd
from bs4 import BeautifulSoup

data = []

page_no: int=1
while True:
    try:
        url: str= f"http://quotes.toscrape.com/page/{page_no}/"

        response = requests.get(url)
        if response.status_code != 200:
            break
        soup = BeautifulSoup(response.text, "html.parser")

        quotes = soup.find_all("div", class_="quote")

        if not quotes:
            break

        for quote in quotes:
            text = quote.find("span", class_="text").text
            author = quote.find("small", class_="author").text
            tags = [tag.text for tag in quote.find_all("a", class_="tag")]



            data.append({"text": text, "author": author , "tags": ", ".join(tags)})
        print(f"Scraped page {page_no} with {len(quotes)} quotes.")
        page_no += 1
    except Exception as e:
        print(f"An error occurred: {e}")
        break
# Convert the data to a DataFrame
df = pd.DataFrame(data)
# Save the DataFrame to a CSV file
df.to_csv("quotes.csv", index=True, encoding="utf-8-sig")
# Scrape quotes from a website and save them to a CSV file


print("Scraping completed. Quotes saved to quotes.csv")