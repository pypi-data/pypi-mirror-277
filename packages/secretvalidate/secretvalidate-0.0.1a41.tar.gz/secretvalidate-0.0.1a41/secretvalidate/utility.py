import os
import subprocess
#Load values from env file
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

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


def update_tool():
    """Update the tool to the latest version."""
    try:
        subprocess.run(["pip", "install", "--upgrade", "your_package_name"], check=True)
        print("Tool updated to the latest version.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to update the tool: {e}")
