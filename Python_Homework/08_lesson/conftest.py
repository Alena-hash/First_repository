import pytest
from yougile_api import YougileApi
import configuration as conf

@pytest.fixture
def api():
    return YougileApi(conf.base_url, conf.token)
