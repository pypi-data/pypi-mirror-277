# mcci-api-python

## About

This library is a wrapper around the [MCC Island API](https://api.mccisland.net/docs). Some basic examples are showcased below, but more extensive documentation will be coming soon.

## Examples

### Basics

To unlock this library's features, you first need to set up an `APIClient` instance. There are two options that must be set: `api_key` and `user_agent`:

- `api_key`: Noxcrew requires you to generate an API key on the [Noxcrew Gateway website](https://gateway.noxcrew.com). This is sensitive, so it is recommended to store this in a safe place. For the purpose of this example, we will use the environment variable `MCCI_API_KEY`.
- `user_agent`: Noxcrew also requires a unique [`User-Agent` header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent) header, which is represented here by this option. It is recommended to include a way to contact you in the header, like an email. Usually I format this as the GitHub repository, followed by the contact email. I'll use an environment variable here too, but you can include this directly in the code if you want.

```py
from mcci_api import APIClient
import os

api_key = os.getenv("MCCI_API_KEY")
user_agent = os.getenv("MCCI_API_USER_AGENT")
client = APIClient(api_key=api_key, user_agent=user_agent)
```

Now we have a client!

...more coming soon...
