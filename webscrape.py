from robobrowser import RoboBrowser
from twilio.rest import TwilioRestClient
import sys
import os

def login():
	#login
	url = "https://website_here.com"
	browser.open(url)
	form = browser.get_form()

	#user info
	form["email"].value = "name@server.com"
	form["password"].value = "password"

	browser.submit_form(form) #submit form

browser = RoboBrowser()
login()
spaceFound = False
while(spaceFound == False): #refresh page
	#open profile page
	browser.open("https://website_here.com")

	#save page source to string
	pageSource = str(browser.parsed)
	#print(pageSource)

	capStr = "/ 1600"
	pos = pageSource.find(capStr)
	
	try:
		regUsers = pageSource[pos - 5:pos - 1]
		spacesOpen = int(regUsers)
		spacesOpen = spacesOpen - 1600
		spacesOpen = abs(spacesOpen)

		if spacesOpen > 0:
			print("ALERT!!! MESSAGE")
			print(spacesOpen)
			print(" spaces available.")
		
			#send sms message
			account_sid = "IDNUMBER"
			auth_token = "TOKENAUTH"
			client = TwilioRestClient(account_sid, auth_token)
			message = client.messages.create(to="+1231234567", from_="+1231234567", body="ALERT!!! Message!")
			message = client.messages.create(to="+1231234567", from_="+1231234567", body="ALERT!!! Message!")
			spaceFound = True

		else:
			clear = lambda: os.system("cls")
			clear()
			sys.stdout.write(str(spacesOpen))
			print(" spaces.")
			
	except: #failed log back in
		login()
