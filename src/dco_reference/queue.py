from collections import deque

from .model import Job, JobState


class InMemoryQueue:
    def __init__(self) -> None:
        self._jobs: deque[Job] = deque()

    def put(self, job: Job) -> None:
        job.state = JobState.QUEUED
        job.record("queued", "job accepted by in-memory queue")
        self._jobs.append(job)

    def get(self) -> Job:
        if not self._jobs:
            raise LookupError("queue is empty")
        return self._jobs.popleft()
