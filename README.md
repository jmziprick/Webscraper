# Webscraper

A basic script I made to scan a website for an opening to an event. The script is able to sign in to a profile on a web form and then scan the source of the page for a specific string of characters (which was the available openings to the event) and convert it to an int. If the int became greater than 0 it would use the Twilio API to send a text message to a couple of different phone numbers.
