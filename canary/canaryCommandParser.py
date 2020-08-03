from canary.canaryInformatic import CanaryInformatic
from canary.canaryBacklogManager import BacklogGetSingleManager
from canary.canaryBackLogInsertManager import BacklogInsertManager
from canary.canaryBacklogStatusChangeManager import BacklogStatusChangeManager
from canary.canaryBacklogGetAllManager import BacklogGetAllManager
from canary.userManagement import UserManager


class CommandParser:

    user_id = None
    DIVIDER_BLOCK = {"type": "divider"}
    WELCOME_BLOCK = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "Welcome to Canary!! :blush:"
            ),
        },
    }
    HELP_BLOCK_HEADER = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "Canary help section\n"
                "Canary command formatting:\n"
                "Canary: command_word data_if_required\n\n"
                "Supported commands:\n"
            ),
        },
    }
    HELP_BLOCK_CONTENT = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "Canary: check_backlog_connection\n"
                "Canary: find_issue issue_id\n"
                "Canary: version\n"
                "Canary: create_issue description,priority\n"
                "Canary: change_status issue_id,new_status\n"
                "Canary: get_all\n"
                "Canary: register_me google_sheets_link\n"
                "Canary: add_email email"
            ),
        },
    }
    channel = None
    config = None

    def __init__(self, userid, channel, config):
        self.user_id = userid
        self.channel = channel
        self.config = config
        self.username = "canary"
        self.icon_emoji = ":robot_face:"
        self.timestamp = ""
        self.reaction_task_completed = False
        self.pin_task_completed = False

    def parseMessage(self, data_string: str):
        canary_command = data_string.startswith('Canary:')
        data = None
        keyword = None
        if not canary_command:
            return self.getHelp()
        canary_command_list = data_string.split(" ", 2)
        if len(canary_command_list) > 1:
            keyword = canary_command_list[1]
        else:
            return self.getHelp()
        if len(canary_command_list) > 2:
            data = canary_command_list[2]
        command_processor = self.resolveCommandProcessor(keyword, data)
        if command_processor is None:
            return self.getHelp()
        return command_processor.get_message_payload()

    def resolveCommandProcessor(self, keyword, data):
        if keyword == "version" and (data is None):
            return CanaryInformatic(self.channel, self.config)
        elif keyword == "help" and (data is None):
            return None
        elif keyword == "find_issue" and (data is not None):
            backlog = BacklogGetSingleManager(self.channel, self.config)
            backlog.loadDataUser(self.user_id, data)
            return backlog
        elif keyword == "create_issue" and (data is not None):
            backlog = BacklogInsertManager(self.channel, self.config)
            backlog.loadDataUser(self.user_id, data)
            return backlog
        elif keyword == "change_status" and (data is not None):
            backlog = BacklogStatusChangeManager(self.channel, self.config)
            backlog.loadDataUser(self.user_id, data)
            return backlog
        elif keyword == "get_all" and (data is None):
            backlog = BacklogGetAllManager(self.channel, self.config)
            backlog.loadDataUser(self.user_id, data)
            return backlog
        elif keyword == "register_me" and (data is not None):
            userRegister = UserManager()
            userRegister.addUser(self.user_id, data, self.channel)
            userRegister.registerUser()
            return userRegister
        elif keyword == "add_email" and (data is not None):
            userRegister = UserManager()
            userRegister.channel = self.channel
            userRegister.add_email(self.user_id, data)
            return userRegister
        else:
            return None



    def getHelp(self):
        return {
            "ts": self.timestamp,
            "channel": self.channel,
            "username": self.username,
            "icon_emoji": self.icon_emoji,
            "blocks": [
                self.WELCOME_BLOCK,
                self.DIVIDER_BLOCK,
                self.HELP_BLOCK_HEADER,
                self.DIVIDER_BLOCK,
                self.HELP_BLOCK_CONTENT,
            ],
        }