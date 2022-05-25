#  -------------------------------
#  Difficult Rocket
#  Copyright © 2021-2022 by shenjackyuanjie
#  All rights reserved
#  -------------------------------

"""
writen by shenjackyuanjie
mail:   3695888@qq.com
github: @shenjackyuanjie
gitee:  @shenjackyuanjie
"""

from . import Error


class CommandError(Error):
    """命令解析相关 error"""


class CommandParseError(CommandError):
    """命令解析时出现错误"""


class CommandQuotationMarkPositionError(CommandParseError):
    """命令中,引号位置不正确
    例如： /command "aabcc "awdawd"""


class CommandQuotationMarkMissing(CommandParseError):
    """命令中引号缺失
    例如: /command "aawwdawda awdaw """