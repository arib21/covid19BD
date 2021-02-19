import pyrebase, json

firebaseConfig = {
	'apiKey': "AIzaSyDBVMlO16x0TJUCyjyNqN5MIUdwq2AoLgA",
	'authDomain': "covid19-tracker-bd.firebaseapp.com",
	'databaseURL': "https://covid19-tracker-bd-default-rtdb.firebaseio.com/",
	'projectId': "covid19-tracker-bd",
	'storageBucket': "covid19-tracker-bd.appspot.com",
	'messagingSenderId': "372162077448",
	'appId': "1:372162077448:web:48f198f2d9c598c540c2bd"
}

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

def getData(date_, month, year, type_="all/cured/deaths/infected/tested"):
	if date_ < 10:
		date_ = f"0{date_}"

	key = f"{date_} {month} {year}"
	value_ = db.child(key).get().val()

	if type_ == "all":
		if value_ == None:
			print("Error: The data for the date you entered is not in our database!")
		else:
			return json.dumps(value_, indent=2)
	
	if type_ == "cured":
		hrs_ = value_.get("Cured (24hrs)")
		total_ = value_.get("Cured (Total)")
		return hrs_, total_
	
	if type_ == "deaths":
		hrs_ = value_.get("Deaths (24hrs)")
		total_ = value_.get("Deaths (Total)")
		return hrs_, total_
	
	if type_ == "infected":
		hrs_ = value_.get("Infected (24hrs)")
		total_ = value_.get("Infected (Total)")
		return hrs_, total_
	
	if type_ == "tested":
		hrs_ = value_.get("Tested (24hrs)")
		total_ = value_.get("Tested (Total)")
		return hrs_, total_
