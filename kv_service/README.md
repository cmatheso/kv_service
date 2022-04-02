# kv_service
The kv_service is a very simple in memory key value cache. It can be manually interacted with using /docs via Swagger UI or for an example usage of it please see the test_client below.

## Local Dev:
- Switch to kv_service directory.
- Create a new venv:
    python -m venv .venv
- Activate .venv
- Install requirements:
    pip install -r requirements.txt

## Testing:
    pip install -r requirements.txt
    pip install -r dev-requirements.txt
    pytest

## Swagger UI
- Simply navigate to /docs in your browser to interact with the services manually.

## Docker Hosting:
- Switch to kv_service directory.
- Execute:
    docker build -t kv_service .
- Run:
    docker run -d --name kv_service -p [DESIRED_PORT]:80 kv_service

    eg. for local use: docker run -d --name kv_service -p 9999:80 kv_service

- Cleanup:
    docker stop kv_service
    docker rm kv_service
    docker image rm kv_service
