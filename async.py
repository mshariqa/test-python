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
    # Run the main function
    asyncio.run(main())
    
    # Print a message
    print("This is a test message.")
    
    # Print the current Python version
    print("Current Python version:")
    
    # Print the Python version
    print(sys.version)
