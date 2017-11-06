#!/bin/usr/env python

from robobrowser import RoboBrowser
import os


LOGIN_URL = 'https://www.nanaco-net.jp/pc/emServlet'
# direnvなどを使い、環境変数に番号を格納しておく
NANACO_NUM = os.environ['NANACO_NUM']
SECURITY_CD = os.environ['SECURITY_CD']


def main():
    browser = openbrowser(LOGIN_URL)
    login(browser)
    display_balance(browser)

def openbrowser(url):
    ''' Open url on RoboBrowser.
    :param str url: Opened url
    :return: Opened url RoboBrowser
    '''

    browser = RoboBrowser(parser='html.parser')
    browser.open(url)
    return browser


def login(browser, nanacoNum=None, securityCd=None):
    ''' Login nanaco Web site
    :param RoboBrowser browser: Opened url RoboBrowser
    :param int nanacoNum: Nanaco number length 16
    :param int securityCd: Security cd length 6
    '''
    
    form = browser.get_form(id='login_card')

    if nanacoNum is not None:
        form['XCID'].value = nanacoNum
    else:
        form['XCID'].value = NANACO_NUM

    if securityCd is not None:
        form['SECURITY_CD'].value = securityCd
    else:
        form['SECURITY_CD'].value = SECURITY_CD

    browser.submit_form(form)


def display_balance(browser):
    ''' Display balance yesterday at 23:59
    :param RoboBworser: Logined browser
    '''

    time = browser.select('#cardzan > span.time')[0].text
    balance = browser.select('#memberInfoFull > .detailBox > .moneyBox > .fRight > p')[0].text
    point = browser.select('#memberInfoFull > .detailBox > .pointBox > .fRight > p')[0].text
    print((f'{time}\n'
           f'残高：{balance}\n'
           f'ポイント残高：{point}'
           ))


if __name__ == '__main__':
    main()
