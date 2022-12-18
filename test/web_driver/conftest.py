import pytest


@pytest.fixture
def target_price() -> str:
    return "US$629.90"


@pytest.fixture
def target_number() -> float:
    return 6586385

@pytest.fixture
def cookie_mandarin_title() -> str:
    return "0 块饼干 - Cookie Clicker"