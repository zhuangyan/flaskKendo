#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''''
Created on
@author: zhuangyan
'''
import datetime
import json
import os
import uuid

from bson import ObjectId
from flask import Flask, Response, jsonify, request, session
from flask_uploads import UploadSet, extension
from PIL import Image

from com import choices
# from com.db import MongoDB, Database
from com.minerequest import MineAuthentic
from com.utils import encrypt_password
from app import mongo

from . import api


@api.route('/homestat',methods=['POST'])
@MineAuthentic.auth(request)
def getHomeStat():
    result = {
                "result": "y",
                "msg": "欢迎登录 Kendo UI Admin 后台管理系统 =^^=",
                "count": {
                    "pv_count": 8901,
                    "visit_count": 1699,
                    "visitor_count": 1245,
                    "ip_count": 998
                },
                "area": [
                    {
                        "category": "2018-05",
                        "pv_count": 1191,
                        "visitor_count": 170
                    },
                    {
                        "category": "",
                        "pv_count": 973,
                        "visitor_count": 106
                    },
                    {
                        "category": "",
                        "pv_count": 583,
                        "visitor_count": 114
                    },
                    {
                        "category": "2018-08",
                        "pv_count": 522,
                        "visitor_count": 110
                    },
                    {
                        "category": "",
                        "pv_count": 370,
                        "visitor_count": 88
                    },
                    {
                        "category": "",
                        "pv_count": 665,
                        "visitor_count": 86
                    },
                    {
                        "category": "2018-11",
                        "pv_count": 769,
                        "visitor_count": 133
                    },
                    {
                        "category": "",
                        "pv_count": 2194,
                        "visitor_count": 255
                    },
                    {
                        "category": "",
                        "pv_count": 765,
                        "visitor_count": 113
                    },
                    {
                        "category": "2019-02",
                        "pv_count": 869,
                        "visitor_count": 70
                    }
                ],
                "donut": [
                    {
                        "category": "新访客",
                        "value": 0.5579
                    },
                    {
                        "category": "老访客",
                        "value": 0.4421
                    }
                ],
                "bar": [
                    {
                        "category": "浏览量",
                        "pc": 8608,
                        "mobile": 293
                    },
                    {
                        "category": "访问次数",
                        "pc": 1575,
                        "mobile": 124
                    },
                    {
                        "category": "访客数",
                        "pc": 1107,
                        "mobile": 119
                    },
                    {
                        "category": "IP 数",
                        "pc": 994,
                        "mobile": 118
                    }
                ],
                "line": [
                    {
                        "category": "0点",
                        "pv_count": 22,
                        "visit_count": 12,
                        "visitor_count": 12,
                        "new_visitor_count": 6,
                        "ip_count": 12
                    },
                    {
                        "category": "",
                        "pv_count": 23,
                        "visit_count": 6,
                        "visitor_count": 6,
                        "new_visitor_count": 4,
                        "ip_count": 5
                    },
                    {
                        "category": "",
                        "pv_count": 27,
                        "visit_count": 8,
                        "visitor_count": 7,
                        "new_visitor_count": 4,
                        "ip_count": 7
                    },
                    {
                        "category": "3点",
                        "pv_count": 15,
                        "visit_count": 5,
                        "visitor_count": 5,
                        "new_visitor_count": 1,
                        "ip_count": 5
                    },
                    {
                        "category": "",
                        "pv_count": 5,
                        "visit_count": 3,
                        "visitor_count": 3,
                        "new_visitor_count": 3,
                        "ip_count": 3
                    },
                    {
                        "category": "",
                        "pv_count": 23,
                        "visit_count": 10,
                        "visitor_count": 9,
                        "new_visitor_count": 9,
                        "ip_count": 10
                    },
                    {
                        "category": "6点",
                        "pv_count": 6,
                        "visit_count": 4,
                        "visitor_count": 4,
                        "new_visitor_count": 4,
                        "ip_count": 3
                    },
                    {
                        "category": "",
                        "pv_count": 14,
                        "visit_count": 7,
                        "visitor_count": 7,
                        "new_visitor_count": 7,
                        "ip_count": 7
                    },
                    {
                        "category": "",
                        "pv_count": 201,
                        "visit_count": 108,
                        "visitor_count": 108,
                        "new_visitor_count": 15,
                        "ip_count": 91
                    },
                    {
                        "category": "9点",
                        "pv_count": 488,
                        "visit_count": 77,
                        "visitor_count": 63,
                        "new_visitor_count": 25,
                        "ip_count": 43
                    },
                    {
                        "category": "",
                        "pv_count": 444,
                        "visit_count": 60,
                        "visitor_count": 35,
                        "new_visitor_count": 12,
                        "ip_count": 23
                    },
                    {
                        "category": "",
                        "pv_count": 368,
                        "visit_count": 42,
                        "visitor_count": 30,
                        "new_visitor_count": 19,
                        "ip_count": 27
                    },
                    {
                        "category": "12点",
                        "pv_count": 88,
                        "visit_count": 29,
                        "visitor_count": 23,
                        "new_visitor_count": 19,
                        "ip_count": 21
                    },
                    {
                        "category": "",
                        "pv_count": 582,
                        "visit_count": 98,
                        "visitor_count": 50,
                        "new_visitor_count": 25,
                        "ip_count": 37
                    },
                    {
                        "category": "",
                        "pv_count": 548,
                        "visit_count": 91,
                        "visitor_count": 58,
                        "new_visitor_count": 44,
                        "ip_count": 51
                    },
                    {
                        "category": "15点",
                        "pv_count": 576,
                        "visit_count": 82,
                        "visitor_count": 47,
                        "new_visitor_count": 32,
                        "ip_count": 41
                    },
                    {
                        "category": "",
                        "pv_count": 638,
                        "visit_count": 72,
                        "visitor_count": 42,
                        "new_visitor_count": 27,
                        "ip_count": 35
                    },
                    {
                        "category": "",
                        "pv_count": 383,
                        "visit_count": 64,
                        "visitor_count": 43,
                        "new_visitor_count": 30,
                        "ip_count": 39
                    },
                    {
                        "category": "18点",
                        "pv_count": 201,
                        "visit_count": 31,
                        "visitor_count": 19,
                        "new_visitor_count": 11,
                        "ip_count": 14
                    },
                    {
                        "category": "",
                        "pv_count": 120,
                        "visit_count": 17,
                        "visitor_count": 13,
                        "new_visitor_count": 10,
                        "ip_count": 13
                    },
                    {
                        "category": "",
                        "pv_count": 81,
                        "visit_count": 19,
                        "visitor_count": 15,
                        "new_visitor_count": 11,
                        "ip_count": 13
                    },
                    {
                        "category": "21点",
                        "pv_count": 117,
                        "visit_count": 24,
                        "visitor_count": 16,
                        "new_visitor_count": 10,
                        "ip_count": 15
                    },
                    {
                        "category": "",
                        "pv_count": 142,
                        "visit_count": 23,
                        "visitor_count": 18,
                        "new_visitor_count": 13,
                        "ip_count": 18
                    },
                    {
                        "category": "",
                        "pv_count": 150,
                        "visit_count": 20,
                        "visitor_count": 18,
                        "new_visitor_count": 17,
                        "ip_count": 18
                    }
                ],
                "radar": [
                    {
                        "category": "浏览量比率",
                        "through": 97.88,
                        "link": 2.12
                    },
                    {
                        "category": "访问次数比率",
                        "through": 97.7,
                        "link": 2.3
                    },
                    {
                        "category": "访客数比率",
                        "through": 97.35,
                        "link": 2.65
                    },
                    {
                        "category": "新访客比率",
                        "through": 55.61,
                        "link": 53.13
                    },
                    {
                        "category": "IP 数比率",
                        "through": 96.69,
                        "link": 3.31
                    },
                    {
                        "category": "跳出率",
                        "through": 42.11,
                        "link": 36.84
                    }
                ],
                "map": {
                    "China": [
                        {
                            "id": "31",
                            "name": "上海",
                            "pv_count": 5992,
                            "visit_count": 946,
                            "visitor_count": 601,
                            "ip_count": 394
                        },
                        {
                            "id": "37",
                            "name": "山东",
                            "pv_count": 786,
                            "visit_count": 82,
                            "visitor_count": 48,
                            "ip_count": 41
                        },
                        {
                            "id": "44",
                            "name": "广东",
                            "pv_count": 429,
                            "visit_count": 110,
                            "visitor_count": 99,
                            "ip_count": 89
                        },
                        {
                            "id": "51",
                            "name": "四川",
                            "pv_count": 322,
                            "visit_count": 59,
                            "visitor_count": 50,
                            "ip_count": 49
                        },
                        {
                            "id": "42",
                            "name": "湖北",
                            "pv_count": 104,
                            "visit_count": 28,
                            "visitor_count": 24,
                            "ip_count": 18
                        },
                        {
                            "id": "32",
                            "name": "江苏",
                            "pv_count": 85,
                            "visit_count": 26,
                            "visitor_count": 24,
                            "ip_count": 23
                        },
                        {
                            "id": "33",
                            "name": "浙江",
                            "pv_count": 68,
                            "visit_count": 28,
                            "visitor_count": 24,
                            "ip_count": 23
                        },
                        {
                            "id": "43",
                            "name": "湖南",
                            "pv_count": 62,
                            "visit_count": 26,
                            "visitor_count": 22,
                            "ip_count": 20
                        },
                        {
                            "id": "11",
                            "name": "北京",
                            "pv_count": 61,
                            "visit_count": 28,
                            "visitor_count": 28,
                            "ip_count": 25
                        },
                        {
                            "id": "13",
                            "name": "河北",
                            "pv_count": 56,
                            "visit_count": 10,
                            "visitor_count": 8,
                            "ip_count": 7
                        },
                        {
                            "id": "23",
                            "name": "黑龙江",
                            "pv_count": 51,
                            "visit_count": 19,
                            "visitor_count": 17,
                            "ip_count": 14
                        },
                        {
                            "id": "61",
                            "name": "陕西",
                            "pv_count": 48,
                            "visit_count": 13,
                            "visitor_count": 11,
                            "ip_count": 9
                        },
                        {
                            "id": "50",
                            "name": "重庆",
                            "pv_count": 41,
                            "visit_count": 12,
                            "visitor_count": 12,
                            "ip_count": 10
                        },
                        {
                            "id": "71",
                            "name": "台湾",
                            "pv_count": 39,
                            "visit_count": 11,
                            "visitor_count": 9,
                            "ip_count": 6
                        },
                        {
                            "id": "34",
                            "name": "安徽",
                            "pv_count": 33,
                            "visit_count": 10,
                            "visitor_count": 9,
                            "ip_count": 9
                        },
                        {
                            "id": "22",
                            "name": "吉林",
                            "pv_count": 27,
                            "visit_count": 8,
                            "visitor_count": 8,
                            "ip_count": 7
                        },
                        {
                            "id": "41",
                            "name": "河南",
                            "pv_count": 23,
                            "visit_count": 12,
                            "visitor_count": 11,
                            "ip_count": 11
                        },
                        {
                            "id": "81",
                            "name": "香港",
                            "pv_count": 20,
                            "visit_count": 8,
                            "visitor_count": 5,
                            "ip_count": 4
                        },
                        {
                            "id": "35",
                            "name": "福建",
                            "pv_count": 16,
                            "visit_count": 5,
                            "visitor_count": 5,
                            "ip_count": 5
                        },
                        {
                            "id": "36",
                            "name": "江西",
                            "pv_count": 11,
                            "visit_count": 4,
                            "visitor_count": 3,
                            "ip_count": 2
                        },
                        {
                            "id": "53",
                            "name": "云南",
                            "pv_count": 11,
                            "visit_count": 2,
                            "visitor_count": 2,
                            "ip_count": 2
                        },
                        {
                            "id": "21",
                            "name": "辽宁",
                            "pv_count": 7,
                            "visit_count": 3,
                            "visitor_count": 2,
                            "ip_count": 2
                        },
                        {
                            "id": "52",
                            "name": "贵州",
                            "pv_count": 6,
                            "visit_count": 1,
                            "visitor_count": 1,
                            "ip_count": 1
                        },
                        {
                            "id": "12",
                            "name": "天津",
                            "pv_count": 3,
                            "visit_count": 1,
                            "visitor_count": 1,
                            "ip_count": 1
                        },
                        {
                            "id": "0",
                            "name": "其他",
                            "pv_count": 2,
                            "visit_count": 1,
                            "visitor_count": 1,
                            "ip_count": 1
                        },
                        {
                            "id": "45",
                            "name": "广西",
                            "pv_count": 1,
                            "visit_count": 1,
                            "visitor_count": 1,
                            "ip_count": 1
                        }
                    ],
                    "world": [
                        {
                            "id": "China",
                            "name": "中国",
                            "code": "cn",
                            "pv_count": 8304,
                            "visit_count": 1454,
                            "visitor_count": 1026,
                            "ip_count": 774
                        },
                        {
                            "id": "United States",
                            "name": "美国",
                            "code": "us",
                            "pv_count": 101,
                            "visit_count": 29,
                            "visitor_count": 26,
                            "ip_count": 25
                        },
                        {
                            "id": "India",
                            "name": "印度",
                            "code": "in",
                            "pv_count": 71,
                            "visit_count": 30,
                            "visitor_count": 30,
                            "ip_count": 29
                        },
                        {
                            "id": "Jordan",
                            "name": "约旦",
                            "code": "jo",
                            "pv_count": 39,
                            "visit_count": 3,
                            "visitor_count": 1,
                            "ip_count": 1
                        },
                        {
                            "id": "Indonesia",
                            "name": "印度尼西亚",
                            "code": "id",
                            "pv_count": 37,
                            "visit_count": 20,
                            "visitor_count": 18,
                            "ip_count": 18
                        },
                        {
                            "id": "Iran",
                            "name": "伊朗",
                            "code": "ir",
                            "pv_count": 35,
                            "visit_count": 7,
                            "visitor_count": 6,
                            "ip_count": 4
                        },
                        {
                            "id": "Russia",
                            "name": "俄罗斯",
                            "code": "ru",
                            "pv_count": 34,
                            "visit_count": 11,
                            "visitor_count": 11,
                            "ip_count": 11
                        },
                        {
                            "id": "Netherlands",
                            "name": "荷兰",
                            "code": "nl",
                            "pv_count": 26,
                            "visit_count": 11,
                            "visitor_count": 11,
                            "ip_count": 9
                        },
                        {
                            "id": "Turkey",
                            "name": "土耳其",
                            "code": "tr",
                            "pv_count": 22,
                            "visit_count": 12,
                            "visitor_count": 12,
                            "ip_count": 12
                        },
                        {
                            "id": "Brazil",
                            "name": "巴西",
                            "code": "br",
                            "pv_count": 21,
                            "visit_count": 11,
                            "visitor_count": 11,
                            "ip_count": 11
                        },
                        {
                            "id": "Peru",
                            "name": "秘鲁",
                            "code": "pe",
                            "pv_count": 17,
                            "visit_count": 3,
                            "visitor_count": 3,
                            "ip_count": 3
                        },
                        {
                            "id": "Malaysia",
                            "name": "马来西亚",
                            "code": "my",
                            "pv_count": 17,
                            "visit_count": 5,
                            "visitor_count": 4,
                            "ip_count": 4
                        },
                        {
                            "id": "Ukraine",
                            "name": "乌克兰",
                            "code": "ua",
                            "pv_count": 15,
                            "visit_count": 10,
                            "visitor_count": 10,
                            "ip_count": 8
                        },
                        {
                            "id": "Canada",
                            "name": "加拿大",
                            "code": "ca",
                            "pv_count": 13,
                            "visit_count": 7,
                            "visitor_count": 5,
                            "ip_count": 5
                        },
                        {
                            "id": "Mexico",
                            "name": "墨西哥",
                            "code": "mx",
                            "pv_count": 13,
                            "visit_count": 7,
                            "visitor_count": 7,
                            "ip_count": 7
                        },
                        {
                            "id": "Thailand",
                            "name": "泰国",
                            "code": "th",
                            "pv_count": 10,
                            "visit_count": 8,
                            "visitor_count": 7,
                            "ip_count": 7
                        },
                        {
                            "id": "Saudi Arabia",
                            "name": "沙特阿拉伯",
                            "code": "sa",
                            "pv_count": 10,
                            "visit_count": 4,
                            "visitor_count": 4,
                            "ip_count": 4
                        },
                        {
                            "id": "United Arab Emirates",
                            "name": "阿拉伯联合酋长国",
                            "code": "ae",
                            "pv_count": 8,
                            "visit_count": 2,
                            "visitor_count": 1,
                            "ip_count": 1
                        },
                        {
                            "id": "Slovakia",
                            "name": "斯洛伐克",
                            "code": "sk",
                            "pv_count": 8,
                            "visit_count": 5,
                            "visitor_count": 5,
                            "ip_count": 5
                        },
                        {
                            "id": "United Kingdom",
                            "name": "英国",
                            "code": "gb",
                            "pv_count": 7,
                            "visit_count": 4,
                            "visitor_count": 4,
                            "ip_count": 4
                        },
                        {
                            "id": "Germany",
                            "name": "德国",
                            "code": "de",
                            "pv_count": 7,
                            "visit_count": 6,
                            "visitor_count": 6,
                            "ip_count": 6
                        },
                        {
                            "id": "Egypt",
                            "name": "埃及",
                            "code": "eg",
                            "pv_count": 6,
                            "visit_count": 4,
                            "visitor_count": 4,
                            "ip_count": 4
                        },
                        {
                            "id": "Bangladesh",
                            "name": "孟加拉国",
                            "code": "bd",
                            "pv_count": 6,
                            "visit_count": 4,
                            "visitor_count": 4,
                            "ip_count": 4
                        },
                        {
                            "id": "Italy",
                            "name": "意大利",
                            "code": "it",
                            "pv_count": 6,
                            "visit_count": 4,
                            "visitor_count": 4,
                            "ip_count": 4
                        },
                        {
                            "id": "Vietnam",
                            "name": "越南",
                            "code": "vn",
                            "pv_count": 6,
                            "visit_count": 4,
                            "visitor_count": 4,
                            "ip_count": 4
                        },
                        {
                            "id": "Australia",
                            "name": "澳大利亚",
                            "code": "au",
                            "pv_count": 5,
                            "visit_count": 2,
                            "visitor_count": 2,
                            "ip_count": 2
                        },
                        {
                            "id": "Spain",
                            "name": "西班牙",
                            "code": "es",
                            "pv_count": 5,
                            "visit_count": 2,
                            "visitor_count": 2,
                            "ip_count": 2
                        },
                        {
                            "id": "Korea",
                            "name": "韩国",
                            "code": "kr",
                            "pv_count": 4,
                            "visit_count": 2,
                            "visitor_count": 2,
                            "ip_count": 2
                        },
                        {
                            "id": "Singapore",
                            "name": "新加坡",
                            "code": "sg",
                            "pv_count": 4,
                            "visit_count": 1,
                            "visitor_count": 1,
                            "ip_count": 1
                        },
                        {
                            "id": "South Africa",
                            "name": "南非",
                            "code": "za",
                            "pv_count": 4,
                            "visit_count": 2,
                            "visitor_count": 2,
                            "ip_count": 2
                        },
                        {
                            "id": "Algeria",
                            "name": "阿尔及利亚",
                            "code": "dz",
                            "pv_count": 3,
                            "visit_count": 2,
                            "visitor_count": 2,
                            "ip_count": 2
                        },
                        {
                            "id": "Colombia",
                            "name": "哥伦比亚",
                            "code": "co",
                            "pv_count": 3,
                            "visit_count": 2,
                            "visitor_count": 2,
                            "ip_count": 2
                        },
                        {
                            "id": "Belgium",
                            "name": "比利时",
                            "code": "be",
                            "pv_count": 3,
                            "visit_count": 2,
                            "visitor_count": 2,
                            "ip_count": 2
                        },
                        {
                            "id": "France",
                            "name": "法国",
                            "code": "fr",
                            "pv_count": 3,
                            "visit_count": 3,
                            "visitor_count": 3,
                            "ip_count": 3
                        },
                        {
                            "id": "Venezuela",
                            "name": "委内瑞拉",
                            "code": "ve",
                            "pv_count": 3,
                            "visit_count": 1,
                            "visitor_count": 1,
                            "ip_count": 1
                        },
                        {
                            "id": "Greece",
                            "name": "希腊",
                            "code": "gr",
                            "pv_count": 3,
                            "visit_count": 1,
                            "visitor_count": 1,
                            "ip_count": 1
                        },
                        {
                            "id": "Morocco",
                            "name": "摩洛哥",
                            "code": "ma",
                            "pv_count": 3,
                            "visit_count": 1,
                            "visitor_count": 1,
                            "ip_count": 1
                        },
                        {
                            "id": "Bulgaria",
                            "name": "保加利亚",
                            "code": "bg",
                            "pv_count": 3,
                            "visit_count": 1,
                            "visitor_count": 1,
                            "ip_count": 1
                        },
                        {
                            "id": "Palestine",
                            "name": "巴勒斯坦",
                            "code": "ps",
                            "pv_count": 2,
                            "visit_count": 1,
                            "visitor_count": 1,
                            "ip_count": 1
                        },
                        {
                            "id": "Ireland",
                            "name": "爱尔兰",
                            "code": "ie",
                            "pv_count": 2,
                            "visit_count": 1,
                            "visitor_count": 1,
                            "ip_count": 1
                        },
                        {
                            "id": "Nepal",
                            "name": "尼泊尔",
                            "code": "np",
                            "pv_count": 2,
                            "visit_count": 1,
                            "visitor_count": 1,
                            "ip_count": 1
                        },
                        {
                            "id": "Pakistan",
                            "name": "巴基斯坦",
                            "code": "pk",
                            "pv_count": 2,
                            "visit_count": 2,
                            "visitor_count": 2,
                            "ip_count": 2
                        },
                        {
                            "id": "Austria",
                            "name": "奥地利",
                            "code": "at",
                            "pv_count": 2,
                            "visit_count": 1,
                            "visitor_count": 1,
                            "ip_count": 1
                        },
                        {
                            "id": "Kazakhstan",
                            "name": "哈萨克斯坦",
                            "code": "kz",
                            "pv_count": 1,
                            "visit_count": 1,
                            "visitor_count": 1,
                            "ip_count": 1
                        },
                        {
                            "id": "Philippines",
                            "name": "菲律宾",
                            "code": "ph",
                            "pv_count": 1,
                            "visit_count": 1,
                            "visitor_count": 1,
                            "ip_count": 1
                        },
                        {
                            "id": "Croatia",
                            "name": "克罗地亚",
                            "code": "hr",
                            "pv_count": 1,
                            "visit_count": 1,
                            "visitor_count": 1,
                            "ip_count": 1
                        },
                        {
                            "id": "Macedonia",
                            "name": "马其顿",
                            "code": "mk",
                            "pv_count": 1,
                            "visit_count": 1,
                            "visitor_count": 1,
                            "ip_count": 1
                        },
                        {
                            "id": "Qatar",
                            "name": "卡塔尔",
                            "code": "qa",
                            "pv_count": 1,
                            "visit_count": 1,
                            "visitor_count": 1,
                            "ip_count": 1
                        },
                        {
                            "id": "Argentina",
                            "name": "阿根廷",
                            "code": "ar",
                            "pv_count": 1,
                            "visit_count": 1,
                            "visitor_count": 1,
                            "ip_count": 1
                        }
                    ]
                }
            }


    return Response(json.dumps(result, indent=4), mimetype='application/json')

