from canary.canaryBaseCommandProcessor import BaseCommandProcessor
import requests
import json

from canary.userManagement import UserManager


class BacklogGetAllManager(BaseCommandProcessor):
    WELCOME_BLOCK = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "Hello from Canary!! :blush:\n"
                "List of all issues:"
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
    issueID = None
    def __init__(self, channel, config):
        self.channel = channel
        self.username = "canary"
        self.icon_emoji = ":robot_face:"
        self.timestamp = ""
        self.reaction_task_completed = False
        self.pin_task_completed = False
        self.config = config

    def loadData(self, data):
        sheetsLink = GoogleSheetsLink(self.config)
        self.data = sheetsLink.getIssue()

    def loadDataUser(self, user_id, data):
        sheetsLink = GoogleSheetsLink(self.config)
        self.data = sheetsLink.getIssueUser(user_id, self.channel)

    def get_message_payload(self):
        if self.data is None:
            return self.get_error_block()
        BasicList = [self.WELCOME_BLOCK, self.DIVIDER_BLOCK]
        return {
            "ts": self.timestamp,
            "channel": self.channel,
            "username": self.username,
            "icon_emoji": self.icon_emoji,
            "blocks":
                self._get_issue_structure(self.data, BasicList)
            ,
        }

    def get_error_block(self):
        return {
            "ts": self.timestamp,
            "channel": self.channel,
            "username": self.username,
            "icon_emoji": self.icon_emoji,
            "blocks": [
                self.WELCOME_BLOCK,
                self.DIVIDER_BLOCK,
                {"type": "section", "text": {"type": "mrkdwn", "text": "User not recognised, please run register_me, use Canary: help for more details"}}
            ],
        }

    @staticmethod
    def _get_issue_structure(data, listData):
        dictDataList = json.loads(data)
        for dictData in dictDataList:
            formatString = ("Data for Issue ID: {} \n"
                            "Issue description: {} \n"
                            "Priority: {} \n"
                            "Posted By: {} \n"
                            "Last Update: {} \n"
                            "Validated: {} \n"
                            "Status: {}")
            dataLike = formatString.format(dictData['Issue ID'], dictData['Issue Description'], dictData['Priority'], dictData['Posted By'], dictData['Last Update'], dictData['Validated'], dictData['Status'])
            listData.append({"type": "section", "text": {"type": "mrkdwn", "text": dataLike}})
        return listData

class GoogleSheetsLink:

    def __init__(self, config):
        self.config = config

    def getIssueUser(self, userId, channel):
        user_manager = UserManager()
        user = user_manager.getUserChannel(userId, channel)
        if user:
            queryDat = self.conditionLink(user_manager.getGoogleFilesLink()) + "?type=get_all_live"
            r = requests.get(queryDat)
            return r.text
        return None

    def getIssue(self):
        queryDat = self.config.get('GoogleSheets', 'BACKLOG_LINK') + "?type=get_all_live"
        r = requests.get(queryDat)
        return r.text

    def conditionLink(self, text):
        return text[:-1]