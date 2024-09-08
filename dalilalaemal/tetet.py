import requests
import re

def extract_coordinates_or_address(short_url, api_key):
    try:
        # إرسال طلب إلى الرابط المختصر
        response = requests.get(short_url, allow_redirects=True)
        
        # الحصول على الرابط الكامل بعد إعادة التوجيه
        full_url = response.url
        
        # طباعة الرابط الكامل لمراجعة النتيجة
        print(f"Full URL: {full_url}")
        
        # محاولة استخراج الإحداثيات من الرابط
        coordinates = re.search(r'@(-?\d+\.\d+),(-?\d+\.\d+)|3d(-?\d+\.\d+)!4d(-?\d+\.\d+)|(\d+\.\d+),(\d+\.\d+)', full_url)
        
        if coordinates:
            # في حالة العثور على الإحداثيات
            if coordinates.group(1):
                latitude = coordinates.group(1)
                longitude = coordinates.group(2)
            elif coordinates.group(3):
                latitude = coordinates.group(3)
                longitude = coordinates.group(4)
            else:
                latitude = coordinates.group(4)
                longitude = coordinates.group(5)
            return latitude, longitude
        else:
            # إذا لم تكن هناك إحداثيات، استخدام Google Maps API لاستخراج الإحداثيات بناءً على العنوان
            return get_coordinates_from_api(full_url, api_key)
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None

def get_coordinates_from_api(address, api_key):
    base_url = 'https://maps.googleapis.com/maps/api/geocode/json'
    params = {
        'address': address,
        'key': api_key
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    
    if data['status'] == 'OK':
        location = data['results'][0]['geometry']['location']
        return location['lat'], location['lng']
    else:
        return None, None

# Example usage
api_key = 'YOUR_GOOGLE_MAPS_API_KEY'
short_url = "https://maps.app.goo.gl/czTxQFTXVD35QypG8"
lat, lng = extract_coordinates_or_address(short_url, api_key)

if lat and lng:
    print(f"Latitude: {lat}, Longitude: {lng}")
else:
    print("Could not extract coordinates.")
