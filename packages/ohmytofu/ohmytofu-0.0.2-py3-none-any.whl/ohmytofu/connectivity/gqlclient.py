from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
import os

# TODO
API_KEY = os.environ['TOFU_API_KEY']
API_BASE = 'https://db.tc.ohmytofu.ai'

# Select your transport with a defined url endpoint
transport = AIOHTTPTransport(
    url=API_BASE, 
    headers={'x-tofu-api': API_KEY})

# Create a GraphQL client using the defined transport
client = Client(transport=transport, fetch_schema_from_transport=True)


