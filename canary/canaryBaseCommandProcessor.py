class BaseCommandProcessor:

    data = None

    def loadData(self, data):
        self.data = data

    def get_message_payload(self):
        return None


