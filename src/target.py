class Target:
    def __init__(self, id, comm_type, comm_link):
        self._id = id
        self._comm_type = comm_type
        self._comm_link = comm_link

    @property
    def target(self):
        return (self._id, self._comm_type, self._comm_link)

    @property
    def id(self):
        return self._id

    @property
    def comm_type(self):
        return self._comm_type

    @property
    def comm_link(self):
        return self._comm_link

    # We're missing the adapters here
    def acknowledge(self, alert):
        alert.set_status = 1

    def healthy(self, service):
        service.set_state = 0