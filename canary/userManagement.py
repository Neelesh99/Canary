from canary.canaryBaseCommandProcessor import BaseCommandProcessor


class UserManager(BaseCommandProcessor):
    file = 'user_store.txt'
    emails = 'email_store.txt'
    user_id = None
    google_sheet = None
    channel = None
    new_sheet = None

    def getUser(self, user_id):
        fileData = open(self.file)
        data = list(fileData)
        for line in data:
            if user_id in line:
                try:
                    self.google_sheet = line.split('=')[1]
                    fileData.close()
                    return True
                except Exception:
                    fileData.close()
                    return False
        fileData.close()
        return False

    def getUserChannel(self, user_id, channel_id):
        fileData = open(self.file)
        data = list(fileData)
        for line in data:
            if user_id in line:
                try:
                    dataline = line.split('=')[1]
                    dataList = dataline.split(',')
                    for entry in dataList:
                        if channel_id in entry:
                            self.google_sheet = entry.split('#')[1]
                            if self.google_sheet[len(self.google_sheet) - 1] != '\n':
                                self.google_sheet = self.google_sheet + '\n'
                            fileData.close()
                            return True
                    fileData.close()
                    return False
                except Exception:
                    fileData.close()
                    return False
        fileData.close()
        return False

    def addUser(self, user_id, google_sheets_link, channel):
        self.user_id = user_id
        self.google_sheet = google_sheets_link
        self.new_sheet = google_sheets_link
        self.channel = channel

    def registerUser(self):

        if not self.getUser(self.user_id):
            string = self.user_id + '=' + self.channel + '#https://script.google.com/macros/s/' + self.new_sheet + '\n'
            fileData = open(self.file, 'a')
            fileData.write(string)
            fileData.close()
        else:
            adjust = self.channel + '#https://script.google.com/macros/s/' + self.new_sheet
            string = self.user_id + '=' + self.google_sheet[:-1] + "," + adjust
            fileDataRead = open(self.file, 'r+')
            fileList = list(fileDataRead)
            fileDataRead.close()
            fileData = open(self.file, 'w')
            index = self.getIndex(fileList, self.user_id)
            fileList[index] = string
            fileData.writelines(fileList)
            fileData.close()

    def add_email(self, user_id, email):
        fileData = open(self.emails, 'a')
        email = email.split(':')[1]
        email = email.split('|')[0]
        string = user_id + '=' + email + '\n'
        fileData.write(string)

    def get_email(self, user_id):
        fileData = open(self.emails, 'r')
        fileList = list(fileData)
        for line in fileList:
            if user_id in line:
                fileData.close()
                return line.split('=')[1]
        fileData.close()
        return 'n.ravichandran@uksdc.org'

    def getIndex(self, list, val):
        for line in range(len(list)):
            if val in list[line]:
                return line
        return -1

    def get_message_payload(self):
        return {
            "ts": "",
            "channel": self.channel,
            "username": "canary",
            "icon_emoji": ":robot_face:",
            "blocks": [
                {"type": "section", "text": {"type": "mrkdwn", "text": "User registered"}}
            ],
        }

    def getGoogleFilesLink(self):
        return self.google_sheet