from enum import Enum

class AlertStatus(Enum):
    NOT_ACKNOWLEDGED, ACKNOWLEDGED = 0, 1


class Alert:
    def __init__(self, id, svc_id, message, status=0):
        self._id = id
        self._svc_id = svc_id
        self._message = message
        self._status = status

    @property
    def alert(self):
        return (self._id, self._svc_id, self._message, self._status)

    @property
    def id(self):
        return self._id

    @property
    def svc_id(self):
        return self._svc_id

    @property
    def message(self):
        return self._message

    @property
    def status(self):
        return self._status        

    @status.setter
    def set_status(self, status):
        self._status = status