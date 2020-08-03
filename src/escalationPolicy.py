from target import Target

class EscalationPolicy:
    def __init__(self, id, svc_id, levels=None):
        self._id = id
        self._svc_id = svc_id
        self._levels = levels

    @property
    def policy(self):
        return (self._id, self._svc_id, self._levels)

    @property
    def id(self):
        return self._id
    
    @property
    def svc_id(self):
        return self._svc_id    

    @property
    def levels(self):
        return self._levels

    @levels.setter
    def set_levels(self, levels):
            self._levels = levels


class Levels:
    def __init__(self):
        self._levels = []

    @property
    def levels(self):
        return self._levels

    def add_level(self, level):
            self._levels.append(level)


class Level:
    def __init__(self, id):
        self._id = id
        self._targets = set()

    @property
    def level(self):
        return (self._id, self._targets)

    @property
    def targets(self):
        return self._targets
    

    def add_target(self, target):
            self._targets.add(target)