import pytest
from lib.utils.DataReader import read_config
import requests

@pytest.fixture(scope="module")
def check_server():
    config=read_config()
    url = config['integration']['url']+config['integration']['pingUri']
    try:
        response = requests.get(url, timeout=5)
        assert response.status_code == 201, f"The api is not responding"
    except requests.exceptions.RequestException as e:
        raise Exception(f"Server at {url} is offline or unreachable. Details: {e}")
    yield config
