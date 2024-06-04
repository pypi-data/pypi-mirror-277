#!/usr/bin/env python

"""
 * appspec-yaml-leaks
 * appspec-yaml-leaks Bug scanner for WebPentesters and Bugbounty Hunters
 *
 * @Developed By Cappricio Securities <https://cappriciosec.com>
 */
"""
import requests
from appspecyamlleaks.utils import const
from appspecyamlleaks.utils import configure


def sendmessage(vul):

    data = {"Tname": "appspec-yaml-leaks", "chatid": configure.get_chatid(), "data": vul,
            "Blog": const.Data.blog, "bugname": const.Data.bugname, "Priority": "Medium"}

    headers = {
        "Content-Type": "application/json",
    }

    try:
        response = requests.put(const.Data.api, json=data, headers=headers)
    except:
        print("Bot Error")
