#!/usr/bin/env python

"""
 * behat-config-leaks
 * behat-config-leaks Bug scanner for WebPentesters and Bugbounty Hunters
 *
 * @Developed By Cappricio Securities <https://cappriciosec.com>
 */
"""
import requests
from behatconfigleaks.utils import const
from behatconfigleaks.utils import configure


def sendmessage(vul):

    data = {"Tname": "behat-config-leaks", "chatid": configure.get_chatid(), "data": vul,
            "Blog": const.Data.blog, "bugname": const.Data.bugname, "Priority": "Medium"}

    headers = {
        "Content-Type": "application/json",
    }

    try:
        response = requests.put(const.Data.api, json=data, headers=headers)
    except:
        print("Bot Error")
