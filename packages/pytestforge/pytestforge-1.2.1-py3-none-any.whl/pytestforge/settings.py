import os
from pytestforge.tools import get_env_as_bool
from urllib.parse import urlparse

print(f'Configuring pytestforge')

# Set constants
AGGREGATOR_PATH = '/api/public/fm/v1/aggregator'
ALLURE_ENVIRONMENT_PROPERTIES_FILE = 'environment.properties'
ALLURE_ZIP = 'allure.zip'

# Read env vars
HUB_URL = os.getenv('HUB_URL') or 'http://selenoid:selenoid@127.0.0.1:4444/wd/hub'
HUB_URL_RESOLVE_IP = get_env_as_bool('HUB_URL_RESOLVE_IP', False)
LOCAL_DRIVER = get_env_as_bool('LOCAL_DRIVER', False)
BROWSER = os.getenv('BROWSER') or 'chrome'
BROWSER_VERSION = os.getenv('BROWSER_VERSION')
BROWSER_PREFS = os.getenv('BROWSER_PREFS')
BROWSER_TIMEOUT = os.getenv('BROWSER_TIMEOUT') or "30"
CHROME_NO_SANDBOX = get_env_as_bool('CHROME_NO_SANDBOX', True)
BUILD_NUMBER = os.getenv('BUILD_NUMBER') or os.getenv('CI_PIPELINE_ID') or "0"
SEND_REPORT = get_env_as_bool("SEND_REPORT", True)
SEND_VERIFY_SSL = get_env_as_bool("SEND_VERIFY_SSL", True)
HUB_ENABLE_VNC = get_env_as_bool('HUB_ENABLE_VNC') or get_env_as_bool('SELENOID_ENABLE_VNC') or False
HUB_TIMEZONE = os.getenv('HUB_TIMEZONE') or os.getenv('SELENOID_TIMEZONE') or 'Etc/GMT'
HUB_HOSTS = os.getenv('HUB_HOSTS') or os.getenv('SELENOID_HOSTS')
HUB_ENV = os.getenv('HUB_ENV') or os.getenv('SELENOID_ENV')
X_FMONQ_PROJECT_KEY = os.getenv('X_FMONQ_PROJECT_KEY')
HTTP_PROXY = os.getenv('HTTP_PROXY')

if os.getenv('AGGREGATOR_URL'):
    parsed_url = urlparse(os.getenv('AGGREGATOR_URL'))
    if parsed_url.scheme == '':
        AGGREGATOR_URL = f'http://{parsed_url.path}'
    else:
        AGGREGATOR_URL = f'{parsed_url.scheme}{parsed_url.path}'
    AGREGATOR_URI = f'{AGGREGATOR_URL}{AGGREGATOR_PATH}'

print(f'Configuration complete')
