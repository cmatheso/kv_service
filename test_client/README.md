# test_client
A simple client which tests the kv_service. Exposes 2 primary testing endpoints: /test/overwrite and /test/deletion.

## Local Dev:
- Switch to test_client directory.
- Create a new venv:
    python -m venv .venv
- Activate venv.
- Install requirements:
    pip install -r requirements.txt
- This client requires a running instance of kv_service. Create a .env file with the following settings once configured:
KV_SERVICE_URL=[HOSTED_KV_SERVICE_URL]

## Testing:
    pip install -r requirements.txt
    pip install -r dev-requirements.txt
    pytest

## Swagger UI
- Simply navigate to /docs in your browser to interact with the services manually.

## Docker Hosting:
- Switch to test_client directory.
- Execute:
    docker build -t test_client .
- Run:
    docker run -d --name test_client -p [DESIRED_PORT]:80 -e KV_SERVICE_URL=[HOSTED_KV_SERVICE_URL] test_client

    eg. for local use: docker run -d --name test_client -p 80:80 -e KV_SERVICE_URL=http://localhost:9999 test_client

- Cleanup:
    docker stop test_client
    docker rm test_client
    docker image rm test_client
