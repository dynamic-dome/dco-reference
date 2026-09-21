from .model import Job, JobState


class SyntheticWorker:
    def run(self, job: Job) -> None:
        job.state = JobState.RUNNING
        job.record("worker_started", "synthetic worker started")
        job.artifact = f"REFERENCE RESULT: {job.objective.strip()}"
        job.record("artifact_created", "deterministic text artifact created")


class Verifier:
    def verify(self, job: Job) -> bool:
        job.verified = bool(job.artifact and job.artifact.startswith("REFERENCE RESULT:"))
        job.record("verified", f"artifact verification result={job.verified}")
        return job.verified
