from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from uuid import uuid4


class JobState(str, Enum):
    SUBMITTED = "submitted"
    QUEUED = "queued"
    RUNNING = "running"
    AWAITING_APPROVAL = "awaiting_approval"
    APPROVED = "approved"
    COMPLETED = "completed"
    FAILED = "failed"


@dataclass
class Event:
    name: str
    detail: str


@dataclass
class Job:
    objective: str
    requires_approval: bool = True
    id: str = field(default_factory=lambda: uuid4().hex)
    state: JobState = JobState.SUBMITTED
    artifact: str | None = None
    verified: bool = False
    events: list[Event] = field(default_factory=list)

    def record(self, name: str, detail: str) -> None:
        self.events.append(Event(name=name, detail=detail))
