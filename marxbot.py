from time import time

from errbot import BotPlugin, botcmd, webhook
import pytumblr


class MarxBot(BotPlugin):
    """Your daily dose of Marx"""
    min_err_version = '1.6.0'
    tumblr_client = None
    poll_interval = 60 * 15

    class NotConfiguredError(Exception):
        pass

    def activate(self):
        super().activate()
        if self.config is None or self.config["consumer_key"] == "" or \
                self.config["consumer_secret"] == "":
            self.warn_admins(
                    "MarxBot must be configured with OAuth consumer key/secret"
            )
            return
        if self.config["oauth_token"] == "" or \
                self.config["oauth_token_secret"] == "":
            self.warn_admins(
                    "MarxBot must be configured with OAuth token key/secret "
                    "(for now)")
            return
        self.tumblr_client = pytumblr.TumblrRestClient(
                self.config["consumer_key"],
                self.config["consumer_secret"],
                self.config["oauth_token"],
                self.config["oauth_token_secret"])
        self.start_poller(self.poll_interval, self.fetch_latest_post)

    def get_configuration_template(self):
        return {"consumer_key": "",
                "consumer_secret": "",
                "oauth_token": "",
                "oauth_token_secret": ""}

    def fetch_latest_post(self):
        if 'last_fetch' in self.keys() and \
                time() - self['last_fetch'] < self.poll_interval:
            return
        if self.tumblr_client is None:
            raise MarxBot.NotConfiguredError(
                    "MarxBot must be configured and restarted to fetch quotes."
            )
        post = self.tumblr_client.posts("dailymarx", limit=1)['posts'][0]
        self['last_fetch'] = time()
        if self['latest_post'] is None or \
                self['latest_post']['id'] != post['id']:
            self.handle_new_post(post)

    @botcmd
    def marx(self, message, args):
        self.fetch_latest_post()
        return str(self['latest_post']['text'])

    def handle_new_post(self, post):
        # TODO here we should broadcast to all rooms that we're in
        pass
