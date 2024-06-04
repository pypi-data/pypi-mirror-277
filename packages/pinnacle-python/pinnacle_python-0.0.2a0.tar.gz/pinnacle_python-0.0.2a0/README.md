# Pinnacle Python Client
This is the official Python client for the Pinnacle Serverless Backend API. 

## Pre-requisites
- Python 3.12 or higher

## Usage
1) Install the package using pip:
```bash
pip install pinnacle-python
```
2) To define an endpoint, use the `@endpoint` decorator:
```python
from pinnacle_python import endpoint

@endpoint
def hello_world():
    return "Hello, World!"
```
This will create a POST endpoint at `/hello_world` with no parameters.

3) To define a scheduled script, use the `@scheduled` decorator:
```python
from pinnacle_python import schedule, Period
@schedule(
    for_time=datetime.datetime.today() + timedelta(minutes=1), 
    repeats=Period(seconds=2)
)
def test_job():
    print("Hello, world!")
```
This will run the `test_job` function every 2 seconds starting 1 minute from the time the script is deployed. See the [schedule documentation](./pinnacle_python/schedules.py) for more information on how to configure the schedule.

4) Install the Pinnacle CLI:
```bash
pip install pinnacle-cli
```
5) Deploy the endpoint using the CLI:
```bash
pinnacle dev
```
6) You can now access the endpoint at `http://localhost:8000/hello_world`. Calling the endpoint 
```bash
curl -X POST http://localhost:8000/hello_world \
     -H "Content-Type: application/json" \
     -d '{}'
```
will return a JSON in the following format:
```json
{
    "data": "Hello, World!"
}
```

## Environment Variables
See the [Pinnacle CLI README](../../cli/README.md#environment-variables) for a list of environment variables that can be used to configure the Pinnacle CLI.