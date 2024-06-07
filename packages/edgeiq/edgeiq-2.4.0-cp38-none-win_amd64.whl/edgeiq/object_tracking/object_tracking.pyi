import numpy as np
from .tracking_results import TrackingResults as TrackingResults
from edgeiq._utils import gen_logger as gen_logger
from edgeiq.analytics_services import load_analytics_results as load_analytics_results
from edgeiq.exceptions import NoMoreResults as NoMoreResults
from edgeiq.object_tracking.trackable_prediction import PredictionT as PredictionT, TrackablePrediction as TrackablePrediction, TrackablePredictionT as TrackablePredictionT, TrackerCbT as TrackerCbT
from typing import Callable, Generic

DEFAULT_DEREGISTER_FRAMES: int
DEFAULT_MAX_DISTANCE: int
DEFAULT_MIN_INERTIA: int
DEFAULT_HISTORY_LENGTH: int

class TrackerAlgorithm(Generic[TrackablePredictionT]):
    def __init__(self, deregister_frames: int, min_inertia: int, history_length: int, enter_cb: TrackerCbT | None, exit_cb: TrackerCbT | None, trackable: type[TrackablePredictionT], distance_function: Callable[[TrackablePredictionT, PredictionT], float], match_optimizer: Callable[[np.ndarray], list[tuple[int, int]]]) -> None: ...
    def update(self, predictions: list[PredictionT], **trackable_kwargs) -> TrackingResults[TrackablePredictionT]: ...
    def remove_id(self, id: int): ...

class TrackerAnalytics(TrackerAlgorithm[TrackablePrediction]):
    def __init__(self, annotations: str) -> None: ...
    def update(self, predictions: list[PredictionT] | None, **trackable_kwargs) -> TrackingResults[TrackablePrediction]: ...
