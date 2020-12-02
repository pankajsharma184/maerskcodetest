from datetime import datetime


class SystemFunction:

    def __init__(self):
        pass

    def start_system_timer(self):
        self.start = float(datetime.utcnow().strftime('%S.%f')[:-3])
        return self.start

    def stop_system_timer(self):
        self.stop = float(datetime.utcnow().strftime('%S.%f')[:-3])
        return self.stop