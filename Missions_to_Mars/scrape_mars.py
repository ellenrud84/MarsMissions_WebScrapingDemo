# import dependencies:
from bs4  import BeautifulSoup
import pymongo
from splinter import Browser
import time
import re
import pandas as pd

def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)

def scrape_info():
    browser = init_browser()
    mars_data={}
    
    # PART 1: MARS NEWS
    
    # define url:
    url= "https://mars.nasa.gov/news/"

    # Go to page with browser:
    browser.visit(url)
    html=browser.html
    # Create BeautifulSoup object; parse with 'lxml'
    soup = BeautifulSoup(html, 'html.parser')
    time.sleep(3)
    # results are returned as an iterable list
    results = soup.find_all(class_='slide')
    for result in results:
        # Identify and return title 
        news_title = result.find(class_="content_title").text
        # Identify and return news paragraph
        news_p = result.div.div.div.text


    #PART 2: MARS ROVER IMAGES:
    # navigate to page using browser
    img_url='https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    base_url='https://www.jpl.nasa.gov'
    browser.visit(img_url)
    # find and click button for full image
    button=browser.find_by_id('full_image')
    button.click()
    # initialize beautiful soup object for page
    html= browser.html
    soup = BeautifulSoup(html, 'html.parser')
     # scrape images & links
    img_link=browser.find_by_id('full_image')['data-fancybox-href']
    featured_image_url= base_url+img_link


    # PART 3: MARS WEATHER:
    weather_url='https://twitter.com/marswxreport?lang=en'
    browser.visit(weather_url)
    time.sleep(3)
    # initialize beautiful soup object for page
    i=1
    while i<5:
        try:
            html= browser.html
            soup=BeautifulSoup(html, 'html.parser')
            # scrape weather
            mars_weather=str(soup.find_all(text=re.compile("InSight"))[0])
            break
        except:
            i=i+1
            continue

    # PART 4:MARS FACTS:
    # define url
    mars_facts_url='https://space-facts.com/mars/'
    # read tableinto pandas
    table= pd.read_html(mars_facts_url)
    # revise table
    df=table[0]
    df.columns=[['parameters', 'values']]
    # convert to html and clean up
    mars_data_table= df.to_html(classes= 'table-striped')


    # PART 5: MARS HEMISPHERES:
    hem_url='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hem_url)
    # initialize beautiful soup object for page
    html= browser.html
    soup=BeautifulSoup(html, 'html.parser')
    time.sleep(3)
    # scrape hemispheres
    results=soup.find_all('div', class_="item")

    hemispheres= []
    # loop to get each image link and title
    for result in results:
        link= result.find('a')['href']
        full_link= 'https://astrogeology.usgs.gov'+link
        title=result.find('h3').text 
        # go to the full link
        browser.visit(full_link)
        # initialize beautiful soup object for page
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        # scrape page
        results=soup.find('div', class_='downloads')
        image_url = results.find("a")["href"]
        # append item dictionary to hemispheres list
        hemispheres.append({'title':title, 'img_url':image_url})
    
    # PART 6: Add all scraped data to mars_data dictionary:
    mars_data['news_title']= news_title
    mars_data['news']=news_p
    mars_data['featured_image_link']=featured_image_url
    mars_data['current_weather']=mars_weather
    mars_data['facts']=mars_data_table
    mars_data['hemisphere_images']=hemispheres
    
    # Close the browser after scraping
    browser.quit()

    # FUNCTION RETURN
    return mars_data

