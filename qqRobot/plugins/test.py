from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event

weather = on_command("你好", priority=5)


@weather.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    # await bot.send(event,"[CQ:image,file=http://oss.youji999.top/images/2020/08/27/1598503009582813.jpg]")
    await weather.finish("👋")


record = on_command("语音", priority=5)
@record.handle()
async def handle_record(bot: Bot, event: Event, state: T_State):
    res = "[CQ:tts,text=你是猪吗]"
    await record.finish(res)
