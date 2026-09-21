from __future__ import annotations

import argparse
import json

from .orchestrator import Orchestrator


def _serialize(job):
    return {
        "id": job.id,
        "objective": job.objective,
        "state": job.state,
        "verified": job.verified,
        "artifact": job.artifact,
        "events": [{"name": event.name, "detail": event.detail} for event in job.events],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run the synthetic DCO reference workflow")
    parser.add_argument("command", choices=["demo"])
    parser.add_argument("--approve", action="store_true")
    args = parser.parse_args(argv)

    orchestrator = Orchestrator()
    orchestrator.submit("produce a synthetic verification artifact")
    job = orchestrator.process_next()
    if args.approve:
        orchestrator.approve(job, actor="local-demo-operator")
    print(json.dumps(_serialize(job), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
