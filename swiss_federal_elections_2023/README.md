# DVIZ - Swiss Federal Elections 2023 - Who voted?

## Project Setup

**This project needs python version 3.9**


### Setup python virtual environment

```
cd [path to this file]/..
py -3.9 -m venv venv
```

### Install requirments
```
venv/Scripts/python -m pip install -r swiss_federal_election/requirements.txt
```

### Render output
```
venv/Scripts/python swiss_federal_election/create_data_story.py
```

The output can now be found in `./swiss_federal_elections/data_story/_build/html/index.html`