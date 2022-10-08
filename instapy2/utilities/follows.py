class FollowUtility:
    def __init__(self):
        self.enabled = False
        self.percentage = 0
        self.times = 1

    def set_enabled(self, enabled: bool):
        self.enabled = enabled

    def set_percentage(self, percentage: bool):
        self.percentage = percentage

    def set_times(self, times: int):
        self.times = times