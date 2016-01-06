from errbot import BotPlugin, botcmd, webhook


class MarxBot(BotPlugin):
    """Your daily dose of Marx"""
    min_err_version = '1.6.0'

    @botcmd(split_args_with=None)
    def marx(self, message, args):
        return "what a guy"
