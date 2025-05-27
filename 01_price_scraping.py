from bs4 import BeautifulSoup
import pandas as pd
import requests

data = []
page: int = 1

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

page_url: str = f"https://www.amazon.in/s?k=mobiles&page={page}&crid=2T0QYMO1ZMQRR&qid=1748335739&sprefix=mobile%2Caps%2C226&xpid=4Lovf3DrJu03L&ref=sr_pg_{page}"

response = requests.get(page_url, headers=headers)

print("Status Code:", response.status_code)

if response.status_code == 200:

    soup = BeautifulSoup(response.text, "html.parser")

    products = soup.find_all("div", class_="a-section a-spacing-small a-spacing-top-small")
    print(f"Found {len(products)} products on page {page}.")

    for product in products:
        try:
            title_elem = product.find("h2", class_="a-size-medium a-spacing-none a-color-base a-text-normal")
            price_sym = product.find("span", class_="a-price-symbol")
            price_whole = product.find("span", class_="a-price-whole")


            if title_elem and price_sym and price_whole:
                text = title_elem.text.strip()
                price = f"{price_sym.text.strip()}{price_whole.text.strip()}"
                data.append({"Product Name": text, "Price": price})
        except Exception as e:
            print("Skipped one due to error:", e)



    df = pd.DataFrame(data)
    print("Scraped:", len(df), "products")
    print(df.head())

    df.to_csv("amazon_products.csv", index=False, encoding="utf-8-sig")