from googlemaps import Client
api_key = 'AIzaSyCfC7QUUsgZ9oQhQTE2gE7Qx-l8uj0swlk';
gmaps = Client(api_key)
address = 'Constitution Ave NW & 10th St NW, Washington, DC'
lat, lng = gmaps.geocode(address)
print lat, lng