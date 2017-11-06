# nanaco_balance

nanaco balance display

## Usage

Clone this repository.

```sh
git clone https://github.com/tamago324/nanaco_balance.git
```

Use direnv.

Click [here](http://tmg0525.hatenadiary.jp/entry/2017/11/07/020609) for how to install direnv

About the value to set [here](https://www.nanaco-net.jp/pc/emServlet)

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

Run program.

```sh
python nanaco_zan.py
```

Example result.

```
2017年11月05日23時59分時点
残高：1,107円
ポイント残高：451P
```
