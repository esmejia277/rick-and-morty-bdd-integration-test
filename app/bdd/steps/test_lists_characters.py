"""
Simple Integration Test (BDD) for public Rick And Morty API
https://rickandmortyapi.com/api/character
"""

import requests
from pytest_bdd import scenario, given, when, then, parsers

CONVERTERTS = {
    "character_name": str,
    "status_code": str
}

@scenario("../features/characters.feature", "Get characaters from API")
def test_outline():
    pass

@given(parsers.parse("A character name {character_name} from the Rick and Morty API"), target_fixture="characters", converters=CONVERTERTS)
def given_api_get_request(character_name):
    return {"character_name": character_name}

@when('I send the request')
def send_the_request(base_url, characters):
    character_name = characters['character_name'].replace(" ", "%20")
    api_url = f'{base_url}/api/character?name={character_name}'
    response = requests.get(api_url)
    characters['response'] = response.json()
    characters['response']['status_code'] = str(response.status_code)
    
@then(parsers.parse("A list of characters must be returned and {character_name} exists in the response"))
def validate_response(characters, character_name):
    try:
        for character in characters['response']['results']:
            assert character['name'] == character_name
    except KeyError:
        print(f'Unable to find {character_name}')
        assert False

    
@then(parsers.parse("the response code should be {response_code}"))
def check_response_code(characters, response_code):
    assert characters['response']['status_code'] == response_code