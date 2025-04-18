🌞 Sun Time Predictor Using Python ⏱🇮🇳

A Sun Time Predictor that calculates sunrise and sunset times for the next 6 days for any location across the globe! 🌍

🔧 Tech Stack & Libraries Used:

1. Astral – to calculate sunrise and sunset times based on geographical coordinates

2. Geopy – to convert place names into latitude and longitude

3. ZoneInfo – to convert UTC times into Indian Standard Time (IST)

📥 How It Works:

* The user inputs a location (like New Delhi, Tokyo, New York) and the current date.

* The program uses Geopy to fetch the latitude & longitude of the location.

* Using Astral, it calculates sunrise and sunset times for the next 6 days and today's also.

* Finally, it converts the output from UTC to IST (Asia/Kolkata) using Python’s ZoneInfo.

📈 Why I Built This: As a Python enthusiast, I was curious about how astronomical data like sunrise/sunset times can be programmatically predicted. This project helped me explore the integration of timezone handling, geolocation APIs, and astronomical calculations — all within a clean Python workflow.

✅ Features:

* Accurate sun timings for any city worldwide

* Easy input: Just location and date

* Results displayed in user-friendly format

* IST conversion handled efficiently using modern timezone support

💡Next Steps (Upcoming Ideas):

* Building a web-based UI for this tool using HTML/CSS & Flask

* Adding animated visuals for sunrise/sunset

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
About Astral Library

Astral is a python package for calculating the times of various aspects of the sun and moon.

It can calculate the following

Dawn

The time in the morning when the sun is a specific number of degrees below the horizon.

Sunrise

The time in the morning when the top of the sun breaks the horizon (assuming a location with no obscuring features.)

Noon

The time when the sun is at its highest point directly above the observer.

Midnight

The time when the sun is at its lowest point.

Sunset

The time in the evening when the sun is about to disappear below the horizon (asuming a location with no obscuring features.)

Dusk

The time in the evening when the sun is a specific number of degrees below the horizon.

Daylight

The time when the sun is up i.e. between sunrise and sunset

Night

The time between astronomical dusk of one day and astronomical dawn of the next

Twilight

The time between dawn and sunrise or between sunset and dusk

The Golden Hour

The time when the sun is between 4 degrees below the horizon and 6 degrees above.

The Blue Hour

The time when the sun is between 6 and 4 degrees below the horizon.

Time At Elevation

the time when the sun is at a specific elevation for either a rising or a setting sun.

Solar Azimuth

The number of degrees clockwise from North at which the sun can be seen

Solar Zenith

The angle of the sun down from directly above the observer

Solar Elevation

The number of degrees up from the horizon at which the sun can be seen

Rahukaalam

“Rahukaalam or the period of Rahu is a certain amount of time every day that is considered inauspicious for any new venture according to Indian Vedic astrology”.

Moonrise and Moonset

Like the Sun but for the moon

Moon Azimuth and Zenith

Also like the Sun but for the moon

Moon Phase

The phase of the moon for a specified date.

Astral also comes with a geocoder containing a local database that allows you to look up information for a small set of locations (new locations can be added).

Moon

The moon rise/set times can be obtained like the sun’s functions

Code:-

from astral import LocationInfo

city = LocationInfo("London", "England", "Europe/London", 51.5, -0.116)

import datetime

from astral.moon import moonrise

from astral.location import Location

dt = datetime.date(2021, 10, 28)

london = Location(city)

rise = moonrise(city.observer, dt)  # returns a UTC time

print(rise)

ouput

2021-10-28 22:02:00+00:00

About phases of moon 

http://moongazer.x10.mx/website/astronomy/moon-phases/ 

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////  
  
About Geopy Libraries  

Installation  
pip install geopy  

1. geopy is a Python wrapper.
It doesn't do geolocation itself — it sends a request to a geocoding service (like OpenStreetMap, Google Maps, Bing, etc.) and just parses the response.

By default, geopy uses OpenStreetMap's Nominatim service unless you specify another.

⚙️ Step-by-Step Workflow (Behind the Scenes)
🔹 Step 1: You type:  
geolocator = Nominatim(user_agent="myapp")  
location = geolocator.geocode("New Delhi")  
🔹 Step 2: It sends an HTTP request to this URL:    
https://nominatim.openstreetmap.org/search?q=New+Delhi&format=json  
This query is:  

* "New Delhi" (your input)

* plus parameters like format=json, optional country codes, etc.  

🔹 Step 3: Nominatim processes your query:  
Searches OpenStreetMap’s place index  

Tries to match "New Delhi" against its database of cities, regions, landmarks, etc.  

Picks the most relevant result  

🔹 Step 4: The response (in JSON):    
  {  
    "place_id": "XXXX",  
    "display_name": "New Delhi, Delhi, India",  
    "lat": "28.6138954",  
    "lon": "77.2090057",  
    ...  
  }  
🔹 Step 5: geopy parses this into a Python object:  
location.latitude  # → 28.6138954  
location.longitude # → 77.2090057  
location.address   # → "New Delhi, Delhi, India"  

🧠 Summary:  
geopy → sends query to Nominatim → gets JSON response → converts it into easy Python object.  
