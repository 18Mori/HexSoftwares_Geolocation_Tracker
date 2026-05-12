import requests, folium, webbrowser, os

def get_geolocation(ip=''):
    url = f"http://ip-api.com/json/{ip}"
    
    try:
        print(f"Fetching data for: {ip if ip else 'Your Current IP'}...")
        response = requests.get(url)
        data = response.json()
        
        if data['status'] == 'fail':
            print(f"Error: {data['message']}")
            return None
            
        return data
    except Exception as e:
        print(f"Connection Error: {e}")
        return None

def create_map(data):
    lat = data['lat']
    lon = data['lon']
    location_name = f"{data['city']}, {data['country']}"
    
    my_map = folium.Map(location=[lat, lon], zoom_start=12)
    
    folium.Marker(
        [lat, lon], 
        popup=location_name,
        tooltip="Click for details"
    ).add_to(my_map)
    
    # Save the map as an .html file
    file_name = "location_map.html"
    my_map.save(file_name)
    
    print(f"\nSuccess! Location found: {location_name}")
    print(f"Coordinates: {lat}, {lon}")
    print(f"Timezone: {data['timezone']}")
    print(f"Map saved as {file_name}")
    
    # Automatically open the map in your browser
    webbrowser.open('file://' + os.path.realpath(file_name))

if __name__ == "__main__":
    print("--- GEOLOCATION TRACKER --- \n")
    target_ip = input("Enter IP address(eg,'8.8.8.8') to track (or press Enter for your own): \n")
    
    geo_data = get_geolocation(target_ip)
    
    if geo_data:
        create_map(geo_data)