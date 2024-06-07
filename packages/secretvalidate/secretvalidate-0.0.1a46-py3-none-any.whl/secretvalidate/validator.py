import argparse
import requests
import os

from secretvalidate.env_loader import get_secret_active, get_secret_inactive, get_service, get_version

from secretvalidate.http_validator import validate_http
from secretvalidate.mongodb_validator import validate_mongodb
from secretvalidate.teams_webhook_validator import validate_teams_webhook
from secretvalidate.utility import format_services, lowercase_choice, update_tool

# Retrieve the current version from environment variable
CURRENT_VERSION = get_version()

def parse_arguments():
    parser = argparse.ArgumentParser(description="Secret Validator Tool",formatter_class=argparse.RawTextHelpFormatter)

    # Retrieve choices from environment variable
    services = get_service()
    formatted_services = format_services(services)
    
    parser.add_argument("-service", type=lowercase_choice, choices=services, required=True, help=f"Service / SecretType to validate secrets.\nSupported services:\n{formatted_services}")
    parser.add_argument("-secret", required=True, help=f"Pass Secrets to be validated")
    parser.add_argument('-r', '--response', action='store_true', help=f"Prints {get_secret_active()}/ {get_secret_inactive()} upon validating secrets.")

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
