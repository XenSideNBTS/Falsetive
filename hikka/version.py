"""Represents current userbot version"""
# ©️ Dan Gazizullin, 2021-2023
# This file is a part of Hikka Userbot
# 🌐 https://github.com/hikariatama/Hikka
# You can redistribute it and/or modify it under the terms of the GNU AGPLv3
# 🔑 https://www.gnu.org/licenses/agpl-3.0.html
# falsetive Team modifided Hikka files for falsetive
# 🌐 https://github.com/XenSideNBTS/falsetive

__version__ = (0, 1, 4)
netver = (0, 1, 4)
netrev = ""
import os
import git

try:
    branch = git.Repo(
        path=os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    ).active_branch.name
except Exception:
    branch = "stable"
