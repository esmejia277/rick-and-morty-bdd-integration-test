# Rick and Morty bdd-integration test

This is an example of BDD/Integration test by using Rick & Morty public API.

https://rickandmortyapi.com/api/character

https://rickandmortyapi.com/

1. Clone this project

    `git clone git@github.com:esmejia277/rick-and-morty-bdd-integration-test.git`

3. Create a virtualenv

   `python3 -m venv env`

4. Activate your virtual environment

   `source env/bin/activate`

5. Install dependencies

   `pip install -r requirements.txt`

6. Run tests with
   
   `pytest`

7. Output
  
    `platform linux -- Python 3.10.8, pytest-7.2.0, pluggy-1.0.0`

    `rootdir: /home/esteban/esteban/snippets/python/bdd/app/bdd`

    `plugins: bdd-6.1.1`

    `collected 4 items`

    `app/bdd/steps/test_lists_characters.py ....  [100%]`

   `=== 4 passed in 1.62s ===`