# MARS INFO- WEB SCRAPING DEMO
In this demo, multiple sources are web scraped using the python library Beautiful Soup and combined into an informative 
web page about NASA's mission to Mars.

## Results: TODO ADD RESULTS AND CONCLUSIONS

## Methods:
### Technologies Used:
  * Splinter was used to navigate the sites when needed and BeautifulSoup was used to find and parse out the necessary data.
  * Pymongo was used for "CRUD" (Create, Read, Update, Delete) applications for the database. In this demo, the existing document is overwriten each time the "/scrape" url is visited and new data is obtained
  * Bootstrap was used to structure your HTML template.
  
###Step 1 - Scraping
Webs scraping is performed using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

A Jupyter Notebook file called mission_to_mars.ipynb was created and used to complete all scraping and analysis. The following outlines what is scraped:

1. NASA Mars News:  TODO Add website link
The NASA Mars News Site was scraped to collect the latest News Title and Paragraph Text. This text was assigned to variables that will be reference later.


2. JPL Mars Space Images - Featured Image: TO DO Add website link
Splinter was used to automatically navigate the site and find the image url for the current Featured Mars Image. This url string was assigned to a variable called featured_image_url.

3. Mars Weather: TODO Add link to Mars Weather Twitter Account
Splinter was used to automatically visit and navigate the Mars Weather twitter account. The latest Mars weather tweet was scraped from the page. The tweet text from the weather report was saved as a variable called mars_weather.

4.Mars Facts: TODO Add link to mars facts web page
Splinter was used to visit the Mars Facts webpage. Pandas was then used to scrape the table containing facts about the planet including Diameter, Mass, etc. The data was then converted to a HTML table string.

5. Mars Hemispheres: TO DO add link to Marks Hemispheres page
The USGS Astrogeology site was visited to obtain high resolution images for each of Mar's hemispheres.
In order to do this, Splinter/ Browser was used to automatically click each of the links to the hemispheres in order to find the image url to the full resolution image. Both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name were scraped. A Python dictionary was used to store the data using the keys img_url and title. This dictionary was then appended with the image url string and the hemisphere title to a list. This list contains one dictionary for each hemisphere.

### Step 2 - MongoDB and Flask Application:
1. MongoDB with Flask templating were used to create a new HTML page to display all of the information that was scraped from the URLs above.

2. The preliminary work in the Jupyter notebook was converted into a Python script called scrape_mars.py with a function called scrape() that executes all of the scraping code from above and returns one Python dictionary containing all of the scraped data.

3. Next, an app route called "/scrape" was created and programmed to import the scrape_mars.py script and call the scrape function. The return value from this script is stored in Mongo DB as a Python dictionary.

4. A root route,  "/"was create and programmed to query the Mongo database and pass the mars data into an HTML template to display the data.

5.A template HTML file called index.html was created. This file takes the mars data dictionary and displays all of the data in HTML elements. 




