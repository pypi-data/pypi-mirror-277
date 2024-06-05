# Copyright (c) 2024 Joseph Hale
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""
A thin wrapper around httpretty to give it a more fluent interface.

Example usage:

```python
import httpmock

@httpmock.enabled
def test_something():
    httpmock.on("GET", "http://example.com").respond(body="Hello, world!")
    assert requests.get("http://example.com").text == "Hello, world!"
```

Documentation for httpretty: https://httpretty.readthedocs.io/en/latest/index.html
"""
import functools
from typing import Literal
from typing import Optional
from typing import Union

import httpretty  # type: ignore  # no stubs available

Method = Literal["GET", "POST", "PUT", "PATCH", "DELETE", "HEAD", "OPTIONS", "CONNECT"]


enabled = functools.partial(httpretty.activate, allow_net_connect=False)
"""
Decorator to enable httpretty for a test.

Usage:

```python
@httpmock.enabled
def test_something():
    ...
```
"""


def on(method: Method, uri: str):
    class ResponseMocker:
        # This one-liner looks nice, but erases type hints.
        # respond = functools.partial(httpretty.register_uri, method=method, uri=uri)
        def respond(
            self,
            body: Union[str, bytes] = '{"message": "HTTPretty :)"}',
            adding_headers: Optional[dict] = None,
            forcing_headers: Optional[dict] = None,
            status: int = 200,
            match_querystring: bool = False,
            priority: int = 0,
            **headers,
        ):
            httpretty.register_uri(
                method=method,
                uri=uri,
                body=body,
                adding_headers=adding_headers,
                forcing_headers=forcing_headers,
                status=status,
                match_querystring=match_querystring,
                priority=priority,
                **headers,
            )

    return ResponseMocker()
