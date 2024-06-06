import json
import argparse
import requests
import os
import subprocess

#Load values from env file
from dotenv import load_dotenv

# MongoDB connections using PyMongo
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError

# Load environment variables from .env
load_dotenv()

# Retrieve the current version from environment variable
CURRENT_VERSION = os.getenv("VERSION", "0.0.1")

# Custom type function to convert input to lowercase
def lowercase_choice(value):
    return value.lower()

def get_services():
    """Retrieve service choices from the environment variable."""
    services = os.getenv('SERVICE_TYPES')
    if services:
        return services.split(',')
    else:
        raise ValueError("Error: 'SERVICE_TYPES' environment variable not set.")

def format_services(services):
    """Format service choices as a bullet-point list."""
    return "\n".join([f"  - {service}" for service in services])

def parse_arguments():
    parser = argparse.ArgumentParser(description="Secret Validator Tool",formatter_class=argparse.RawTextHelpFormatter)

    # Retrieve choices from environment variable
    services = get_services()
    formatted_services = format_services(services)
    
    parser.add_argument("-service", type=lowercase_choice, choices=services, required=True, help=f"Service / SecretType to validate secrets.\nSupported services:\n{formatted_services}")
    parser.add_argument("-secret", required=True, help=f"Pass Secrets to be validated")
    parser.add_argument('-r', '--response', action='store_true', help=f"Prints Active/ InActive upon validating secrets.")

        # Adding version argument
    parser.add_argument(
        '-v', 
        '--version', 
        action='version', 
        version=f'Secret Validator Tool version {CURRENT_VERSION}', 
        help='Show the version of this tool and exit.'
    )
    
    # Adding update argument
    parser.add_argument(
        '--update',
        action='store_true',
        help='Update the tool to the latest version.'
    )

    return parser.parse_args()

# Reuse session for multiple requests
requests.packages.urllib3.disable_warnings()
session = requests.Session()

def update_tool():
    """Update the tool to the latest version."""
    try:
        subprocess.run(["pip", "install", "--upgrade", "your_package_name"], check=True)
        print("Tool updated to the latest version.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to update the tool: {e}")

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
                    return "InActive"
                else:
                    return response_data.text
    except requests.HTTPError as e:
        if response:
            return "InActive"
        else:
            return e.response.text
    except requests.RequestException as e:
        return str(e.response.text)

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

def validate_teams_webhook(webhook_url, response):
    """Validate Teams webhook URL."""
    payload = {'text': ''}
    headers = {'Content-Type': 'application/json'}
    
    try:
        response_data = requests.post(webhook_url, json=payload, headers=headers)
        response_body = response_data.text

        if response_data.status_code == 400:
            if 'Text is required' in response_body:
                if response:
                    return "Active"
                else:
                    return "Teams webhook URL validation successful!"
            else:
                if response:
                    return "InActive"
                else:
                    return f"Unexpected response body: {response_body}"
        elif response_data.status_code < 200 or response_data.status_code >= 500:
            if response:
                return "InActive"
            else:
                return f"Unexpected HTTP response status: {response_data.status_code}"
        else:
            if response:
                return "InActive"
            else:
                return "Unexpected error"
    except requests.exceptions.RequestException as e:
        if response:
            return "InActive"
        else:
            return str(e)

def validate(service, secret, response):
    if service == 'mongodb':
        return validate_mongodb(secret, response)
    elif service == 'teams_webhook':
        return validate_teams_webhook(secret, response)
    else:
        return validate_http(service, secret, response)

def main(args=None):  
    if args is None:
        args = parse_arguments()

    if args.update:
        update_tool()
        return        

    try:
        # Call the validate function with provided arguments
        result = validate(args.service, args.secret, args.response)
        print(result)
    except Exception as e:
        print(f"Error: {e}")
