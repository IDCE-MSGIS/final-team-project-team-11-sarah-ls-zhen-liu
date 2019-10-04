## Final Project: Script 1
### Web-scraping Weather Forecast Information with Python
In this lab, you will work with a script that scrapes the 5-day weather forecast from the National Weather Service website. The script extracts information from multiple elements listed under the same class name using the BeautifulSoup library. 

- Copy the **NWS_WeatherForecast.py** file and paste it into the online Python compiler: https://repl.it/languages/python
Make sure you are using Python version 2.7. You can check the Python version in the compiler window on the right.

- Read the description and comments in the script to understand the purpose of the script

- Run the script. You will see some packages being installed in the compiler window when you run it for the first time.

- The script returns the 5-day forecast for Worcester, MA (Lat: 42.2634, Lon: -71.8022) with the latitude and longitude information provided. Using the latitude and longitude values, it generates the following URL through string concatenation: https://forecast.weather.gov/MapClick.php?lat=42.2634&lon=-71.8022

- Open this URL in a Firefox or Chrome browser. Locate the information that is being outputted in our script. Right click on this and select the Inspect Element option. This will launch the Inspector window that helps locate different elements on the page.

- Notice that all forecast containers in this section are located in the _forecast-tombstone_ class inside the _li_ tag. In order to scrape multiple elements listed under the same class name, we utilize the _findAll()_ function from BeautifulSoup. The tag and class names are required arguments for this function.

### Edit the NWS_ WeatherForecast.py script to add the following functionality:
1. Take latitude and longitude values as inputs in decimal degrees from user

2.	Convert the latitude and longitude values to strings to generate the URL for the selected location. Pass this URL as an argument in the _get()_ request.

3.	The returned forecast information did not preserve its spacing during the scraping process. Using the _replace()_ function, fix any spacing issues with the output

4.	Convert the final output to uppercase

Remember to update the Script1.py file to include comments and documentation in your script to tell me what it’s doing!

## Final Project: Script 2
### Your Chosen Assignment
For this script, you will complete the assignment that you have proposed, which involves modifying a previous exercise. Remember to update the Script2.py file to include comments and documentation in your script to tell me what it’s doing!

## Final Project: Documentation

Script 1:

The purpose of this script is to extract weather information from the National Weather Service for a latitude/longitude input given by users. The information includes 5-day temperature and precipitation forecasts.

The original script had the latitude/longitude built in; we edited the script so that users could provide their own lat/long values. Another change we made is that when the script scrapes the text descriptions, it does not preserve spacing-- the words are upper case followed by a character in lower case. To restore the spacing, we locate all of the capital letters, and insert spacing before each of them. Additionally, we account for the few cases where we would like to insert commas before the spaces, such as “CHANCE SHOWERS, LOW”. Finally, we add spaces for the words “and” and “then”, which do not preserve their spacings either. We locate them, and add a space before them using the replace function.

One challenge with both of these instances is that when we insert a space, we alter the index of the string. To account for this, we create a new index shared by both strings: we define an empty string, put the correct characters into the string, and replace the original string with the correct one.

There is a great possibility that we will apply something like this in the future. When we need to get location names from big data and want them in the same form, we need to use this method to get ideal data. Commas and spacing change the output of a large variety of functions, including those in popular GIS programs such as ArcMap. In ArcMap, if we wanted to join certain fields, we would need to make sure the data were identical, and commas and spaces could interrupt the join.

Script 2:

This script has two different purposes: converting a given temperature from the user into centigrade, and giving clothing recommendations based on the temperature they input, and the quality of clothing they are interested in. A real-life use of this script could be for international travelers on shopping trips, staying in apartment buildings where it’s difficult to go outside to tell the temperature. 

The process of the script was fairly smooth -- we first created the overall structure for the two programs (the While(True) loop), and built out the different temperature options for the clothing program (built on the “it is hot!” lab). Then, we coded the different options for the clothing recommendations - this was also smooth, as it was essentially a nested copy of the elif loop from the lab.
The one major edit we made after this process was separating the temperature input from the program menu options. Initially, we had the temperature input as just one of the menu options, alongside clothing recommendations and conversion. The code used to just send you back to the beginning if you selected option 2 or 3 before option 1 (input the temperature). Realizing this was odd, one of us created a pull request in github to give an initial input for temperature, followed by the second menu options. The other person edited the code, re-inserting a “change the temperature” option to the second menu, so that users could go through either the conversion or clothing recommendation loops without needing to exit the whole program if they wanted to change the temperature. Github was a great help!

