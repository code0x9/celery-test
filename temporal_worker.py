import asyncio
from datetime import timedelta
from temporalio import activity, workflow
from temporalio.client import Client
from temporalio.worker import Worker
from dataclasses import dataclass


@dataclass
class AddInputs:
    x: int | float
    y: int | float


@activity.defn
async def add(inputs: AddInputs) -> int | float:
    return inputs.x + inputs.y


@workflow.defn
class AddWorkflow:
    @workflow.run
    async def run(self, inputs: AddInputs) -> int | float:
        return await workflow.execute_activity(
            add,
            inputs,
            start_to_close_timeout=timedelta(seconds=5),
        )


async def main():
    client = await Client.connect("localhost:7233")
    worker = Worker(
        client,
        task_queue="add-task-queue",
        workflows=[AddWorkflow],
        activities=[add],
    )
    print("worker started.")
    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
