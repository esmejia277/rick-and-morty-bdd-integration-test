Feature: Rick and Morty API
    As a user, I want to handle the public
    Rick and Morty API.

    Scenario Outline: Get characaters from API
        Given A character name <character_name> from the Rick and Morty API
        When I send the request
        Then A list of characters must be returned and <character_name> exists in the response
        And the response code should be <response_code>

        Examples:
        | character_name                        | response_code |
        |      Rick Sanchez                     |      200      |
        |      Morty Smith                      |      200      |
        |      Summer Smith                     |      200      |
        |      Beth Smith                       |      200      |
