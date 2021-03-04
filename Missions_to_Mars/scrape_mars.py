pip3 install selenium
pip3 install splinter

    # Declare Dependencies
    from bs4 import BeautifulSoup
    from splinter import Browser
    import pandas as pd
    import requests
   
# Initialize browser
def init_browser(): 
    
    "# Choose the executable path to driver \n",
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path)

    # Create Mission to Mars global dictionary that can be imported into Mongo
    mars_info = {}

    def scrape():
        
    # Visit the mars nasa news site\n
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
  
     # Create a Beautiful Soup object
    
    # HTML Object
    html = browser.html
    
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    
    # Retrieve the latest element that contains news title and news_paragraph
    news_title = soup.find('div', class_ ='list_text').find('a').text
    news_paragraph = soup.find('div', class_ ='article_teaser_body').text
    
    # Display scrapped data
    # print(news_title)
    # print(news_paragraph)
   
    #JPL Mars Space Images
    #Use splinter to find the url for the current featured image
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path)
    mars_image_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    browser.visit(mars_image_url)
   
    # Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url 
    #string to a variable called `featured_image_url`
    full_image_button = browser.find_by_text(" FULL IMAGE")
    full_image_button.click()
  
    # Parse Results HTML with BeautifulSoup
    html_image = browser.html
    image_soup = BeautifulSoup(html_image, "html.parser")
   
    # Find the image url to the full size `.jpg` image
    featured_image_url = image_soup.select_one("img.fancybox-image").get("src")
    featured_image_url

    # Save a complete url string for this image
    featured_image_url = f"https://www.jpl.nasa.gov{featured_image_url}"
    # print(featured_image_url)
   
    #Mars Facts
    # Visit the Mars Facts webpage [here](https://space-facts.com/mars/) and use Pandas to scrape the table 
    # containing facts about the planet including Diameter, Mass, etc
    mars_facts_df = pd.read_html("https://space-facts.com/mars/")[0]
    #print(mars_facts_df)
   
    # Visit the Mars Facts webpage [here](https://space-facts.com/mars/) and use Pandas to scrape the table
    # containing facts about the planet including Diameter, Mass, etc
    mars_facts_df = pd.read_html("https://space-facts.com/mars/\")
    #print(mars_facts_df)
   
    # Visit the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars)
    # to obtain high resolution images for each of Mar's hemispheres.
    executable_path = {"executable_path": "chromedriver.exe"}
    browser = Browser("chrome", **executable_path, headless=False)
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)
  
    hemisphere_image_urls = []
    
    # Get a List of All the Hemispheres
    links = browser.find_by_css("a.product-item h3")
    for item in range(len(links)):
     hemisphere = {}

    # Loop each element
    browser.find_by_css("a.product-item h3")[item].click()
   
    # Save both the image url string for the full resolution hemisphere image, and the Hemisphere title \n",
    # containing the hemisphere name. Use a Python dictionary to store the data using the keys `img_url` \n",
    # and `title`.\n",
    sample_element = browser.find_link_by_text("Sample").first
     # Get hemisphere image url\n",
    hemisphere["img_url"] = sample_element["href"]
   
    # Get hemisphere title
    hemisphere["title"] = browser.find_by_css("h2.title").text",
   
    # Append the dictionary with the image url string and the hemisphere title to a list. This list will \n",
    # contain one dictionary for each hemisphere.\n",
    hemisphere_image_urls.append(hemisphere)"
    
    browser.back()

    # Pint the array hemisphere_image_urls
    hemisphere_image_urls
    browser.quit()

    return  mars_info 

  