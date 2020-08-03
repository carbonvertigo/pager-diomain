from enum import Enum

class MonitoredSvcState(Enum):
    HEALTHY, UNHEALTHY = 0, 1

class MonitoredSvc:
    def __init__(self, id, state=0):
        self._id = id
        self._state = state

    @property
    def id(self):
        return self._id

    @property
    def state(self):
        return self._state

    @state.setter
    def set_state(self, state):
        self._state = state