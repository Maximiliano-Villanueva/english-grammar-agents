
# English grammar agents

This repository implements three different agents to provide different options to enhance English writting as well as summarize text. 

These three functionalities are implemented using the Langchain library and are accessible through an API using FastAPI.

## App Architecture
This app has been developed following a layered architecture, separating the application layer from the business logic and the infrastructure.

The application folder contains the implementation of the application layer, in this case the exposure of endpoints for the API.

The services folder contains the implementation of the business logic, in this case the creation of the agents along with business logic exception handling.

The moduless folder contains the necessary python modules to implement the infrasatructure, in this case it contains the logic of the agents. 

## Notebooks
There are 2 notebooks inside the notebooks folder to showcase all 3 use cases.

## Prompts
The prompts used can be seen at src/modules/prompts

## Input sanatizing
The cleaning of the input has not been tested and therefore not included, yet the functions to deal with those cases can be found in the src/modules/cleaner module.

## Installation

### OpenAI API key
The first step is to set a valid OpenAI API key in the src/envs/debug.env file. 
```
OPENAI_API_KEY="YOUR-API-KEY-HERE"
```

Note that the model is set to gpt-4 in order to be as accurate as possible but it is much slower than gpt-3.5-turbo. In case you want to drasticaly reduce the time of the execution gpt3 is recommended.

### Option 1: Docker
In order to run this this demo using docker use the following commands.
```
docker build -t english-grammar-container .
```

Followed by
```
docker run -p 8000:8000 english-grammar-container
```

### Option 2: local deployment
The server can also be instantiated by running:
```
python app.py
```

Before running you should install the dependencies by using the command below.
```
pip install -r requirements.txt
```

## How to try it
There are 2 options to try the API.

### Option 1: Swagger / curl
Just acces http://localhost:8000/docs or send a curl message to the API like this:
```
curl -X 'POST' \
  'http://localhost:8000/writting' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "data": "My text goes here"
  }'
```

### Option 2: Execute the examples provided in the examples directory.

Execute these examples using:
```
python -m examples.writting
```

