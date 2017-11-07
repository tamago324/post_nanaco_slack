# nanaco_balance

Send nanaco balance information to Slack

## Installation

```sh
git clone https://github.com/tamago324/nanaco_balance.git
```

### Set environment variables

- 'NANACO_NUM'
    nanaco number length 16
- 'SECURITY_CD'
    security cd length 6
- 'WEBHOOK_URL'
    send channel webhook url

Click [here](https://www.nanaco-net.jp/pc/emServlet) for the value set for 'NANACO_NUM' and 'SECURITY_CD'.

About the value set for 'WEBHOOK_URL'.

Access [here](https://slack.com/services/new/incoming-webhook).Select the channel you want to send at 'Choose a channel', and click 'Add Incoming WebHooks integration'.The value of 'Webhook URL'.

1.Use direnv
2.Use Pipenv

#### 1.use direnv

if you use direnv to set environment variables

click [here](http://tmg0525.hatenadiary.jp/entry/2017/11/07/020609) for how to install direnv

```sh
cd nanaco_balance
echo "export nanaco_num='number length 16'" > .envrc
echo "export security_cd='number length 6'" > .envrc
echo "export webhook_url='webhook url'" > .envrc
direnv allow .
```

install required modules.

```sh
pip install robobrowser
```

#### 2.Use Pipenv

If you use Pipenv to set environment variables

Click [here](http://tmg0525.hatenadiary.jp/entry/2017/10/29/134453) for how to install pipenv

```sh
cd nanaco_balance
pipenv install
echo NANACO_NUM=nanacoNumber > .env
echo SECURITY_CD=securityCd > .env
echo WEBHOOK_URU=webhookUrl > .env
```


### Usage

```sh
python post_nanaco_slack.py

# pipenv
pipenv run python post_nanaco_slack.py
```

![result](https://github.com/tamago324/post_nanaco_slack/img.png)
