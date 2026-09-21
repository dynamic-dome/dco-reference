import pytest

from dco_reference import JobState, Orchestrator


def test_empty_objective_is_rejected():
    with pytest.raises(ValueError, match="objective"):
        Orchestrator().submit("  ")


def test_verified_job_waits_for_approval():
    orchestrator = Orchestrator()
    job = orchestrator.submit("build synthetic artifact")

    processed = orchestrator.process_next()

    assert processed is job
    assert job.verified is True
    assert job.state is JobState.AWAITING_APPROVAL
    assert "approval_required" in [event.name for event in job.events]


def test_human_approval_completes_job():
    orchestrator = Orchestrator()
    job = orchestrator.submit("build synthetic artifact")
    orchestrator.process_next()

    orchestrator.approve(job, actor="owner")

    assert job.state is JobState.COMPLETED
    assert [event.name for event in job.events][-2:] == ["approved", "completed"]


def test_safe_job_can_complete_without_approval():
    orchestrator = Orchestrator()
    job = orchestrator.submit("read synthetic input", requires_approval=False)

    orchestrator.process_next()

    assert job.state is JobState.COMPLETED


def test_approval_is_rejected_in_wrong_state():
    orchestrator = Orchestrator()
    job = orchestrator.submit("queued only")

    with pytest.raises(ValueError, match="not awaiting approval"):
        orchestrator.approve(job, actor="owner")
