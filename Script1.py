'''
# Assignment title: Final Project- Web-scraping Weather Forecast
# Name: Zhen Liu and Sarah Lerman-Sinkoff
# Date: 10/04/2019
# Description: The script web-scrapes the weather.gov website to extract the 5-Day weather forecast for a given location
# time: 3 hours
# Inputs: Latitude & Longitude in Decimal Degrees
# Outputs: 5-Day Weather Forecast
'''

# import required libraries
import requests
from bs4 import BeautifulSoup

# List to store response
forecast = []

## Provide the latitude and longitude for the location you would like to check the forecast for
## Lat/lon in decimal degrees provided for Worcester, MA
#get the latitude and longitude from the keyboard
lat=str(input("Please enter the latitude:"))
lon=str(input("Please enter the longitude:"))


# Create url for the requested location through string concatenation
url = 'https://forecast.weather.gov/MapClick.php?lat='+lat+"&lon="+lon
# Check if the URL exists
# print url

# Send request to retrieve the web-page using the get() function from the requests library
# The page variable stores the response from the web-page
page = requests.get(url)

# Create a BeautifulSoup object with the response from the URL
# Access contents of the web-page using .content
# html_parser is used since our page is in HTML format
soup=BeautifulSoup(page.content,"html.parser")

# Locate elements on page to be scraped
# findAll() locates all occurrences of div tag with the given class name
# stores it in the BeautifulSoup object
weather_forecast = soup.findAll("li", {"class": "forecast-tombstone"})

# Loop through the BeautifulSoup object to extract text text from every class instance using .text
# Store results in a list
for i in weather_forecast:
    i = i.text
    forecast.append(i)

# Print list to remove unicode characters
for day in forecast:
    # if(' then' not in day):
    list_day=day.split('\n')
    # day.replace('then',' then')
    if (list_day[3].find(' then')<0):
      list_day[3]=list_day[3].replace('then',' then')
    if (list_day[3].find(' and')<0):
      list_day[3]=list_day[3].replace('and',' and')
    i=0
    str1=""
    # we find that the capital letter which does not preserve its space has the same characteristic. Like "yS" in "MostlySun", the letter in upper case is followed a letter in lower case. So, we go through the whole sentence to find the letter which have this characteristic, and put a space before the letter in upper case.
    for i in range(len(list_day[3])-1):
      if(list_day[3][i+1].isupper() and list_day[3][i].islower()):
        str1=str1+list_day[3][i]+' '
      else:
        str1=str1+list_day[3][i]
    str1=str1+"F"
    list_day[3]=str1
    list_day[3]=list_day[3].replace(' Low',', Low')
    list_day[3]=list_day[3].replace(' High',', High')
    list_day[2]=list_day[2].replace('Night',' Night')
    # Stardard Output
    print list_day[2].upper()
    print list_day[3].upper()
    print("\n")
