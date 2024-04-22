import requests

# API endpoint
url = "https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/EC4M7RF"

# Headers to identify as a browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

# Fetch data from the API
response = requests.get(url, headers=headers)

# Check if request was successful
if response.status_code == 200:
    data = response.json()
    
    # Extract relevant information
    restaurants = data.get('restaurants', [])
    
    for restaurant in restaurants:
        name = restaurant.get('name', 'N/A')
        address = restaurant.get('address', {}).get('firstLine', 'N/A')
        cuisine = restaurant.get('cuisineTypes', [])
        cuisine = ', '.join([cuisine_type.get('name', 'N/A') for cuisine_type in cuisine])
        rating = restaurant.get('rating', {}).get('average', 'N/A')
        
        print("Restaurant Name:", name)
        print("Address:", address)
        print("Cuisine:", cuisine)
        print("Rating:", rating)
        print("------------------------------------------")
else:
    print("Failed to fetch data from the API. Status code:", response.status_code)


