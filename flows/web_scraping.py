import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

class whisky_data_scraping():

    
    def scrape_html(seft, base_url):
        seft.base_url = base_url
        
        options = Options()
        # options.add_argument('--headless=new')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--disable-dev-sh-usage')
        options.add_argument('--incognito')

        driver = webdriver.Chrome(options=options)
        driver.get(base_url)

        accept_cookies = driver.find_element(
            By.XPATH, '//*[@id="termly-code-snippet-support"]/div/div/div/div/div/div[2]/button[2]')
        accept_cookies.click()
        time.sleep(3)

        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(5)
        # soup = BeautifulSoup(driver.page_source, 'html.parser')

        return driver

    def get_page_content(self, soup):
        self.soup = soup

        products_info_content = soup.find_all(
            'div', class_='product-card__content')

        return products_info_content

    def get_page_price(self, soup):
        self.soup = soup
        products_info_price = soup.find_all('div', class_='product-card__data')

        return products_info_price

    def get_product_name(self, products_info_content):
        self.products_info_content = products_info_content

        product_name = []

        for product in range(len(products_info_content)):
            name_p = products_info_content[product].find_all('p')[0]
            alcohol_name = name_p.contents[0].strip()
            product_name.append(alcohol_name)
        return product_name

    def get_product_alcohol_percent(self, products_info_content):
        self.products_info_content = products_info_content

        products_alcohol_percent = []

        for product in range(len(products_info_content)):
            alcohol_p = products_info_content[product].find_all('p')[1]
            alcohol_percent_str = alcohol_p.contents[0].strip()
            start = alcohol_percent_str.find('/')
            end = alcohol_percent_str.find('%')
            alcohol_percent = alcohol_percent_str[start+2:end]
            products_alcohol_percent.append(alcohol_percent)

        return products_alcohol_percent

    def get_product_alcohol_capacity(self, products_info_content):
        self.products_info_content = products_info_content

        products_alcohol_capacity = []

        for product in range(len(products_info_content)):
            alcohol_p = products_info_content[product].find_all('p')[1]
            alcohol_capacity_str = alcohol_p.contents[0].strip()
            start = 0
            end = alcohol_capacity_str.find('/')
            alcohol_capacity = alcohol_capacity_str[start:end-1]
            products_alcohol_capacity.append(alcohol_capacity)

        return products_alcohol_capacity

    def get_product_price(self, products_info_price):
        self.products_info_price = products_info_price

        product_price = []

        for product in range(len(products_info_price)):
            alcohol_p = products_info_price[product].find_all('p')[0]
            alcohol_price = alcohol_p.contents[0].replace('£', '').strip()
            product_price.append(alcohol_price)

        return product_price

    def create_df(self, names, alcohol_capcity, alcohol_percent, price):
        self.names = names
        self.alcohol_capcity = alcohol_capcity
        self.alcohol_percent = alcohol_percent
        self.price = price

        original_df = pd.DataFrame(names, columns=['Product_Name'])
        original_df['Alcohol_Percent'] = alcohol_percent
        original_df['Alcohol_Capcity'] = alcohol_capcity
        original_df['Alcohol_Price'] = price

        return original_df

    def insert_to_df(self, original_df, new_df):
        self.original_df = original_df
        self.new_df = new_df

        original_df = original_df._append(
            new_df, ignore_index=True, verify_integrity=True)

        return original_df

    def get_links(self, url='https://www.thewhiskyexchange.com/'):

        self.url = url

        # Generate a BeautifullSoup object called soup
        url = url
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')

        # Collect all the html objects of type 'a'
        a_tags = soup.find_all('a', class_='subnav__link')

        links_list = []

        # Collect all the hyper links of the webpage.
        for link in a_tags:
            links_list.append(link.get('href'))

        relevant_links = []

        # Iterate through the links and filter only the relevant ones that showcase a type of whiskey.
        for link in links_list:
            if link is not None and '/c/' in link and 'whisky' in link and '?' not in link:
                relevant_links.append(link)

        return relevant_links

    def scrape_whisky(self, url='https://www.thewhiskyexchange.com', number_of_pages=None):

        self.url = url
        self.number_of_pages = number_of_pages
        df = pd.DataFrame()
        # Creating a scraper object
        s = whisky_data_scraping()

        # Generating the relevant links to scrape data from
        links = s.get_links()

        # Iterating throught each link
        for link in links:

            try:
                driver = s.scrape_html(base_url=url + link + '?psize=120')

                # For each page in each link, generate a DataFrame of whiskey related data
                for page in range(0, number_of_pages):
                    # soup = s.scrape_html(
                    #     base_url=url + link + '?pg=', page=page+1)
                    soup = BeautifulSoup(driver.page_source,'html.parser')

                    content_html = s.get_page_content(soup)
                    price_html = s.get_page_price(soup)

                    names = s.get_product_name(content_html)
                    alcohol_amount = s.get_product_alcohol_capacity(content_html)
                    alcohol_percent = s.get_product_alcohol_percent(content_html)
                    price = s.get_product_price(price_html)

                    # Create a new DataFrame for the first page of each whiskey type
                    if page == 0:
                        data = s.create_df(
                            names, alcohol_amount, alcohol_percent, price)

                    # Insert to an existing DataFrame new data.
                    data = s.insert_to_df(data,s.create_df(
                            names, alcohol_amount, alcohol_percent, price))
                    
                    value_end = int(soup.find('span', class_='paging-count__value js-paging-count__value--end').text)
                    value_total = int(soup.find('span', class_='paging-count__value js-paging-count__value--total').text)

                    if value_end < value_total:
                        show_more = driver.find_element(
                            By.XPATH, '//*[@id="content"]/section[4]/div[2]/nav/a')
                        show_more.click()
                        time.sleep(3)
                    else:
                        break
                driver.close()
            except:
                print('Error with the link: {}'.format(link))
            # Export data for each whiskey type to a seperate CSV file
            finally:
                # start_location = link.rfind('/')+1
                # end_location = len(link)
                # data.to_csv(link[start_location:end_location] + '.csv')
                df = df._append(data, ignore_index=True)

        return df
