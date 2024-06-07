import time
import pytest
from pytestforge import settings
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.remote.remote_connection import RemoteConnection


def chrome_options():
    options = ChromeOptions()
    options.add_argument("disable-extensions")
    options.add_argument("disable-infobars")
    options.add_argument('--ignore-certificate-errors')
    if settings.CHROME_NO_SANDBOX:
        options.add_argument('--no-sandbox')
    if not settings.HUB_ENABLE_VNC:
        options.add_argument('--headless')
    options.add_experimental_option(
        'prefs', {
            'download': {
                'prompt_for_download': False
            },
            'credentials_enable_service': False,
            'profile': {
                'password_manager_enabled': False
            },
            "plugins.plugins_enabled": [
                "Chrome PDF Viewer",
                "Native Client"
            ]
        }
    )
    if settings.LOCAL_DRIVER:
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
    if settings.HTTP_PROXY:
        options.add_argument(f"--proxy-server={settings.HTTP_PROXY}")
    return options.to_capabilities()


def firefox_options():
    options = FirefoxOptions()
    if not settings.HUB_ENABLE_VNC:
        options.headless = True
    if settings.BROWSER_PREFS:
        prefs = settings.BROWSER_PREFS.split(';')
        for pref in prefs:
            key, value = pref.split(':')
            options.set_preference(key, value)
    return options.to_capabilities()


def safari_options():
    options = {
        'browserName': 'safari'
    }
    return options


def edge_options():
    options = {
        'browserName': 'MicrosoftEdge'
    }
    return options


def selenoid_options(**kwargs):
    options = {
        'enableVNC': settings.HUB_ENABLE_VNC,
        'timeZone': settings.HUB_TIMEZONE
    }
    if settings.HUB_HOSTS:
        hosts_entries = settings.HUB_HOSTS.split(';')
        options['hostsEntries'] = hosts_entries
        if isinstance(settings.HUB_HOSTS, list):
            options['hostsEntries'] = settings.HUB_HOSTS

    if settings.HUB_ENV:
        env = options.get('env', [])
        env.extend(json.loads(settings.HUB_ENV))
        options.update({'env': env})

    options.update(kwargs)
    return options


def local_driver(**kwargs):
    options = {}

    if settings.BROWSER == 'chrome':
        options.update(chrome_options())
        driver = webdriver.Chrome(desired_capabilities=options, service_args=['--allowed-ips=127.0.0.1'])
    else:
        pytest.exit(f'Browser {settings.BROWSER} is unsupported with LOCAL_DRIVER', 1)
    driver.maximize_window()
    return driver


def remote_driver(**kwargs):
    custom_capabilities = {}
    selenoid_args = {}

    sel_options = selenoid_options(**selenoid_args)
    custom_capabilities.update(sel_options)

    options = {}
    if settings.BROWSER.lower() == 'chrome':
        options = chrome_options()
        options.pop('version', None)
    elif settings.BROWSER.lower() == 'firefox':
        options = firefox_options()
    elif settings.BROWSER.lower() == 'safari':
        options = safari_options()
    elif settings.BROWSER.lower() == 'edge':
        options = edge_options()
    custom_capabilities.update(options)
    if settings.BROWSER_VERSION:
        custom_capabilities['version'] = settings.BROWSER_VERSION
    custom_capabilities["moon:options"] = sel_options

    driver = webdriver.Remote(
        command_executor=RemoteConnection(settings.HUB_URL, resolve_ip=settings.HUB_URL_RESOLVE_IP),
        desired_capabilities=custom_capabilities)
    time.sleep(5)
    settings.BROWSER_VERSION = driver.capabilities["browserVersion"]
    driver.set_window_size(1920, 1080)
    return driver
