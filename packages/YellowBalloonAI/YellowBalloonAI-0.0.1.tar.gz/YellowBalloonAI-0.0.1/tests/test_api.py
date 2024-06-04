import pytest
from ybai_sdk import YellowBalloonAI

def test_get_resource(mocker):
    sdk = YellowBalloonAI(api_key="dummy_api_key")
    mock_response = mocker.Mock()
    mock_response.json.return_value = {"id": 1, "name": "Test Resource"}
    mock_response.status_code = 200
    mocker.patch("requests.get", return_value=mock_response)

    response = sdk.get_resource(1)
    assert response["name"] == "Test Resource"

def test_create_resource(mocker):
    sdk = YellowBalloonAI(api_key="dummy_api_key")
    mock_response = mocker.Mock()
    mock_response.json.return_value = {"id": 1, "name": "New Resource"}
    mock_response.status_code = 201
    mocker.patch("requests.post", return_value=mock_response)

    data = {"name": "New Resource"}
    response = sdk.create_resource(data)
    assert response["name"] == "New Resource"
