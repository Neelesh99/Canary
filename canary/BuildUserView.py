class BuildUserView:
    def __init__(self, user_id):
        self.message = {
            "user_id": user_id,
            "view": {
                "type": "home",
                "blocks": [
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "Hello User, Welcome to Canary Home!! Canary is a group task managment software, specifically designed for UKSDC users. It allows our different committees and groups to share their workload and update each other on their progress"
                        }
                    },
                    {
                        "type": "divider"
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "*Setting up Canary for yourself*\nCurrently canary allows a user to be registered to a single backlog per channel. To set up canary please contact Neelesh, cos he's still working on the easy onboarding feature."
                        },
                        "accessory": {
                            "type": "image",
                            "image_url": "https://i.imgur.com/7T91kCB.png",
                            "alt_text": "alt text for image"
                        }
                    },
                    {
                        "type": "divider"
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "*Canary Help*\n Canary is designed to provide a slack based interface for the Backlog sheets available on the UKSDC drive. We will be rolling out these sheets for most commitees in due course. Please see below on explanations for each Canary command."
                        },
                        "accessory": {
                            "type": "image",
                            "image_url": "https://i.imgur.com/EuNEjGk.png",
                            "alt_text": "alt text for image"
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "*Canary: version*\nSimple command that will check what version of canary is currently deployed."
                        },
                        "accessory": {
                            "type": "image",
                            "image_url": "https://avatars.slack-edge.com/2020-07-08/1230295658130_b63a694cad6d0d2ebea7_96.png",
                            "alt_text": "alt text for image"
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "*Canary: register_me [backlog token]*\nA command which will register the calling user to the backlog specified by the 'backlog token', Ask Neelesh if you haven't got your backlog token."
                        },
                        "accessory": {
                            "type": "image",
                            "image_url": "https://avatars.slack-edge.com/2020-07-08/1230295658130_b63a694cad6d0d2ebea7_96.png",
                            "alt_text": "alt text for image"
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "*Canary: get_all*\nA command which will retrieve every entry in the backlog that you belong to."
                        },
                        "accessory": {
                            "type": "image",
                            "image_url": "https://avatars.slack-edge.com/2020-07-08/1230295658130_b63a694cad6d0d2ebea7_96.png",
                            "alt_text": "alt text for image"
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "*Canary: find_issue [issue id]*\nA command which will search for the 'issue id' in the list of tasks in the backlog that you belong to\nE.g. Canary: find_issue PD-1"
                        },
                        "accessory": {
                            "type": "image",
                            "image_url": "https://avatars.slack-edge.com/2020-07-08/1230295658130_b63a694cad6d0d2ebea7_96.png",
                            "alt_text": "alt text for image"
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "*Canary: create_issue [Description of task],[priority]*\nA command which allows you to create a new task in the backlog when given a description and priority for the task\nE.g. Canary: create_issue Create a home page for Canary,High"
                        },
                        "accessory": {
                            "type": "image",
                            "image_url": "https://avatars.slack-edge.com/2020-07-08/1230295658130_b63a694cad6d0d2ebea7_96.png",
                            "alt_text": "alt text for image"
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "*Canary: change_status [issue id]*\nA command which allows you to change the status of the task\nE.g. Canary: change_status PD-1"
                        },
                        "accessory": {
                            "type": "image",
                            "image_url": "https://avatars.slack-edge.com/2020-07-08/1230295658130_b63a694cad6d0d2ebea7_96.png",
                            "alt_text": "alt text for image"
                        }
                    }
                ]
            }
        }

    def getHomeView(self):
        return self.message

