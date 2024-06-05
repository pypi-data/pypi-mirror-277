import asyncio
from functools import wraps
import nest_asyncio

# Apply the nest_asyncio patch to allow nested event loops
nest_asyncio.apply()

def block(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if asyncio.iscoroutinefunction(func):
            try:
                # Try to get the running event loop
                loop = asyncio.get_running_loop()
            except RuntimeError:
                # No running event loop, use asyncio.run()
                return asyncio.run(func(*args, **kwargs))
            else:
                # Running event loop, use loop.run_until_complete()
                return loop.run_until_complete(func(*args, **kwargs))
        else:
            raise TypeError("The block decorator can only be used with coroutine functions")
    return wrapper

