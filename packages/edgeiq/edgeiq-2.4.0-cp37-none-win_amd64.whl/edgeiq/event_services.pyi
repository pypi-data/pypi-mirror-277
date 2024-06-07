from _typeshed import Incomplete

def generate_event_timestamp(): ...

class BaseEvent:
    timestamp: Incomplete
    event_label: Incomplete
    object_label: Incomplete
    object_id: Incomplete
    event_id: Incomplete
    camera_label: Incomplete
    zone_label: Incomplete
    data: Incomplete
    def __init__(self, timestamp, event_label, event_id: Incomplete | None = ..., object_label: Incomplete | None = ..., object_id: Incomplete | None = ..., camera_label: Incomplete | None = ..., data: Incomplete | None = ..., zone_label: Incomplete | None = ...) -> None: ...

class OccurrenceEvent(BaseEvent):
    def publish_event(self) -> None: ...

class ValueEvent(BaseEvent):
    value: Incomplete
    def __init__(self, timestamp, value, event_label, object_label: Incomplete | None = ..., event_id: Incomplete | None = ..., object_id: Incomplete | None = ..., camera_label: Incomplete | None = ..., data: Incomplete | None = ..., zone_label: Incomplete | None = ...) -> None: ...
    def publish_event(self) -> None: ...

class StartTimedEvent(BaseEvent):
    def publish_event(self) -> None: ...

class EndTimedEvent(BaseEvent):
    def __init__(self, timestamp, event_id, event_label, object_label: Incomplete | None = ..., object_id: Incomplete | None = ..., camera_label: Incomplete | None = ..., data: Incomplete | None = ..., zone_label: Incomplete | None = ...) -> None: ...
    def publish_event(self) -> None: ...

class CompleteTimedEvent:
    start_timed_event: Incomplete
    end_timed_event: Incomplete
    def __init__(self, start_timestamp, end_timestamp, event_label, event_id: Incomplete | None = ..., start_object_label: Incomplete | None = ..., start_object_id: Incomplete | None = ..., start_camera_label: Incomplete | None = ..., start_zone_label: Incomplete | None = ..., data: Incomplete | None = ..., end_camera_label: Incomplete | None = ..., end_zone_label: Incomplete | None = ..., end_object_id: Incomplete | None = ..., end_object_label: Incomplete | None = ...) -> None: ...
    def publish_event(self) -> None: ...
