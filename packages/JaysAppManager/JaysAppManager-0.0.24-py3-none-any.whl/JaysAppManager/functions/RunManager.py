import uuid



class RunManager:
    def __init__(self):
        self._run_id = None

    def set_run_id(self):
        self._run_id = str(uuid.uuid4())  # Generate a unique run ID

    def get_run_id(self):
        return self._run_id