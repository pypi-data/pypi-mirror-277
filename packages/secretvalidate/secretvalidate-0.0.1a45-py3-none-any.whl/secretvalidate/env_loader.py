# env_loader.py
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Debug print to check loaded environment variables
print(os.environ)

def get_service():
    """Retrieve the list of supported service types."""
    service_types = os.getenv('SERVICE_TYPES')
    if service_types:
        return service_types.split(',')
    else:
        raise ValueError("Error: 'SERVICE_TYPES' environment variable not set.")

def get_version():
    """Retrieve the current version."""
    return os.getenv('VERSION', "0.0.1")

def get_secret_active():
    """Retrieve the value for active secret."""
    return os.getenv('SECRET_ACTIVE', "Active")

def get_secret_inactive():
    """Retrieve the value for inactive secret."""
    return os.getenv('SECRET_INACTIVE', "InActive")
