import pytest

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        "viewport": {
            "width": 500,
            "height": 500,
        }
    }
