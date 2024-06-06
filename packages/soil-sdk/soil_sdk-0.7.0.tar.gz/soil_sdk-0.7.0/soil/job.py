"""Job module"""

from dataclasses import dataclass
from datetime import UTC, datetime

from soil import data
from soil.api import create_experiment, get_experiment
from soil.data_structure import DataStructure
from soil.data_structure import DataStructure as InternalDataStructure
from soil.types import ExperimentStatuses as Statuses
from soil.types import Job


@dataclass(kw_only=True, slots=True)
class _Job(Job):
    """Represents a Job."""

    experiment_id: str
    result_id: str
    _created_at: str
    _group: str
    _total_jobs: int | None = None

    @property
    def group(self) -> str:
        """Get the group of the job"""
        return self._group

    @property
    def created_at(self) -> str:
        """Get the created at of the job"""
        return self._created_at

    @property
    def total_jobs(self) -> int | None:
        """Get the total jobs of the job group"""
        return self._total_jobs

    @property
    def status(self) -> Statuses:
        """Get the status of the job"""
        experiment = get_experiment(self.experiment_id)
        output_key = next(
            output_key
            for (output_key, output_id) in experiment["outputs"].items()
            if output_id == self.result_id
        )
        return experiment["status"][output_key]

    @property
    def data(self) -> DataStructure:  # type:ignore[reportIncompatibleMethodOverride]
        """Get the data of the job"""
        return data(self.result_id)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, _Job):
            return False
        return (
            self.experiment_id == other.experiment_id
            and self.result_id == other.result_id
            and self._created_at == other._created_at
            and self._group == other._group
            and self._total_jobs == other._total_jobs
        )


def _new_job(
    data_structure: InternalDataStructure,
    group: str,
    total_jobs: int | None = None,
) -> Job:
    if data_structure.pipeline is None:
        raise ValueError("Pipeline plan is required")
    if data_structure.sym_id is None:
        raise ValueError("sym_id is required")
    experiment = create_experiment(
        data_structure.pipeline.plan,
        experiment_group=group,
    )
    return _Job(
        experiment_id=experiment["_id"],
        result_id=experiment["outputs"][data_structure.sym_id],
        _created_at=datetime.fromtimestamp(
            experiment["created_at"] / 1000, tz=UTC
        ).isoformat(),
        _group=group,
        _total_jobs=total_jobs,
    )


def job(
    data_object: DataStructure,
    *,
    group: str,
    total_jobs: int | None = None,
) -> Job:
    """Creates a non-blocking job at soil."""
    return _new_job(data_object, group=group, total_jobs=total_jobs)
