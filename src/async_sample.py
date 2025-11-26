import asyncio


async def fetch_data(delay: float) -> float:
    # 'await' yields control back to the event loop
    print(f"Starting fetch with delay of {delay}s...")
    await asyncio.sleep(delay)
    print(f"Finished fetching data after {delay}s.")
    return delay


async def main():
    # Execute two tasks concurrently
    results = await asyncio.gather(
        fetch_data(3),  # Starts, then yields
        fetch_data(1),  # Starts, then yields/finishes faster
    )
    print(f"All tasks completed. Results: {results}")


if __name__ == "__main__":
    # Start the event loop
    asyncio.run(main())
