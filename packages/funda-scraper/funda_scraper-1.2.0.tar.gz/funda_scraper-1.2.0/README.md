# FundaScraper

[![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)
[![Build Status](https://app.travis-ci.com/whchien/funda-scraper.svg?branch=main)](https://app.travis-ci.com/whchien/funda-scraper)
[![codecov](https://codecov.io/gh/whchien/funda-scraper/branch/main/graph/badge.svg?token=QUKTDyeUqp)](https://codecov.io/gh/whchien/funda-scraper)
[![Downloads](https://static.pepy.tech/badge/funda-scraper)](https://pepy.tech/project/funda-scraper)
[![PyPI version](https://img.shields.io/pypi/v/funda-scraper)](https://pypi.org/project/funda-scraper/)
[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)

`FundaScaper` provides you the easiest way to perform web scraping from Funda, the Dutch housing website. 
You can find houses either for sale or for rent, and the historical data from the past few year are also attainable.

Please note:
1. Scraping this website is ONLY allowed for personal use (as per Funda's Terms and Conditions).
2. Any commercial use of this Python package is prohibited. The author holds no liability for any misuse of the package.


## Install
1. The easiest way is to install with pip:
```
pip install funda-scraper
```
2. You can also clone the repository to your local machine with:
```
git clone https://github.com/whchien/funda-scraper.git
cd funda-scraper
export PYTHONPATH=${PWD}
python funda_scraper/scrape.py --area amsterdam --want_to rent --page_start 1 --n_pages 3 --save
```

## Quickstart 
```
from funda_scraper import FundaScraper

scraper = FundaScraper(area="amsterdam", want_to="rent", find_past=False, page_start=1, n_pages=3, min_price=500, max_price=2000)
df = scraper.run(raw_data=False, save=True, filepath="test.csv")
df.head()
```
![image](static/example_df.png)


*** Note: if you are using Windows, please add `if __name__ == '__main__':
` before your script.


You can pass several arguments to `FundaScraper()` for customized scraping:
- `area`: Specify the city or specific area you want to look for, e.g. Amsterdam, Utrecht, Rotterdam, etc.
- `want_to`: You can choose either `buy` or `rent`, which finds houses either for sale or for rent. 
- `find_past`: Specify whether you want to find the data in the past or the ones in the market. If `True`, only historical data will be scraped. The default is `False`.
- `page_start`: Indicate which page you want to start scraping. The default is `1`. 
- `n_pages`: Indicate how many page you want to scrape. The default is `1`. 
- `min_price`: Indicate the lowest amount for the budget.
- `max_price`: Indicate the highest amount for the budget.
- `min_floor_area`: Indicate the lowest floor area.
- `max_floor_area`: Indicate the highest floor area.
- `days_since:`: Specify the maximum amount of days since listing date.
- `property_type`: Specify the desired property type(s).
- `sort`: Specify sorting.


The scraped raw result contains following information:
- url
- price
- address
- description
- listed_since
- zip_code 
- size
- year_built
- living_area
- kind_of_house
- building_type
- num_of_rooms
- num_of_bathrooms
- layout
- energy_label
- insulation
- heating
- ownership
- exteriors
- parking
- neighborhood_name
- date_list
- date_sold
- term
- price_sold
- last_ask_price
- last_ask_price_m2
- city

*** Note: information regarding listing date is no longer available since 2023 Q4. Funda requires users to log in to see this information.

You can specify `scraper.run(raw_data=True)` to fetch the data without preprocessing.

## More information

You can check the [example notebook](https://colab.research.google.com/drive/1hNzJJRWxD59lrbeDpfY1OUpBz0NktmfW?usp=sharing) for further details. 
Please give me a [star](https://github.com/whchien/funda-scraper) if you find this project helpful. 


