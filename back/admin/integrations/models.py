import json
import uuid

import requests
from django.db import models
from django.template import Context, Template
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from fernet_fields import EncryptedTextField

INTEGRATION_OPTIONS = (
    (0, _("Slack bot")),
    (1, _("Slack account creation")),
    (2, _("Google account creation")),
    (3, _("Google Login")),
    (4, _("Asana")),
)
INTEGRATION_OPTIONS_URLS = [
    {
        "create_url": reverse_lazy("settings:slack-bot"),
        "disabled": False,
        "disable_url": reverse_lazy("settings:google-login"),
        "extra_action_url": "settings:slack-account-update-channels",
        "extra_action_text": _("Update Slack channels list"),
    },
    {
        "disabled": True,
        "create_url": reverse_lazy("settings:slack-account"),
        "disable_url": reverse_lazy("settings:google-login"),
    },
    {
        "disabled": False,
        "create_url": reverse_lazy("settings:google-account"),
        "disable_url": reverse_lazy("settings:google-account"),
    },
    {
        "disabled": False,
        "create_url": reverse_lazy("settings:google-login"),
        "disable_url": reverse_lazy("settings:google-account"),
    },
    {
        "disabled": False,
        "create_url": reverse_lazy("settings:asana"),
        "disable_url": reverse_lazy("settings:asana"),
    },
]


class IntegrationManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

    def account_provision_options(self):
        return self.get_queryset().filter(integration=10)


class Integration(models.Model):
    name = models.CharField(max_length=300, default="", blank=True)
    integration = models.IntegerField(choices=INTEGRATION_OPTIONS)
    token = EncryptedTextField(max_length=10000, default="", blank=True)
    refresh_token = EncryptedTextField(max_length=10000, default="", blank=True)
    base_url = models.CharField(max_length=22300, default="", blank=True)
    redirect_url = models.CharField(max_length=22300, default="", blank=True)
    account_id = models.CharField(max_length=22300, default="", blank=True)
    active = models.BooleanField(default=True)
    ttl = models.IntegerField(null=True, blank=True)
    expiring = models.DateTimeField(null=True, blank=True)
    one_time_auth_code = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True
    )

    manifest = models.JSONField(default=dict)
    # example
    # {
    #     "headers": {
    #         "Content-Type": "application/json",
    #         "Accept": "application/json",
    #         "Authorization": "Bearer {{TOKEN}}"
    #     },
    #     "form": [{
    #         "id": "TEAM_ID",
    #         "name": "Select team to add user to",
    #         "url": "https://app.asana.com/api/1.0/organizations/{{ORG}}/teams",
    #         "type": "multiple_choice",
    #         "items": "data",
    #         "choice_id": "data.gid",
    #         "choice_name": "data.name",
    #         "multiple": false
    #     }],
    #     "exists": {
    #         "method": "GET",
    #         "url": "https://app.asana.com/api/1.0/users/{{email}}",
    #         "data": {
    #             "data": {
    #                 "user": "{{email}}"
    #             }
    #         },
    #         "expected": "{{email}}"
    #     },
    #     "execute": [{
    #             "method": "POST",
    #             "url": "https://app.asana.com/api/1.0/workspaces/{{ORG}}/addUser",
    #             "data": {
    #                 "data": {
    #                     "user": "{{email}}"
    #                 }
    #             }
    #         },
    #         {
    #             "method": "POST",
    #             "url": "https://app.asana.com/api/1.0/teams/{{TEAM_ID}}/addUser",
    #             "data": {
    #                 "data": {
    #                     "user": "{{email}}"
    #                 }
    #             }
    #         }
    #     ],
    #     "initial_data_form": [{
    #             "id": "TOKEN",
    #             "name": "Please put your token here",
    #             "description": "You can find your token here: https://...."
    #         },
    #         {
    #             "id": "ORG",
    #             "name": "Organization id",
    #             "description": "You can find your organization id here: https://..."
    #         }
    #     ]
    # }

    extra_args = models.JSONField(default=dict)
    # Real output:
    # {
    #      "TOKEN": "xxxxx",
    #      "ORG": "org-token"
    # }

    # Slack
    app_id = models.CharField(max_length=100, default="")
    client_id = models.CharField(max_length=100, default="")
    client_secret = models.CharField(max_length=100, default="")
    signing_secret = models.CharField(max_length=100, default="")
    verification_token = models.CharField(max_length=100, default="")
    bot_token = EncryptedTextField(max_length=10000, default="", blank=True)
    bot_id = models.CharField(max_length=100, default="")

    def _run_request(self, data):
        url = self._replace_vars(data["url"])
        if "data" in data:
            post_data = json.loads(self._replace_vars(json.dumps(data["data"])))
        else:
            post_data = {}
        return requests.request(
            data["method"], url, headers=self._headers, data=post_data
        ).json()

    def _replace_vars(self, text):
        if hasattr(self, "new_hire") and self.new_hire is not None:
            text = self.new_hire.personalize(text, self.extra_args)
        t = Template(text)
        context = Context(self.extra_args)  # | self.params)
        text = t.render(context)
        return text

    @property
    def _headers(self):
        new_headers = {}
        for key, value in self.manifest["headers"].items():
            new_headers[self._replace_vars(key)] = self._replace_vars(value)
        return new_headers

    def user_exists(self, new_hire):
        self.new_hire = new_hire
        return self._replace_vars(self.manifest["exists"]["expected"]) in json.dumps(
            self._run_request(self.manifest["exists"])
        )

    def execute(self, new_hire, params):
        self.parms = params
        self.new_hire = new_hire
        for item in self.manifest.execute:
            self._run_request(item)

    def config_form(self, data=None):
        from .forms import IntegrationConfigForm

        return IntegrationConfigForm(instance=self, data=data)

    objects = IntegrationManager()
