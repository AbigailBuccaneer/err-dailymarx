# marxbot

an errbot plugin that provides you with a daily Marx quote from [dailymarx.tumblr.com](https://dailymarx.tumblr.com/)

## Installing

1. [Register a tumblr application](https://www.tumblr.com/oauth/apps)
2. [Get an OAuth token](https://api.tumblr.com/console)
3. In errbot:

    !repos install https://github.com/AbigailBuccaneer/err-dailymarx.git
    !plugin config MarxBot {'consumer_key': '...',
                            'consumer_secret: '...',
                            'oauth_token': '...',
                            'oauth_token_secret': '...' }

## Using

<abigail> !marx
<MarxBot> neither thoughts nor language in themselves form a realm of their own, they are only manifestations of actual life.

## LICENSE

This code is released under the [MIT license](http://opensource.org/licenses/MIT).
