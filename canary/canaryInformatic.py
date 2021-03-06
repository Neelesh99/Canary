from canary.canaryBaseCommandProcessor import BaseCommandProcessor


class CanaryInformatic(BaseCommandProcessor):
    WELCOME_BLOCK = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "Hello from Canary!! :blush:"
            ),
        },
    }
    DIVIDER_BLOCK = {"type": "divider"}
    VERSION_BLOCK = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "Canary Version: {}".format( "0.0.1.alpha")
            ),
        }
    }
    data = None

    def __init__(self, channel, config):
        self.channel = channel
        self.username = "canary"
        self.icon_emoji = ":robot_face:"
        self.timestamp = ""
        self.reaction_task_completed = False
        self.pin_task_completed = False
        self.VERSION_BLOCK['text']['text'] = "Canary Version: {}".format(config.get("CanaryVersion", "CANARY_VERSION"))

    def loadData(self, data):
        self.data = data

    def get_message_payload(self):

        return {
            "ts": self.timestamp,
            "status": "200",
            "channel": self.channel,
            "username": self.username,
            "icon_emoji": self.icon_emoji,
            "blocks": [
                self.WELCOME_BLOCK,
                self.DIVIDER_BLOCK,
                self.VERSION_BLOCK,
            ],
        }