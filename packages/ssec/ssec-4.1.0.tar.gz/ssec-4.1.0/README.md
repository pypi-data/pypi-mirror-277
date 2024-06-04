# ssec

[![Rye](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/rye/main/artwork/badge.json)](https://github.com/astral-sh/rye)
[![ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://github.com/python/mypy)

## Description

Yet another library for server-sent events.  
This library works with [httpx](https://github.com/encode/httpx) to support
synchronous as well as asynchronous workflows but is also usable with other
http frameworks ([see below](#aiohttp)).

## Example

`sync`

```python
import logging
import ssec

def main() -> None:
    logging.basicConfig(level=logging.INFO)
    for event in ssec.sse(
        "https://stream.wikimedia.org/v2/stream/recentchange"
    ):
        print(event)

main()
```

`async`

```python
import asyncio
import logging
import ssec

async def main() -> None:
    logging.basicConfig(level=logging.INFO)
    async for event in ssec.sse_async(
        "https://stream.wikimedia.org/v2/stream/recentchange"
    ):
        print(event)

asyncio.run(main())
```

## Note

Although there are already some libraries on the subject
([aiohttp-sse-client](https://github.com/rtfol/aiohttp-sse-client),
[aiosseclient](https://github.com/ebraminio/aiosseclient)), these are
unfortunately not entirely correct. In example, both mentioned libraries
asynchronously iterate over the stream content via `async for line in response.content`[^1][^2].
This internally calls [aiohttp](https://docs.aiohttp.org/en/stable)'s
[`readuntil`](https://docs.aiohttp.org/en/stable/streams.html#aiohttp.StreamReader.readuntil)
method with the default seperator `\n`, but the official specification says:

> Lines must be separated by either a U+000D CARRIAGE RETURN U+000A LINE FEED
   (CRLF) character pair, a single U+000A LINE FEED (LF) character, or a
   single +000D CARRIAGE RETURN (CR) character.

Another point is the error handling, which is often not sufficient to analyze
the error or is entirely skipped.

### aiohttp

Although this library works with `httpx`, it is also possible to use it with
other http frameworks like `aiohttp` as long as they provide a method to
iterate over a byte-stream. Unfortunately, it is not possible to handle
reconnection then, so you will have to implement that by yourself. An example
could look like this:

```python
import asyncio
import logging

import aiohttp
import ssec

async def main() -> None:
    logging.basicConfig(level=logging.INFO)

    chunk_size = 1024
    connect_attempt = 1
    max_connect_attempts = 5
    config = ssec.SSEConfig(reconnect_timeout=3)
    async with aiohttp.ClientSession() as session:
        while True:
            headers = {
                "Accept": "text/event-stream",
                "Cache-Control": "no-store",
            }
            if config.last_event_id:
                headers["Last-Event-ID"] = config.last_event_id
            try:
                async with session.get(
                    "https://stream.wikimedia.org/v2/stream/recentchange",
                ) as response:
                    streamer = response.content.iter_chunked(chunk_size)
                    async for event in ssec.stream_async(streamer, config=config):
                        print(event)
            except aiohttp.ClientError:
                if connect_attempt >= max_connect_attempts:
                    logging.exception("Failed to connect!")
                    raise

                waiting_period = config.reconnect_timeout

                message = (
                    f"Failed to connect. "
                    f"Reconnect in {waiting_period} seconds "
                    f"[attempt {connect_attempt}/{max_connect_attempts}]."
                )
                logging.info(message)

                connect_attempt += 1
                await asyncio.sleep(waiting_period)

asyncio.run(main())
```

[^1]: [Code Reference](https://github.com/rtfol/aiohttp-sse-client/blob/e311075ac8b9b75d8b09512f8638f1dd03e2ef2b/aiohttp_sse_client/client.py#L157)  
[^2]: [Code Reference](https://github.com/ebraminio/aiosseclient/blob/375d597bcc3a7bf871b65913b366d515b300dc93/aiosseclient.py#L131)

## Installation

ssec is written in [Python](https://www.python.org) and tries to keep track
of the newest version available. Currently[^3], this is
[Python 3.12.3](https://www.python.org/downloads/release/python-3123/).
On some operating systems, this version is pre-installed, but on many it is
not. This guide will not go into details on the installation process, but
there are tons of instructions out there to guide you. A good starting point
is the [beginners guide](https://www.python.org/about/gettingstarted/).

[^3]: 06\. May 2024

## Installation (User)

..via [rye](https://github.com/astral-sh/rye):

```sh
rye add ssec
```

..via [pip](https://pypi.org):

```sh
pip install ssec
```

## Installation (Developer)

**1\. Clone this repository to a desired location on your maschine using `ssh`:**

```sh
git git@github.com:sharly-project/ssec.git
```

**2\. Change into the project directory:**

```sh
cd ssec
```

**3\. Sync:**

```sh
rye sync
```

**4\. Run an example:**

```sh
rye run sse_sync_example
```

\- or -

```sh
rye run sse_async_example
```

**5\. Start coding!**

## Miscellaneous

### Documentation

Build the documentation by running the following command in the root directory
of the project:

```sh
sphinx-build -b html docs/src docs/build
```

> The command requires that the [developers edition](#installation-developer)
> of `ssec` is installed and the virtual environment is running.

The documentation is then accessible via `doc/build/index.html`.

### Set up Visual Studio Code for Development

To edit the code base with [Visual Studio Code](https://code.visualstudio.com),
install the following extensions:

| Name              | URL                                                                                  |
|-------------------|--------------------------------------------------------------------------------------|
| Python            | <https://marketplace.visualstudio.com/items?itemName=ms-python.python>               |
| Mypy Type Checker | <https://marketplace.visualstudio.com/items?itemName=ms-python.mypy-type-checker>    |
| Ruff              | <https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff>             |
| markdownlint      | <https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint> |
| Even Better TOML  | <https://marketplace.visualstudio.com/items?itemName=tamasfe.even-better-toml>       |

Necessary settings are already included in the `.vscode` directory and should
be enabled per default.

## Contributing

Contributing to `ssec` is highly appreciated, but comes with some requirements:

1. **Type Hints**

    Write modern python code using
    [type annotations](https://peps.python.org/pep-0484/)
    to enable static analysis and potential runtime type checking.

2. **Documentation**

    Write quality documentation using
    [numpydoc](https://numpydoc.readthedocs.io/en/latest/format.html)
    docstring conventions.

3. **Linting**

   Lint your code with [ruff](https://github.com/charliermarsh/ruff) and
   [mypy](http://mypy-lang.org).

4. **Style**

    Format your code using [ruff](https://github.com/charliermarsh/ruff).

5. **Testing**

    Write tests for your code using
    [pytest](https://docs.python.org/3/library/unittest.html).
