import json

import slack_sdk
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.cache import cache

from admin.integrations.models import Integration


class Slack:
    def __init__(self):
        if not settings.FAKE_SLACK_API:
            try:
                team = Integration.objects.get(integration=0)
                self.client = slack_sdk.WebClient(token=team.token)
            except Integration.DoesNotExist:
                raise Exception("Access token not available")

    def get_channels(self):
        try:
            response = self.client.api_call(
                "conversations.list",
                data={
                    "exclude_archived": True,
                    "types": "public_channel,private_channel",
                },
            )
        except Exception:
            return []
        return [[x["name"], x["is_private"]] for x in response["channels"]]

    def get_all_users(self):
        try:
            response = self.client.api_call("users.list")
        except Exception:
            return []
        return response["members"]

    def find_by_email(self, email):
        try:
            response = self.client.api_call(
                "users.lookupByEmail", data={"email": email}
            )
        except Exception:
            return False
        return response

    def find_user_by_id(self, id):
        try:
            response = self.client.api_call("users.info", data={"user": id})["user"]
        except Exception:
            return False
        return response

    def update_message(self, blocks=[], channel="", timestamp=0):
        # if there is no channel, then drop
        if channel == "" or timestamp == 0:
            return False

        if settings.FAKE_SLACK_API:
            cache.set("slack_channel", channel)
            cache.set("slack_ts", timestamp)
            cache.set("slack_blocks", json.dumps(blocks))
            return

        return self.client.chat_update(
            channel=channel,
            ts=timestamp,
            blocks=blocks,
        )

    def send_message(self, blocks=[], channel=""):
        # if there is no channel, then drop
        if channel == "":
            return False

        print(blocks)
        if settings.FAKE_SLACK_API:
            cache.set("slack_channel", channel)
            cache.set("slack_blocks", blocks)
            return

        return self.client.chat_postMessage(channel=channel, blocks=blocks)

    def delete_message(self, ts=0, channel=""):
        if settings.FAKE_SLACK_API:
            cache.set("slack_channel", channel)
            cache.set("slack_ts", json.dumps(ts))
            return

        return self.client.chat_delete(channel=channel, ts=ts)

    def open_modal(self, trigger_id, view):
        if settings.FAKE_SLACK_API:
            cache.set("slack_trigger_id", trigger_id)
            cache.set("slack_view", json.dumps(view))
            return

        return self.client.views_open(trigger_id=trigger_id, view=view)

    def update_modal(self, view_id, view):
        if settings.FAKE_SLACK_API:
            cache.set("slack_view_id", view_id)
            cache.set("slack_view", json.dumps(view))
            return

        return self.client.views_update(view_id=view_id, view=view)


def paragraph(text):
    return {"type": "section", "text": {"type": "mrkdwn", "text": text}}


def actions(elements=[]):
    return {"type": "actions", "elements": elements}


def button(text, style, value, action_id=""):
    if action_id == "":
        action_id = value
    return {
        "type": "button",
        "text": {"type": "plain_text", "text": text},
        "style": style,
        "value": value,
        "action_id": action_id,
    }


def has_slack_account(user_id):
    return get_user_model().objects.filter(slack_user_id=user_id).exists()
