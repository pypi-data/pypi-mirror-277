# Guide
0. Require:
    - Python >= 3.7
    - Poetry >= 1.2.0
1. Prepare
    - Install poetry 
    - Using poetry to create new source or init to existed source

2. Configure pyproject.toml
    - Minimum requirements
    ```
    [tool.poetry]
    name = "demopythonlib"      -> project / package name
    version = "0.1.0"           -> pypi only accept code with new version 
    packages = [{include = "demopythonlib"}] -> is package should be packed then push to pypi
    
    ...

    [tool.poetry.dependencies]
    python = "^3.12"            -> python version should fit with your project
    ...

    [tool.poetry.scripts]
    say-hi = "demopythonlib:say_hi"     -> add custom command to run directly from terminal -> like "celery -A worker ...."
    ...

    ```
3. Prepare your pypi account
    - Create new if you need: https://pypi.org/account/register/ 
    - Add 2FA to your account
    - Login > Account Settings > Tokens
    - Add API Token: create a token for all projects (for first time publish) - copy it and securely storage

4. Publish first time
    - Build 
        ```
        $ poetry build
        
        ->  Building demopythonlib (0.1.0)
            - Building sdist
            - Built demopythonlib-0.1.0.tar.gz
            - Building wheel
            - Built demopythonlib-0.1.0-py3-none-any.whl
        ```
    - Add credential
        ``` https://python-poetry.org/docs/repositories/#configuring-credentials
        $ poetry config pypi-token.pypi <your-token>
        ```
    - Publish
        ```
        $ poetry publish
        ```


10. Add Api token to next deploy code
    