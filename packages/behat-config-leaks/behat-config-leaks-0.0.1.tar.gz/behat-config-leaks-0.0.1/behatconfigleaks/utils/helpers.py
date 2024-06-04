#!/usr/bin/env python

"""
 * behat-config-leaks
 * behat-config-leaks Bug scanner for WebPentesters and Bugbounty Hunters
 *
 * @Developed By Cappricio Securities <https://cappriciosec.com>
 */

"""
import getpass
username = getpass.getuser()


def display_help():
    help_banner = f"""

👋 Hey \033[96m{username}
   \033[92m                                                                          v1.0
    __         __          __                         _____             __           __
   / /_  ___  / /_  ____ _/ /_      _________  ____  / __(_)___ _      / /__  ____ _/ /_______
  / __ \/ _ \/ __ \/ __ `/ __/_____/ ___/ __ \/ __ \/ /_/ / __ `/_____/ / _ \/ __ `/ //_/ ___/
 / /_/ /  __/ / / / /_/ / /_/_____/ /__/ /_/ / / / / __/ / /_/ /_____/ /  __/ /_/ / ,< (__  )
/_.___/\___/_/ /_/\__,_/\__/      \___/\____/_/ /_/_/ /_/\__, /     /_/\___/\__,_/_/|_/____/
                                                        /____/

                              \033[0mDeveloped By \x1b[31;1m\033[4mhttps://cappriciosec.com\033[0m


\x1b[31;1mbehat-config-leaks : Bug scanner for WebPentesters and Bugbounty Hunters

\x1b[31;1m$ \033[92mbehat-config-leaks\033[0m [option]

Usage: \033[92mbehat-config-leaks\033[0m [options]

Options:
  -u, --url     URL to scan                                behat-config-leaks -u https://target.com
  -i, --input   <filename> Read input from txt             behat-config-leaks -i target.txt
  -o, --output  <filename> Write output in txt file        behat-config-leaks -i target.txt -o output.txt
  -c, --chatid  Creating Telegram Notification             behat-config-leaks --chatid yourid
  -b, --blog    To Read about behat-config-leaks Bug       behat-config-leaks -b
  -h, --help    Help Menu
    """
    print(help_banner)


def banner():
    help_banner = f"""
    \033[94m
👋 Hey \033[96m{username}
      \033[92m                                                                      v1.0
    __         __          __                         _____             __           __
   / /_  ___  / /_  ____ _/ /_      _________  ____  / __(_)___ _      / /__  ____ _/ /_______
  / __ \/ _ \/ __ \/ __ `/ __/_____/ ___/ __ \/ __ \/ /_/ / __ `/_____/ / _ \/ __ `/ //_/ ___/
 / /_/ /  __/ / / / /_/ / /_/_____/ /__/ /_/ / / / / __/ / /_/ /_____/ /  __/ /_/ / ,< (__  )
/_.___/\___/_/ /_/\__,_/\__/      \___/\____/_/ /_/_/ /_/\__, /     /_/\___/\__,_/_/|_/____/
                                                        /____/
                                                        
                              \033[0mDeveloped By \x1b[31;1m\033[4mhttps://cappriciosec.com\033[0m


\x1b[31;1mbehat-config-leaks : Bug scanner for WebPentesters and Bugbounty Hunters

\033[0m"""
    print(help_banner)
