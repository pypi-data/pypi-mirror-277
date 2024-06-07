import os
import zipfile
import requests
from pytestforge import settings


def get_env_as_bool(env_name, default=None):
    """ Read env var as boolean
    """
    result = os.getenv(env_name)
    if not result:
        return default
    if result.upper() == 'TRUE':
        return True
    return False


def create_allure_zip(zip_file_name, path):
    """ Make zip from allure report files
    """
    os.chdir(path)

    files = os.listdir(path)
    zip_file = zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED)
    for file in files:
        zip_file.write(file)
    zip_file.close()
    return zip_file


def send_allure_zip(path, uri):
    print(f'Sending report to {uri}.')
    response = requests.post(uri, params={'projectKey': settings.X_FMONQ_PROJECT_KEY}, files={'file': open(path, 'rb')},
                             verify=settings.SEND_VERIFY_SSL)
    print(f'Response: {response.text or response.status_code}.')
    response.raise_for_status()


def get_test_full_path(request):
    """ Find full path of test
    """
    path = str(request.config.known_args_namespace.file_or_dir[0])
    file_name, _, test_name = request.node.location
    if os.path.isdir(path):
        full_path = os.path.join(path, os.path.basename(file_name))
        return full_path, test_name
    else:
        return path, test_name
