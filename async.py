import sys
from rich import print
import asyncio

async def do_something():
    await asyncio.sleep(1)
    print("Hello, World!")

async def do_something_else():
    await do_something()
    print("This is a test message from do_something_else.")

async def do_something_else_without_wait():
    print("This is a test message from do_something_else_without_await.")

async def main():
    await asyncio.gather(
            do_something(), 
            do_something_else(),
            do_something_else_without_wait(),
            do_something()
        )

if __name__ == "__main__":
    '''
    Note: We cannot use 'await main()' directly in the global scope because:
    1. The 'await' keyword can only be used inside an async function
    2. The global scope (top-level code) cannot be asynchronous
    That's why we use asyncio.run() - it's the correct way to run async code from synchronous code
    '''
    asyncio.run(main())
    
    # Print a message
    print("This is a test message.")
    
    # Print the current Python version
    print("Current Python version:")
    
    # Print the Python version
    print(sys.version)
