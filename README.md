# Quart Example - How to use and setup Quart

## Step 1: Poetry
To set up Poetry you want to do the following things.</br>
### a) `poetry init` which will create the poetry project
### b) You want to then add an include section to your project with the destination of your start script. 
In this case mine is called `__init__.py` and sits in the following structure:
Hello look at me!!! Again
```
    quart_example
    ├── src
    │   └── poetry_example
    │       ├── __init__.py
    │       └── ...
    ├── .gitignore
    ├── pyproject.toml
    ├── poetry.lock
    └── ...
```
Thus my include statement looks like this (it goes in the `[tool.poetry]` section at the top level):
```
packages = [
  { include = "src", from = "." }
]
```
What does this do? It allows you to install your own project as a package into your venv. This allows you to create scripts you can run which is critical for deployment.
### c) Add your dependencies
In this case you can run `poetry add quart` to install quart and then whatever else you need
### d) Activate your poetry shell and install
Run `poetry shell` in order to launch your virtual environment and then run `poetry install` to install all dependencies including your own package. You need a README.md or the installing of your own project will fail.

## Step 2: Quart
With Poetry now installed, you can start developing in Quart. Let me explain the starter code (you can find it in `__init__.py`):
```
from quart import Quart, jsonify, request

app = Quart(__name__)

@app.get("/example")
async def example():
    return jsonify(["a", "b"])

@app.post("/echo")
async def echo():
    data = await request.get_json()
    return {"input": data, "extra": True}

def run() -> None:
    app.run()
```
- The `from quart import Quart, jsonify, request` line item is importing the outside packages you'll need. Specifically these are versions of jsonify and request bundled with quart.
- `app = Quart(__name__)` is initializing the quart application and assigning it to the variable `app`
- `@app.get("/example")` is a `GET` endpoint. Remember there are 4 types of endpoints, `GET`, `POST`, `PUT`, and `DELETE`. `GET` is meant for just getting static information.
  - The `/example` part of the endpoint means this is the route on the server where you can find that information. If you are running on localhost you could go to `localhost:5000/example` to send that `GET` request
  - The async part is specific to Quart vs. Flask.
- `@app.post("/echo")` is a `POST` endpoint. `POST` endpoints require data to be passed. Use a `POST` endpoint whenever you are expecting something to be sent from the user or frontend.
  - In this case this endpoint expects a JSON object to be passed in. If you were doing authentication you might expect a token or password from the user (as an example)
- The `def run() -> None:` function is meant to be the "start the server" function.

With all of this starter code, you can now add the following to the `pyproject.toml` which can be used to run a script. In this case the script will call the `run` function and thus start the server.
Scripts are important when it comes to DevOps and being able to execute various commands to run your project automatically.
```
[tool.poetry.scripts]
start = "src.quart_example:run"
```
`start` is the name of the script and `src.quart_example` is the path to the `__init__.py` python script. The colon then refers to which function inside the module, in this case the `run` function.
By running `poetry run start` you are running the script called `start`
