import ibis
import pytest


@pytest.fixture(scope="session")
def con():
    yield ibis.connect("duckdb://")
