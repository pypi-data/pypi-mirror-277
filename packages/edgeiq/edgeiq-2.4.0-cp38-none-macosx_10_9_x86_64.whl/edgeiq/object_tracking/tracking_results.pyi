from _typeshed import Incomplete
from edgeiq import object_detection as object_detection
from edgeiq.object_tracking.trackable_prediction import TrackablePrediction as TrackablePrediction
from edgeiq.tools import to_json_serializable as to_json_serializable
from typing import TypeVar

T = TypeVar('T')

class TrackingResults(dict[int, T]):
    def __init__(self, objects: dict[int, T], tracking_algorithm: str) -> None: ...
    @property
    def tracking_algorithm(self): ...

RESULT_TYPE: Incomplete
