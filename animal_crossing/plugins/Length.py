from nonebot import on_command, CommandSession
from .Object import Room

@on_command('len', aliases=('length', '排队长度', '等待人数', '查看队列等待人数'), only_to_me=False)
async def len(session: CommandSession):
    user = session.event['user_id']
    room = Room()
    room.getQueue()
    roomID = room.inMember(user)
    queueID = room.inQueue(user)
    if roomID:
        await session.send(f"\n您已在房间【{roomID}】中", at_sender=True)
    elif queueID:
        output = f"\n你正在房间【{queueID}】的队列中\n前方排队人数为：{room.getWaitLen(session.event['user_id'])}" if room.getWaitLen(session.event['user_id']) else "当前不在队列中"
        await session.send(output, at_sender=True)
    else:
        output = "您不在任何队列中"
        await session.send(output, at_sender=True)