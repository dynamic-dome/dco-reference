from .model import Job, JobState
from .queue import InMemoryQueue
from .worker import SyntheticWorker, Verifier


class Orchestrator:
    def __init__(self) -> None:
        self.queue = InMemoryQueue()
        self.worker = SyntheticWorker()
        self.verifier = Verifier()

    def submit(self, objective: str, *, requires_approval: bool = True) -> Job:
        if not objective or not objective.strip():
            raise ValueError("objective must not be empty")
        job = Job(objective=objective.strip(), requires_approval=requires_approval)
        job.record("submitted", "objective validated")
        self.queue.put(job)
        return job

    def process_next(self) -> Job:
        job = self.queue.get()
        self.worker.run(job)
        if not self.verifier.verify(job):
            job.state = JobState.FAILED
            return job
        if job.requires_approval:
            job.state = JobState.AWAITING_APPROVAL
            job.record("approval_required", "write-like finalization remains blocked")
        else:
            self._complete(job)
        return job

    def approve(self, job: Job, *, actor: str) -> None:
        if job.state is not JobState.AWAITING_APPROVAL:
            raise ValueError("job is not awaiting approval")
        if not actor.strip():
            raise ValueError("approval actor must not be empty")
        job.state = JobState.APPROVED
        job.record("approved", f"human approval recorded for actor={actor.strip()}")
        self._complete(job)

    @staticmethod
    def _complete(job: Job) -> None:
        job.state = JobState.COMPLETED
        job.record("completed", "verified result finalized")
