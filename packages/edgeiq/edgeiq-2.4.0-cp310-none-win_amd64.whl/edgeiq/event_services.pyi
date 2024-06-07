from _typeshed import Incomplete

__all__ = ['generate_event_timestamp', 'OccurrenceEvent', 'ValueEvent', 'StartTimedEvent', 'EndTimedEvent', 'CompleteTimedEvent']

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
    def __init__(self, timestamp, event_label, event_id: Incomplete | None = None, object_label: Incomplete | None = None, object_id: Incomplete | None = None, camera_label: Incomplete | None = None, data: Incomplete | None = None, zone_label: Incomplete | None = None) -> None: ...

class OccurrenceEvent(BaseEvent):
    def publish_event(self) -> None: ...

class ValueEvent(BaseEvent):
    value: Incomplete
    def __init__(self, timestamp, value, event_label, object_label: Incomplete | None = None, event_id: Incomplete | None = None, object_id: Incomplete | None = None, camera_label: Incomplete | None = None, data: Incomplete | None = None, zone_label: Incomplete | None = None) -> None: ...
    def publish_event(self) -> None: ...

class StartTimedEvent(BaseEvent):
    def publish_event(self) -> None: ...

class EndTimedEvent(BaseEvent):
    def __init__(self, timestamp, event_id, event_label, object_label: Incomplete | None = None, object_id: Incomplete | None = None, camera_label: Incomplete | None = None, data: Incomplete | None = None, zone_label: Incomplete | None = None) -> None: ...
    def publish_event(self) -> None: ...

class CompleteTimedEvent:
    start_timed_event: Incomplete
    end_timed_event: Incomplete
    def __init__(self, start_timestamp, end_timestamp, event_label, event_id: Incomplete | None = None, start_object_label: Incomplete | None = None, start_object_id: Incomplete | None = None, start_camera_label: Incomplete | None = None, start_zone_label: Incomplete | None = None, data: Incomplete | None = None, end_camera_label: Incomplete | None = None, end_zone_label: Incomplete | None = None, end_object_id: Incomplete | None = None, end_object_label: Incomplete | None = None) -> None: ...
    def publish_event(self) -> None: ...
