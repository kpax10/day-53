# Web Scraping and Data Entry Capstone Project Requirements

Set up your own Google Form

First, you need to create a new form in Google Forms.

1. Go to https://docs.google.com/forms/ and create your own form:

2. Add 3 questions to the form, make all questions "short-answer":

3. Click send and copy the link address of the form. You will need to use this in your program.


Go to our Zillow-Clone Website

4. Go to https://appbrewery.github.io/Zillow-Clone/ and see how the website is structured. This is where you'll be scraping the data from:
BeautifulSoup Requirements

    Use BeautifulSoup/Requests to scrape all the listings from the Zillow-Clone web address (Step 4 above).


    Create a list of links for all the listings you scraped. e.g.


    Create a list of prices for all the listings you scraped. e.g.

Clean up the strings, by removing any "+" symbols and other information so that you are only left with a dollar price. The price should look like "$1,234" instead of "$1,234+ /mo"


    Create a list of addresses for all the listings you scraped. e.g.

Clean up the address data as well. Remove any newlines, pipe symbols |, and unnecessary whitespace.


Selenium Requirements


    Use Selenium to fill in the form you created (step 1,2,3 above). Each listing should have its price/address/link added to the form. You will need to fill in a new form for each new listing. e.g.

    Once all the data has been filled in, click on the "Sheet" icon to create a Google Sheet from the responses to the Google Form. You should end up with a spreadsheet with all the details from the properties.

Objective 🎯

You should end up with a spreadsheet that looks something like this.
Resources for this lecture

