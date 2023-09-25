import pytest

from helperFunctions.helper_functions import RequestFunctions


@pytest.fixture
def helper():
    return RequestFunctions()
