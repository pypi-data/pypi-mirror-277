from aiohttp_sse_client2 import client as sse_client
from aiohttp import ClientSession
import aiohttp
import os
import json

VALID_EVENTS = [
    'stream', 
    'createProjectFromTemplate'
]
class SseException(Exception):
    pass

# TODO: handle sse auth errors, just hangs RN
async def handle_sse_events(rid, tofu_type, on_message=None, wait_for_done=False, debug_level=0):
    try:
        async with ClientSession() as session:
            url = f'http://db.tc.ohmytofu.ai/channel/{tofu_type}/{rid}'
            headers = {'Accept': 'text/event-stream', 'x-tofu-api': os.environ['TOFU_API_KEY']}
            if debug_level >=3: print(url)

            # TODO error handling
            def internal_on_message(event):
                """Additional Callback for message event."""
                if debug_level >= 3: print(event, rid)

                # parse the message
                msg = event if isinstance(event, dict) else json.loads(event.data)

                if debug_level >= 2: print(msg, rid)

                rid_patched = rid.replace('_', '.')
                assert msg['key'].replace('_', '.') == rid_patched , 'Rid doesnt match'

            
            source = sse_client.EventSource(
                url,
                headers=headers,
                session=session,
                on_message=internal_on_message,
            )
            await source.connect()

            async for e in source:
                # message received, handled by message event handler
                # callback
                if on_message: await on_message(msg)
                break

            await source.close()

    except Exception as e:
        print(f'ERRORED ON SSE for {tofu_type}/{rid}')
        print(e)


async def handle_message(event):
    print(f"Received message: {event.data}")

async def listen_to_sse_stream(rid, tofu_type, on_message=None, debug_level=0):
    url = f'http://db.tc.ohmytofu.ai/channel/{tofu_type}/{rid}'
    headers = {'Accept': 'text/event-stream', 'x-tofu-api': os.environ['TOFU_API_KEY']}
    if debug_level >= 1: print(f'listening to sse stream on {url}')

    async with ClientSession() as session:
        should_close_connection = False
        async with sse_client.EventSource(url, session=session, headers=headers) as event_source:
            async for event in event_source:
                if debug_level >= 5: print(event)
                if event.type in VALID_EVENTS:
                    # parse message
                    msg = json.loads(event.data)
                    #msg = json.loads(event['data']) if isinstance(event, dict) else json.loads(event.data)
                    if debug_level >= 4: print(msg)
                    if on_message: 
                        # run callback. if it returns True, we close the connection
                        should_close_connection = on_message(msg)
                    else: await handle_message(msg)

                    # break the loop on the final and confirmed message
                    if should_close_connection:
                        await event_source.close()
                        break
                        
                elif event.type == 'error':
                    print(f"Error: {event.data}")
                elif event.type == 'open':
                    print("Connection opened.")
                elif event.type == 'close':
                    print("Connection closed.")

            # we exited the loop and are done. Upon closing the connection the associated task resolves.
            await event_source.close()
