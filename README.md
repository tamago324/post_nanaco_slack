# nanaco_balance

nanaco balance display

## Usage

### Clone this repository

```sh
git clone https://github.com/tamago324/nanaco_balance.git
```

### Set environment variables

About the value to set [here](https://www.nanaco-net.jp/pc/emServlet)

1.Use direnv
2.Use Pipenv

#### 1.Use direnv

If you use direnv to set environment variables

Click [here](http://tmg0525.hatenadiary.jp/entry/2017/11/07/020609) for how to install direnv

```sh
cd nanaco_balance
echo "export NANACO_NUM='Number length 16'" > .envrc
echo "export SECURITY_CD='Number length 6'" > .envrc
direnv allow .
```

Install required modules.

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
```


### Run program.

```sh
python nanaco_zan.py

# pipenv
pipenv run python nanaco_zan.py
```

e.g.

```
2017年11月05日23時59分時点
残高：1,107円
ポイント残高：451P
```
