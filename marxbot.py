from errbot import BotPlugin, botcmd, webhook
import pytumblr


class MarxBot(BotPlugin):
    """Your daily dose of Marx"""
    min_err_version = '1.6.0'
    tumblr_client = None

    def activate(self):
        super().activate()
        if self.config is None or self.config["consumer_key"] == "" or self.config["consumer_secret"] == "":
            self.warn_admins("MarxBot must be configured with OAuth consumer key/secret")
            return
        if self.config["oauth_token"] == "" or self.config["oauth_token_secret"] == "":
            self.warn_admins("MarxBot must be configured with OAuth token key/secret (for now)")
            return
        self.tumblr_client = pytumblr.TumblrRestClient(
                self.config["consumer_key"],
                self.config["consumer_secret"],
                self.config["oauth_token"],
                self.config["oauth_token_secret"])

    def get_configuration_template(self):
        return {"consumer_key": "",
                "consumer_secret": "",
                "oauth_token": "",
                "oauth_token_secret": ""}

    @botcmd
    def marx(self, message, args):
        if self.tumblr_client is None:
            return "MarxBot must be configured and restarted to serve quotes."
        post = self.tumblr_client.posts("dailymarx", limit=1)['posts'][0]
        self['latest_post'] = post
        return str(post['text'])
