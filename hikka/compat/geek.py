# ©️ Dan Gazizullin, 2021-2023
# This file is a part of Hikka Userbot
# 🌐 https://github.com/hikariatama/Hikka
# You can redistribute it and/or modify it under the terms of the GNU AGPLv3
# 🔑 https://www.gnu.org/licenses/agpl-3.0.html
# Netfoll Team modifided Hikka files for Netfoll
# 🌐 https://github.com/MXRRI/Netfoll

import re


def compat(code: str) -> str:
    """
    Reformats modules, built for GeekTG to work with Netfoll
    :param code: code to reformat
    :return: reformatted code
    """
    return "\n".join(
        [
            re.sub(
                r"^( *)from \.\.inline import (.+)$",
                r"\1from ..inline.types import \2",
                re.sub(
                    r"^( *)from \.\.inline import rand[^,]*$",
                    "\1from ..utils import rand",
                    re.sub(
                        r"^( *)from \.\.inline import rand, ?(.+)$",
                        r"\1from ..inline.types import \2\n\1from ..utils import rand",
                        re.sub(
                            r"^( *)from \.\.inline import (.+), ?rand[^,]*$",
                            r"\1from ..inline.types import \2\n\1from ..utils import"
                            r" rand",
                            re.sub(
                                r"^( *)from \.\.inline import (.+), ?rand, ?(.+)$",
                                r"\1from ..inline.types import \2, \3\n\1from ..utils"
                                r" import rand",
                                line.replace("GeekInlineQuery", "InlineQuery").replace(
                                    "self.inline._bot",
                                    "self.inline.bot",
                                ),
                                flags=re.M,
                            ),
                            flags=re.M,
                        ),
                        flags=re.M,
                    ),
                    flags=re.M,
                ),
                flags=re.M,
            )
            for line in code.splitlines()
        ]
    )
