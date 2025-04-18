import requests
from bs4 import BeautifulSoup
import random
import datetime

def get_google_trends(keyword):
    today = datetime.date.today()
    return [(today - datetime.timedelta(days=i), random.randint(10, 100)) for i in range(30)][::-1]

def get_etsy_results(keyword):
    fake_data = []
    for i in range(1, 6):
        fake_data.append({
            "Titolo": f"{keyword.title()} Prodotto {i}",
            "Vendite stimate": random.randint(50, 500),
            "Prezzo (€)": round(random.uniform(2.99, 19.99), 2),
            "Link": f"https://www.etsy.com/listing/{random.randint(100000000, 999999999)}"
        })
    return fake_data
