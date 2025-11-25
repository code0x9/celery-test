import asyncio
import sys
from temporalio.client import Client
from temporal_worker import AddInputs, AddWorkflow


async def client(x: int, y: int):
    client = await Client.connect("localhost:7233")
    result: int | float = await client.execute_workflow(
        AddWorkflow.run,
        AddInputs(x, y),
        id="my-workflow-id",
        task_queue="add-task-queue",
    )
    print(f"Result: {result}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python temporal_client.py <x> <y>")
        sys.exit(1)
    x, y = int(sys.argv[1]), int(sys.argv[2])
    asyncio.run(client(x, y))
