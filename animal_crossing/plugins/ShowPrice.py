from nonebot import on_command, CommandSession
from .PriceList import Price
import config


@on_command('price', aliases=('查看价格',), only_to_me=False)
async def show(session: CommandSession):
    price = Price()
    await session.send(price.toString(config.GROUP_ID))
