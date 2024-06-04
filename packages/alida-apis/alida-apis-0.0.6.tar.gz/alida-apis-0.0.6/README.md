Python ALIDA apis.

# Quickstart

## Installation
```
pip install alida-apis
```
## Setup
In order to use it some env variables must be set.
You can either set a token or user and password:
- Token
    ```
    export TOKEN=<your alida token>
    ```
- User and pass:
    ```
    export USERNAME=<your username>
    export PASSWORD=<your password>
    ```
When possible, a token is preferred for security reasons.

## Examples
```python
from alidaapis import service
services = service.get(limit=2)
print(len(services))
```


