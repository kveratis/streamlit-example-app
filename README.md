# streamlit-example-app

Example Streamlit Application using Docker Containers

## Local Development

### Create Virutal Environment

```cli
python -m venv env
```

### Activate Virtual Environment

#### Windows

```cli
env\Scripts\activate
```

#### Linux/MacOS

```
source ./env/bin/activate
```

### Update Tools

```cli
python -m pip install -U pip wheel setuptools pylint
```

## Install Dependencies

```cli
pip install -r ./app/requirements.txt
```

## Run app in docker

```cli
docker-compose up --build
```
