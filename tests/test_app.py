import pytest
from src.quart_example import app as quart_example


@pytest.fixture
def test_client():
    """This fixture creates a test client for the app."""
    quart_example.app.config["TESTING"] = True
    client = quart_example.app.test_client()
    yield client


@pytest.mark.asyncio
async def test_currencies_supported(test_client):
    """Test the /currencies endpoint."""
    response = await test_client.get("/currencies")
    assert response.status_code == 200
    assert await response.json == quart_example.currency_list()


def test_currency_list():
    """Test the currency_list function."""
    expected_list = {"dollar": "USD", "euro": "EUR", "british sterling": "GBP"}
    assert quart_example.currency_list() == expected_list


@pytest.mark.parametrize(
    "currency_name, expected_response",
    [
        pytest.param("dollar", "Currency is accepted", id="Currency good"),
        pytest.param("euro", "Currency is accepted", id="Currency good"),
        pytest.param("yen", "Currency not supported", id="Currency bad"),
    ],
)
@pytest.mark.asyncio
async def test_currency_supported(
    currency_name, expected_response, test_client, mocker
):
    """Test the /currency_supported endpoint."""
    mocker.patch.object(
        quart_example, "currency_list", return_value={"dollar": "USD", "euro": "EUR"}
    )
    test_data = {"currency_name": currency_name}
    response = await test_client.post("/currency_supported", json=test_data)
    assert response.status_code == 200
    assert await response.get_data(as_text=True) == expected_response
