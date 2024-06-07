import numpy as np
from .tracking_results import TrackingResults as TrackingResults
from edgeiq._utils import gen_logger as gen_logger
from edgeiq.analytics_services import load_analytics_results as load_analytics_results
from edgeiq.exceptions import NoMoreResults as NoMoreResults
from edgeiq.object_tracking.trackable_prediction import PredictionT as PredictionT, TrackablePrediction as TrackablePrediction, TrackablePredictionT as TrackablePredictionT, TrackerCbT as TrackerCbT
from typing import Callable, Generic, List, Optional, Tuple, Type

DEFAULT_DEREGISTER_FRAMES: int
DEFAULT_MAX_DISTANCE: int
DEFAULT_MIN_INERTIA: int
DEFAULT_HISTORY_LENGTH: int

class TrackerAlgorithm(Generic[TrackablePredictionT]):
    def __init__(self, deregister_frames: int, min_inertia: int, history_length: int, enter_cb: Optional[TrackerCbT], exit_cb: Optional[TrackerCbT], trackable: Type[TrackablePredictionT], distance_function: Callable[[TrackablePredictionT, PredictionT], float], match_optimizer: Callable[[np.ndarray], List[Tuple[int, int]]]) -> None: ...
    def update(self, predictions: List[PredictionT], **trackable_kwargs) -> TrackingResults[TrackablePredictionT]: ...
    def remove_id(self, id: int): ...

class TrackerAnalytics(TrackerAlgorithm[TrackablePrediction]):
    def __init__(self, annotations: str) -> None: ...
    def update(self, predictions: Optional[List[PredictionT]], **trackable_kwargs) -> TrackingResults[TrackablePrediction]: ...
