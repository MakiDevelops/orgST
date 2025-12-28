# Prompts for orgfetch/main
from os import getcwd

from texts.info import (
    contributors,
    date_edited,
    host,
    main_authors,
    spdxid,
    terminal_name,
    user,
    version,
)

border = "+---------------------------+"
ticon = "[>] "

mprompt = f"""
{terminal_name} {version}.
{user}@{host}
Last edited: {date_edited}
{getcwd()}
{border}
"""

ftprompt = f"""
{border}
a cool open source terminal made by some people
Main authors: {main_authors}
Contributors: {contributors}
{terminal_name} {version}.
{user}@{host}
Last edited: {date_edited}
{border}
Copyright (c) 2025 Wdboyes13, MakiDevelops. All rights reserved.
SPDX-License-Identifier:{spdxid}
{border}
"""
