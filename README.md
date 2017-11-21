# post_nanaco_slack

ナナコの残高情報を Slack に送信する

## インストール方法

```sh
git clone https://github.com/tamago324/nanaco_balance.git
```

### 環境変数を設定する

- 'NANACO_NUM'
    ナナコの16桁の番号
- 'SECURITY_CD'
    ナナコの6桁のセキュリティCD
- 'WEBHOOK_URL'
    ナナコの残高情報を送信するチャンネルのWebHook URL

'NANACO_NUM' と 'SECURITY_CD' については[ここ](https://www.nanaco-net.jp/pc/emServlet)を見てください

'WEBHOOK_URL' に設定する値について

ここにアクセスして、`Choose a channel` で送信先のチャンネルを選択して、`Add Incoming WebHooks integration`をクリックする。表示されている`Webhook URL`を設定する。

環境変数を設定する方法は２つある

1.direnvを使う
2.Pivenvを使う

#### 1.direnvを使う

direnvを使って環境変数を設定する場合

direnvのインストール方法については[ここ](http://tmg0525.hatenadiary.jp/entry/2017/11/07/020609)に書いてある

以下のように設定する

```sh
cd nanaco_balance
echo "export nanaco_num='number length 16'" > .envrc
echo "export security_cd='number length 6'" > .envrc
echo "export webhook_url='webhook url'" > .envrc
direnv allow .
```

必要なライブラリをインストールする

```sh
pip install robobrowser
```

#### 2.Pipenvを使う

Pipenvを使って環境変数を設定する場合

Pipenvのインストール方法と説明は[ここ](http://tmg0525.hatenadiary.jp/entry/2017/10/29/134453)に書いてある

以下のように設定する

```sh
cd nanaco_balance
pipenv install
echo NANACO_NUM=nanacoNumber > .env
echo SECURITY_CD=securityCd > .env
echo WEBHOOK_URU=webhookUrl > .env
```


## 使い方

```sh
# direnvの場合
python post_nanaco_slack.py

# Pipenvの場合
pipenv run python post_nanaco_slack.py
```

![result](https://github.com/tamago324/post_nanaco_slack/blob/master/img.png?raw=true)

<br>

---

# post_nanaco_slack

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


## Usage

```sh
python post_nanaco_slack.py

# pipenv
pipenv run python post_nanaco_slack.py
```

![result](https://github.com/tamago324/post_nanaco_slack/blob/master/img.png?raw=true)
