# Redactive Python SDK

## Install

```bash
pip install redactive
```

## Usage

### Auth Client

```python
import redactive
import asyncio
from typing import Literal

# Use the API key you generated in the app dashboard.
# https://dashboard.redactive.ai
client = redactive.AuthClient(api_key="")

# This is the redirect url Redactive will redirect the user to 
# after successfully connecting to a data source.
redirect_uri = "https://url-debugger.vercel.app/"

async def connect_datasource(datasource: redactive.Datasources):
    sign_in_url = await client.begin_connection(provider=datasource, redirect_uri=redirect_uri)

    print(sign_in_url)

    # Have the user go to the sign in url and follow the OAuth flow. 
    # Once completed and at the redirect website get the URL parameter "code" and use it in exchange_tokens
    response = await client.exchange_tokens(code=code)

    # Once this is complete you can use the idToken in the response object to run semantic queries.
    print(response)

if __name__ == "__main__":
    # The current list of data sources that Redactive can connect to.
    # "confluence", "google-drive", "jira", "zendesk", "slack", "sharepoint"
    asyncio.run(connect_datasource("confluence"))
```

### Search Client

```python
import redactive 
import asyncio

client = redactive.SearchClient()

# This is the id token returned from the auth client method connect datasource
access_token = ""

async def semantic_query():    
    while True:
        semantic_query = input("Enter a query: ")
        if not semantic_query:
            break
        chunks = await client.query_chunks(semantic_query, access_token, count=count, filter=filter_dict)
        for chunk in chunks:
            print(chunk.chunk_body)


if __name__ == "__main__":
    asyncio.run(semantic_query())
```

## FastAPI Example

