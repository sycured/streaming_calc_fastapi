# streaming_calc_fastapi

Bandwidth calculation for streaming server - webservice | Rewrite from my original in Python

## Usage

### Run the server

	uvicorn main:app

### Information about endpoints

#### Documentation
##### Swagger
	curl http://localhost:8000/
##### Redoc
    curl http://localhost:8000/redoc
##### OpenAPI
    curl http://localhost:8000/openapi.json

#### Computing
    curl http://localhost:8000/bwserver
	curl http://localhost:8000/serverusagebw

### Determine necessary server bandwidth

    curl -XPOST -H "Content-Type: application/json" --data '{"nblisteners":250,"bitrate":64}' http://localhost:8000/bwserver

**Output**

    {"server_bandwidth":15625.0}

### Determine the amount of data used for the streaming

    curl -XPOST -H "Content-Type: application/json" --data '{"nblisteners":250,"bitrate":64,"nbdays":1,"nbhours":24}' http://localhost:8000/serverusagebw

**Output**

    {"bandwidth_used":164794.921875}
