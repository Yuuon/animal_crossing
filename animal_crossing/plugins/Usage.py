from nonebot import on_command, CommandSession
import config

GROUP_COMMANDLIST = """
【目前支持中英文"/" "!" "#"作为命令识别符】
私聊命令需要加bot的QQ好友进行私聊命令
必须加好友！必须加好友！必须加好友！
bot的QQ号为：2750447037
加好友后输入 /帮助 命令查看帮助文档"""

COMMANDLIST = """帮助文档：
/查看  
说明：查看所有岛
--------------------
/开门 (需私聊)
说明：需要提供岛密码和大头菜价格
格式1：/开门 岛密码|价格|最大登岛人数(可选，默认""" + str(config.DEFAULT_CAPACITY) + """"人)
格式2：/开门 岛密码|备注(非纯数字)|最大登岛人数(可选，默认""" + str(config.DEFAULT_CAPACITY) + """"人)
示例1：/开门 GTX98|605
示例2：/开门 GTX98|605|4
示例3：/开门 GTX98|猫头鹰妹妹|4
--------------------
/关门 (需私聊)
说明：关闭自己的岛
示例：/关门
--------------------
/成员 (需私聊)
说明：查看你岛上当前的成员的QQ昵称和QQ号
示例：/成员
--------------------
/重开 (需私聊)
说明：更新岛密码和最大登岛人数，炸岛时使用
格式：/重开 岛密码|最大登岛人数(可选)
示例1：/重开 GTX98
示例2：/重开 GTX98|2
--------------------
/备注
说明：修改备注房备注
格式：/备注 备注内容
示例1：/备注 猫头鹰妹妹
--------------------
/踢人 (需私聊)
说明：根据QQ号移除当前在你岛上人员
格式：/踢人 QQ号
示例1：/踢人 1702955399
示例2（移除全部人员）：/踢人 全部
--------------------
/排队 (需私聊)
格式：/排队 岛ID
示例：/排队 5
--------------------
/准备 (需私聊)
说明：排队排到你时需要在2分钟内该命令，
准备后才能获取到岛密码
示例：/准备
--------------------
/等待人数 (需私聊)
说明：查看队列你前方的等待人数
并显示当前在岛上的人员QQ昵称和QQ号
--------------------
/退出 (需私聊)
说明：退出当前所在岛"""


# 使用帮助
@on_command('help', aliases=('帮助', '命令', '查看帮助'), only_to_me=False)
async def usage(session: CommandSession):
    if session.event['message_type'] == 'private':
        await session.send(COMMANDLIST)
    else:
        await session.send(GROUP_COMMANDLIST, at_sender=True)
