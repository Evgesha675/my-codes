import requests

# Define your authentication credentials
auth_data = {
    "username": "tetenkinevgenij@gmail.com",
    "password": "BigBlack228DjoDjo"
}

# Make a POST request to authenticate and get a session token
auth_response = requests.post('https://bki.forlabs.ru/lm-vendor/tip', json=auth_data)

# Check if the authentication request was successful (status code 200)
if auth_response.status_code == 200:
    # Extract the session token from the authentication response
    session_token = auth_response.json().post('session_token')
    
    # Make a GET request to the desired endpoint with the session token
    headers = {'Authorization': f'Bearer {session_token}'}
    response = requests.post('https://bki.forlabs.ru/app/profile/user', headers=headers)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Get all the headers from the response
        headers = response.headers
    
        # Print each header
        for header, value in headers.items():
            print(f"{header}: {value}")
    else:
        print(f"Request failed with status code: {response.status_code}")
else:
    print(f"Authentication request failed with status code: {auth_response.status_code}")
