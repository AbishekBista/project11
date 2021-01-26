# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 11:07:21 2021

@author: Test
"""

#Review for a product

#scrapping data using selenium
from selenium import webdriver
from time import sleep

A = []
url = "https://www.etsy.com/listing/729276570/gold-link-choker-with-gold-coin-chain?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=sc_gallery-1-1&plkey=9bfaae31df87710a2a315c4d6e034754ebe9d7aa%3A729276570&bes=1";
browser = webdriver.Chrome("c:/chromedriver.exe")
browser.get(url)

button_Text = int(browser.find_element_by_xpath("//*[@id=\"reviews\"]/div[2]/nav/ul/li[5]/a").text.split("\n")[1]);


for j in range(0, button_Text):
                                     
    next_button = browser.find_element_by_xpath('//*[@id="reviews"]/div[2]/nav/ul/li[position() = last()]/a')
    
    for i in range(0,4):
        for records in browser.find_elements_by_id('review-preview-toggle-'+str(i)):
            A.append(records.text.strip())
                                 
    next_button.click()
    sleep(3)
browser.quit()    

#storing the reviews in a csv file
import pandas as pd

df = pd.DataFrame()

df['reviewText'] = A

df.to_csv('list_of_etsy_reviews.csv', index = False)


#storing the reviews in a sqlite database

import sqlite3 as sql

#open the connection

conn = sql.connect('etsy_reviews.db')

df.to_sql('reviews', conn, index = False)

new_df = pd.read_sql('SELECT * FROM reviews', conn)
