import json
import argparse
import requests
import os

# MongoDB connections using PyMongo
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError

# Custom type function to convert input to lowercase
def lowercase_choice(value):
    return value.lower()

def parse_arguments():
    parser = argparse.ArgumentParser(description="Secret Validator Tool")
    parser.add_argument("-service", type=lowercase_choice, choices=["snykkey", "sonarcloud_token", "npm_access_token", "huggingface", "pagerduty_api_key", "sentry_auth_token", "mongodb"], required=True, help="Service to validate secret for")
    parser.add_argument("-secret", required=True, help="Secret to validate")
    parser.add_argument('-r', '--response', action='store_true', help='Print simple response (status/true/false).')
    return parser.parse_args()

# Reuse session for multiple requests
requests.packages.urllib3.disable_warnings()
session = requests.Session()

def get_headers(service, secret):
    headers_map = {
        'snykkey': {'Authorization': f'token {secret}'},
        'sonarcloud_token': {'Authorization': f'Bearer {secret}'},
        'npm_access_token': {'Authorization': f'Bearer {secret}'},
        'huggingface': {'Authorization': f'Bearer {secret}'},
        'pagerduty_api_key': {'Authorization': f'Token {secret}'},
        'sentry_auth_token': {'Authorization': f'Bearer {secret}'}
        # Add more services here as needed
    }
    return headers_map.get(service, {})

def get_service_url(service):
    current_dir = os.path.dirname(os.path.dirname(__file__))
    urls_path = os.path.join(current_dir, 'urls.json')

    with open(urls_path, 'r') as f:
        urls = json.load(f)

    service_url = urls.get(service)

    if not service_url:
        raise ValueError(f"Error: URL for service {service} not found.")

    return service_url

def validate_http(service, secret, response):
    headers = get_headers(service, secret)
    url = get_service_url(service)

    try:
        with session.get(url, headers=headers, verify=False) as response_data:
            response_data.raise_for_status()  # Raise an HTTPError for bad responses

            if response_data.status_code == 200:
                if response:
                    return "Active"
                else:
                    try:
                        json_response = response_data.json()
                        return json.dumps(json_response, indent=4)
                    except json.JSONDecodeError:
                        return "Response is not a valid JSON."
            else:
                if response:
                    return "Inactive"
                else:
                    return response_data.text
    except requests.HTTPError as e:
        if response:
            return "Inactive"
        else:
            return e.response.text
    except requests.RequestException as e:
        return str(e)

def validate_mongodb(connection_string, response):
    """Validate MongoDB connection string."""

    try:
        client = MongoClient(connection_string, serverSelectionTimeoutMS=5000)
        # Attempt to retrieve server information to force a connection check
        server_info = client.server_info()
        if response:
            return "Active"
        else:
            return server_info       

        client.close()
    except (ConnectionError, ConnectionFailure) as e:
        if response:
            return "Inactive"
        else:
            return f"MongoDB connection string validation failed: {e}"

def validate(service, secret, response):
    if service == 'mongodb':
        return validate_mongodb(secret, response)
    else:
        return validate_http(service, secret, response)

def main(args=None):  
    if args is None:
        args = parse_arguments()
        
    try:
        # Call the validate function with provided arguments
        result = validate(args.service, args.secret, args.response)
        print(result)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
