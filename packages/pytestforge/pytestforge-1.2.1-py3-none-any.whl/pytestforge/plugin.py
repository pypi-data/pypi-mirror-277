import pytest
from os import path
from pytestforge import settings
from pytestforge.page import Page
from pytestforge.driver import remote_driver, local_driver
from pytestforge.tools import create_allure_zip, send_allure_zip, get_test_full_path


@pytest.fixture(scope='session')
def browser():
    try:
        if settings.LOCAL_DRIVER:
            driver = local_driver()
        else:
            driver = remote_driver()
        driver = Page(driver)
        driver.timeout = int(settings.BROWSER_TIMEOUT)
        driver.set_page_load_timeout(int(settings.BROWSER_TIMEOUT))
        driver.set_script_timeout(int(settings.BROWSER_TIMEOUT))
        yield driver
        driver.quit()
    except Exception as err:
        print(err)


@pytest.fixture(autouse=True)
def prepare_test_env(request):
    test_full_path, test_name = get_test_full_path(request)
    ALLURE_DIR = request.config.option.allure_report_dir
    environment_properties = {
        'project': test_name,
        'build': settings.BUILD_NUMBER,
        'browser': f'{settings.BROWSER}:{settings.BROWSER_VERSION}'
    }
    with open(path.join(ALLURE_DIR, settings.ALLURE_ENVIRONMENT_PROPERTIES_FILE), 'w') as _f:
        data = '\n'.join([f'{variable}={value}' for variable, value in environment_properties.items()])
        _f.write(data)


def pytest_terminal_summary(config):
    if settings.SEND_REPORT and settings.AGREGATOR_URI and settings.X_FMONQ_PROJECT_KEY:
        if str(config.option.allure_report_dir).startswith("/"):
            allure_dir = config.option.allure_report_dir
        else:
            allure_dir = f'{config.invocation_dir}/{config.option.allure_report_dir}'
        create_allure_zip(settings.ALLURE_ZIP, allure_dir)
        send_allure_zip(f'{allure_dir}/{settings.ALLURE_ZIP}', settings.AGREGATOR_URI)
    else:
        print(f'The report will not be sent. Check configuration.')
