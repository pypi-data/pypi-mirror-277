# -*- coding: utf-8 -*-
import asyncio

import pytest as pytest
import pytest_asyncio
from patchwork.core import Task

from patchwork.node import PatchworkWorker
from patchwork.node.core.router import TaskRouter


@pytest_asyncio.fixture
async def worker():
    worker = PatchworkWorker(settings={
        'subscriber': {
            'engine': 'patchwork.core.client.local:AsyncLocalSubscriber',
            'options': {
                'queue_names': ['test'],
            }
        },
        'publisher': {
            'engine': 'patchwork.core.client.local:AsyncLocalPublisher',
        }
    })
    await worker.run()
    yield worker

    await worker.terminate()


@pytest.mark.asyncio
async def test_unsupported_task_use(worker):

    caught_tasks = []

    router = TaskRouter(skip_unsupported_tasks=True)
    worker.include_router(router)

    async def send():
        task = Task(task_type='test-msg-2', payload=b'test')
        task.meta.queue_name = 'test'
        await worker.get_publisher().send_task(task)

    asyncio.create_task(send())

    # wait until executor processing unit becomes busy which means given message has been consumed
    await asyncio.wait_for(worker.executor.busy.wait(), timeout=1)
    assert len(caught_tasks) == 0


@pytest.mark.asyncio
async def test_simple_use(worker):

    caught_tasks = []

    router = TaskRouter()

    @router.on('test-msg')
    async def processor(task: Task):
        caught_tasks.append(task)

    worker.include_router(router)

    async def send():
        task = Task(task_type='test-msg', payload=b'test')
        task.meta.queue_name = 'test'
        await worker.get_publisher().send_task(task)

    asyncio.create_task(send())

    # wait until executor processing unit becomes busy which means given message has been consumed
    await asyncio.wait_for(worker.executor.busy.wait(), timeout=1)
    assert len(caught_tasks) == 1
