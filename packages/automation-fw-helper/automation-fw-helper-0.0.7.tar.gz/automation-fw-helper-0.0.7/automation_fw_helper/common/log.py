# -*- coding: utf-8 -*-
"""
# ---------------------------------------------------------------------------------------------------------
# ProjectName:  automation-fw-helper
# FileName:     log.py
# Description:  TODO
# Author:       mfkifhss2023
# CreateDate:   2024/06/03
# Copyright ©2011-2024. Hunan xxxxxxx Company limited. All rights reserved.
# ---------------------------------------------------------------------------------------------------------
"""
import logging


def init_airtest_log(is_enable: bool, level: int = logging.WARNING):
    log = logging.getLogger("airtest")
    if is_enable is True:
        log.setLevel(level=level)
    else:
        # 移除所有处理器
        for handler in log.handlers[:]:
            log.removeHandler(handler)


logger = logging.getLogger("root")
