__version__ = (0, 0, 2)

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.types import Message

from .. import loader, utils


class HetaSearcherMod(loader.Module):
    """search a modules in @hikkamods_bot"""

    strings = {"name": "HetaSearcher", "mod": "<b>👇 Probably this module</b>"}
    strings_ru = {"mod": "<b>👇 Вероятно, это этот модуль</b>"}

    async def hetacmd(self, event):
        "<module name>"
        args = utils.get_args_raw(event)
        result = await event.client.inline_query("hikkamods_bot", args)
        await result[0].click(event.to_id)
        await event.edit(self.strings("mod"))