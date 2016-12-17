from geopy.distance import vincenty
import requests


def get_distance(lat_orig, lng_orig, lat_des, lng_des):
	# Use the vincenty method (geopy.distance) to return the distance between two sets of coordinates. 
    
    # Args:
    #   lat_orig (float): latitude of origin
	#   lng_orig (float): longitude of origin
	#   lat_des (float): latitude of destination
	#   lng_des (float): longitude of destination

    # Return:
    #   nm (float): distance between coordinates in nautical miles
    #   mi (float): distance between coordinates in statute miles
    #   km (float): distance between coordinates in kilometers

	nm = vincenty((lat_orig, lng_orig),(lat_des, lng_des)).nm
	mi = vincenty((lat_orig, lng_orig),(lat_des, lng_des)).miles
	km = vincenty((lat_orig, lng_orig),(lat_des, lng_des)).kilometers
	return nm, mi, km 

def get_lat_lng(payload):
	# Use the requests module and Google API to return the latitude and longitude of a location.

    # Args:
    #   payload (str): of the format 'https://maps.googleapis.com/maps/api/geocode/json?address=COLUMBUS+OH+UNITED+STATES'
    
    # Return:
    #   lat (float): latitude
    #   lng (float): longitude

    response = requests.get(payload)
    resp_json_payload = response.json()
    lat = resp_json_payload['results'][0]['geometry']['location']['lat']
    lng = resp_json_payload['results'][0]['geometry']['location']['lng']
    return lat, lng