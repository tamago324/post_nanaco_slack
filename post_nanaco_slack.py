#!/usr/bin/env python

from robobrowser import RoboBrowser
import os
from nanaco import Nanaco
from slack_bot import SlackBot


LOGIN_URL = 'https://www.nanaco-net.jp/pc/emServlet'
MIN_MONEY = 700


def main():
    browser = openbrowser(LOGIN_URL)
    login(browser)
    # Generate nanaco object
    nanaco = generate_nanaco(browser)

    # 設定額よりも低かった場合送信
    if nanaco.money <= MIN_MONEY:
        slackBot = SlackBot('nanacoBot')
        slackBot.post_nanaco_status(nanaco)

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

    form['XCID'].value = os.environ['NANACO_NUM']
    form['SECURITY_CD'].value = os.environ['SECURITY_CD']
    
    browser.submit_form(form)


def generate_nanaco(browser):
    ''' Generate nanaco object fo browser data
    :param RoboBworser: Logined browser
    :return: nanaco
    '''
    nanaco = Nanaco()
    nanaco.time = browser.select('#cardzan > span.time')[0].text

    # 数値のみを取り出す
    nanaco.money = int(browser.select('#memberInfoFull > .detailBox > .moneyBox > .fRight > p') \
                   [0].text[:-1].replace(',',''))
    nanaco.point = int(browser.select('#memberInfoFull > .detailBox > .pointBox > .fRight > p') \
                   [0].text[:-1].replace(',',''))

    return nanaco


if __name__ == '__main__':
    main()
