from astral import LocationInfo
from astral.sun import sun
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo  # For timezone conversion
from geopy.geocoders import Nominatim
# Function to calculate sunrise & sunset for the next 7 days
def get_sun_times(lat, lon, date_str):
    city = LocationInfo(name="New Delhi", region="India", timezone="Asia/Kolkata",latitude=lat, longitude=lon)
    
    # Convert input date string to datetime
    base_date = datetime.strptime(date_str, "%Y-%m-%d")

    print(f"Sunrise & Sunset Times for ({lat}, {lon}) in IST")
    print("="*40)
    
    for i in range(7):  # Next 7 days
        current_date = base_date + timedelta(days=i)
        s = sun(city.observer, date=current_date,tzinfo=ZoneInfo("Asia/Kolkata"))
        
        sunrise_time = s["sunrise"].strftime("%H:%M:%S")
        sunset_time = s["sunset"].strftime("%H:%M:%S")
        
        print(f"{current_date.date()} → Sunrise: {sunrise_time}, Sunset: {sunset_time}")

# Example Usage
# latitude = 28.6139  # Change to your location
# longitude = 77.2090  # Change to your location
geolocator = Nominatim(user_agent="geoapi")

# Enter city or place name
location_name=input("Enter the location name (e.g., New Delhi, India):")
location = geolocator.geocode(location_name)

# Print results
if location:
    print(f"Location: {location.address}")
    print(f"Latitude: {location.latitude}, Longitude: {location.longitude}")
else:
    print("Location not found.")
today_date = input("Enter the date in YYYY-MM-DD format: ")
 # Input date (YYYY-MM-DD)
get_sun_times(location.latitude, location.longitude, today_date)