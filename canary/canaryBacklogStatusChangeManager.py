from canary.canaryBaseCommandProcessor import BaseCommandProcessor
import requests
import json

class BacklogStatusChangeManager(BaseCommandProcessor):
    WELCOME_BLOCK = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "Hello from Canary!! :blush:\n"
                "Issue status changed!!"
            ),
        },
    }
    DIVIDER_BLOCK = {"type": "divider"}
    ISSUE_BLOCK = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "Canary Version: {}".format("0.0.1.alpha")
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
        self.config = config

    def loadData(self, data):
        sheetBackend = GoogleSheetsLink(self.config)
        self.data = sheetBackend.postIssue(data)

    def get_message_payload(self):

        return {
            "ts": self.timestamp,
            "channel": self.channel,
            "username": self.username,
            "icon_emoji": self.icon_emoji,
            "blocks": [
                self.WELCOME_BLOCK,
                self.DIVIDER_BLOCK,
                self._get_issue_structure(self.data)
            ],
        }

    @staticmethod
    def _get_issue_structure(data):
        dictData = json.loads(data)
        formatString = ("Data for Issue ID: {} \n"
                        "Issue description: {} \n"
                        "Priority: {} \n"
                        "Posted By: {} \n"
                        "Last Update: {} \n"
                        "Validated: {} \n"
                        "Status: {}")
        dataLike = formatString.format(dictData['Issue ID'], dictData['Issue Description'], dictData['Priority'],
                                       dictData['Posted By'], dictData['Last Update'], dictData['Validated'],
                                       dictData['Status'])
        return {"type": "section", "text": {"type": "mrkdwn", "text": dataLike}}

class GoogleSheetsLink:

    def __init__(self, config):
        self.config = config

    def postIssue(self, details):
        queryDat = self.config.get('GoogleSheets', 'BACKLOG_LINK') + "?type=change_status"
        postData = details
        r = requests.post(queryDat, postData)
        return r.text