# scim2-models

Pydantic models for SCIM2 schemas defined in [RFC7643](https://datatracker.ietf.org/doc/html/rfc7643.html) and [RFC7644](https://datatracker.ietf.org/doc/html/rfc7644.html).

This library provides utilities to parse and produce SCIM2 payloads, and handle them with native Python objects.
It aims to be used as a basis to build SCIM2 servers and clients.

## Installation

```shell
pip install scim2-models
```

## Usage

Check the [tutorial](https://scim2-models.readthedocs.io/en/latest/tutorial.html) and the [reference](https://scim2-models.readthedocs.io/en/latest/reference.html) for more details.

```python
from scim2_models import User
import datetime

payload = {
    "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
    "id": "2819c223-7f76-453a-919d-413861904646",
    "userName": "bjensen@example.com",
    "meta": {
        "resourceType": "User",
        "created": "2010-01-23T04:56:22Z",
        "lastModified": "2011-05-13T04:42:34Z",
        "version": 'W\\/"3694e05e9dff590"',
        "location": "https://example.com/v2/Users/2819c223-7f76-453a-919d-413861904646",
    },
}

user = User.model_validate(payload)
assert user.user_name == "bjensen@example.com"
assert user.meta.created == datetime.datetime(
    2010, 1, 23, 4, 56, 22, tzinfo=datetime.timezone.utc
)
```
