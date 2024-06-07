
import requests
from urllib import request


def validate_teams_webhook(webhook_url, response):
    """Validate Teams webhook URL."""
    payload = {'text': ''}
    headers = {'Content-Type': 'application/json'}
    
    try:
        response_data = request.post(webhook_url, json=payload, headers=headers)
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
