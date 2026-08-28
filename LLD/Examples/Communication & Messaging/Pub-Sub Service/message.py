import uuid
import time

class Message:
    def __init__(self, payload: str):
        self.id = uuid.uuid4()
        self.payload = payload
        self.timestamp = time.time()
