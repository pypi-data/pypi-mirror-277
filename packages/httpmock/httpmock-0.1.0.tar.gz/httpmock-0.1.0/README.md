<!--
 Copyright (c) 2024 Joseph Hale
 
 This Source Code Form is subject to the terms of the Mozilla Public
 License, v. 2.0. If a copy of the MPL was not distributed with this
 file, You can obtain one at http://mozilla.org/MPL/2.0/.
-->

# httpmock

Fluent API for mocking HTTP requests in Python tests

<!-- BADGES -->
[![](https://badgen.net/github/license/thehale/httpmock)](https://github.com/thehale/httpmock/blob/master/LICENSE)
[![Sponsor Joseph Hale](https://badgen.net/badge/icon/Sponsor/pink?icon=github&label)](https://github.com/sponsors/thehale)
[![Joseph Hale's software engineering blog](https://jhale.dev/badges/website.svg)](https://jhale.dev)
[![Follow Joseph Hale!](https://jhale.dev/badges/follow.svg)](https://www.linkedin.com/comm/mynetwork/discovery-see-all?usecase=PEOPLE_FOLLOWS&followMember=thehale)


`httpmock` is essentially a thin wrapper around `httpretty` to give it a more fluent interface.

Example usage:

```python
import httpmock
import requests

@httpmock.enabled
def test_something():
    httpmock.on("GET", "http://example.com").respond(body="Hello, world!")
    assert requests.get("http://example.com").text == "Hello, world!"
```

Documentation for httpretty: https://httpretty.readthedocs.io/en/latest/index.html

## [License](/LICENSE)
Copyright (c) 2024 - Joseph Hale. All Rights Reserved.

```
httpmock by Joseph Hale is licensed under the terms of the Mozilla
Public License, v 2.0, which are available at https://mozilla.org/MPL/2.0/.

You can download the source code for httpmock for free from
https://github.com/thehale/httpmock.
```
<details>

<summary><b>What does the MPL-2.0 license allow/require?</b></summary>

### TL;DR

You can use files from this project in both open source and proprietary
applications, provided you include the above attribution. However, if
you modify any code in this project, or copy blocks of it into your own
code, you must publicly share the resulting files (note, not your whole
program) under the MPL-2.0. The best way to do this is via a Pull
Request back into this project.

If you have any other questions, you may also find Mozilla's [official
FAQ](https://www.mozilla.org/en-US/MPL/2.0/FAQ/) for the MPL-2.0 license
insightful.

If you dislike this license, you can contact me about negotiating a paid
contract with different terms.

**Disclaimer:** This TL;DR is just a summary. All legal questions
regarding usage of this project must be handled according to the
official terms specified in the `LICENSE` file.

### Why the MPL-2.0 license?

I believe that an open-source software license should ensure that code
can be used everywhere.

Strict copyleft licenses, like the GPL family of licenses, fail to
fulfill that vision because they only permit code to be used in other
GPL-licensed projects. Permissive licenses, like the MIT and Apache
licenses, allow code to be used everywhere but fail to prevent
proprietary or GPL-licensed projects from limiting access to any
improvements they make.

In contrast, the MPL-2.0 license allows code to be used in any software
project, while ensuring that any improvements remain available for
everyone.

</details>
