#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''''
Created on
@author: zhuangyan
'''
import json

from flask import Response
from flask_jwt import jwt_required, current_identity

from . import api




@api.route('/menu',methods=['POST'])
@jwt_required()
def getMenu():
    username = current_identity.username
    result = {
        "result": "y",
        "msg": "",
        "data": [
            {
                "text": "<i class='fas fa-sync-alt'></i>刷新",
                "encoded": False,
                "url": "javascript:refresh();"
            },
            {
                "text": "<i class='fas fa-expand'></i>全屏",
                "encoded": False,
                "cssClass": "fullscreen",
                "url": "javascript:;"
            },
            {
                "text": "<i class='fas fa-lock'></i>锁屏",
                "encoded": False,
                "url": "javascript:lockScreen();"
            },
            {
                "text": "<hr>",
                "encoded": False
            },
            {
                "text": "<i class='fas fa-paint-brush'></i>配色",
                "encoded": False,
                "items": [
                    {
                        "text": "<i class='fas fa-genderless'></i>IKKI Amikoko",
                        "encoded": False,
                        "items": [
                            {
                                "text": "<i class='color' style='background-color: #1890ff;'></i><i class='color' style='background-color: #69c0ff;'></i>默认",
                                "encoded": False,
                                "url": "javascript:changeColor(\"default\", \"#1890ff\", \"#69c0ff\");"
                            },
                            {
                                "text": "<i class='color' style='background-color: #c39b8f;'></i><i class='color' style='background-color: #d9b6ac;'></i>褐色",
                                "encoded": False,
                                "url": "javascript:changeColor(\"brown\", \"#c39b8f\", \"#d9b6ac\");"
                            },
                            {
                                "text": "<i class='color' style='background-color: #d770ad;'></i><i class='color' style='background-color: #ec87c0;'></i>桃色",
                                "encoded": False,
                                "url": "javascript:changeColor(\"pink\", \"#d770ad\", \"#ec87c0\");"
                            },
                            {
                                "text": "<i class='color' style='background-color: #da4453;'></i><i class='color' style='background-color: #ed5565;'></i>红色",
                                "encoded": False,
                                "url": "javascript:changeColor(\"red\", \"#da4453\", \"#ed5565\");"
                            },
                            {
                                "text": "<i class='color' style='background-color: #ff9800;'></i><i class='color' style='background-color: #ffb74d;'></i>橙色",
                                "encoded": False,
                                "url": "javascript:changeColor(\"orange\", \"#ff9800\", \"#ffb74d\");"
                            },
                            {
                                "text": "<i class='color' style='background-color: #f6bb42;'></i><i class='color' style='background-color: #ffce54;'></i>黄色",
                                "encoded": False,
                                "url": "javascript:changeColor(\"yellow\", \"#f6bb42\", \"#ffce54\");"
                            },
                            {
                                "text": "<i class='color' style='background-color: #e6e9ed;'></i><i class='color' style='background-color: #f5f7fa;'></i>白色",
                                "encoded": False,
                                "url": "javascript:changeColor(\"white\", \"#e6e9ed\", \"#f5f7fa\");"
                            },
                            {
                                "text": "<i class='color' style='background-color: #8cc152;'></i><i class='color' style='background-color: #a0d468;'></i>翠色",
                                "encoded": False,
                                "url": "javascript:changeColor(\"grass\", \"#8cc152\", \"#a0d468\");"
                            },
                            {
                                "text": "<i class='color' style='background-color: #37bc9b;'></i><i class='color' style='background-color: #48cfad;'></i>绿色",
                                "encoded": False,
                                "url": "javascript:changeColor(\"green\", \"#37bc9b\", \"#48cfad\");"
                            },
                            {
                                "text": "<i class='color' style='background-color: #3bafda;'></i><i class='color' style='background-color: #4fc1e9;'></i>青色",
                                "encoded": False,
                                "url": "javascript:changeColor(\"cyan\", \"#3bafda\", \"#4fc1e9\");"
                            },
                            {
                                "text": "<i class='color' style='background-color: #4a89dc;'></i><i class='color' style='background-color: #5d9cec;'></i>蓝色",
                                "encoded": False,
                                "url": "javascript:changeColor(\"blue\", \"#4a89dc\", \"#5d9cec\");"
                            },
                            {
                                "text": "<i class='color' style='background-color: #967adc;'></i><i class='color' style='background-color: #ac92ec;'></i>紫色",
                                "encoded": False,
                                "url": "javascript:changeColor(\"purple\", \"#967adc\", \"#ac92ec\");"
                            },
                            {
                                "text": "<i class='color' style='background-color: #434a54;'></i><i class='color' style='background-color: #656d78;'></i>黑色",
                                "encoded": False,
                                "url": "javascript:changeColor(\"black\", \"#434a54\", \"#656d78\");"
                            },
                            {
                                "text": "<i class='color' style='background-color: #aab2bd;'></i><i class='color' style='background-color: #ccd1d9;'></i>灰色",
                                "encoded": False,
                                "url": "javascript:changeColor(\"gray\", \"#aab2bd\", \"#ccd1d9\");"
                            }
                        ]
                    },
                    {
                        "text": "<i class='fas fa-genderless'></i>Ant Design",
                        "encoded": False,
                        "items": [
                            {
                                "text": "<i class='color' style='background-color: #1890ff;'></i><i class='color' style='background-color: #40a9ff;'></i>默认",
                                "encoded": False,
                                "url": "javascript:changeColor(\"ant_default\", \"#1890ff\", \"#40a9ff\");"
                            },
                            {
                                "text": "<i class='color' style='background-color: #f5222d;'></i><i class='color' style='background-color: #ff7875;'></i>薄暮",
                                "encoded": False,
                                "url": "javascript:changeColor(\"ant_red\", \"#f5222d\", \"#ff7875\");"
                            },
                            {
                                "text": "<i class='color' style='background-color: #fa541c;'></i><i class='color' style='background-color: #ff9c6e;'></i>火山",
                                "encoded": False,
                                "url": "javascript:changeColor(\"ant_volcano\", \"#fa541c\", \"#ff9c6e\");"
                            },
                            {
                                "text": "<i class='color' style='background-color: #fa8c16;'></i><i class='color' style='background-color: #ffc069;'></i>日暮",
                                "encoded": False,
                                "url": "javascript:changeColor(\"ant_orange\", \"#fa8c16\", \"#ffc069\");"
                            },
                            {
                                "text": "<i class='color' style='background-color: #faad14;'></i><i class='color' style='background-color: #ffd666;'></i>金盏花",
                                "encoded": False,
                                "url": "javascript:changeColor(\"ant_gold\", \"#faad14\", \"#ffd666\");"
                            },
                            {
                                "text": "<i class='color' style='background-color: #fadb14;'></i><i class='color' style='background-color: #fff566;'></i>日出",
                                "encoded": False,
                                "url": "javascript:changeColor(\"ant_yellow\", \"#fadb14\", \"#fff566\");"
                            },
                            {
                                "text": "<i class='color' style='background-color: #a0d911;'></i><i class='color' style='background-color: #d3f261;'></i>青柠",
                                "encoded": False,
                                "url": "javascript:changeColor(\"ant_lime\", \"#a0d911\", \"#d3f261\");"
                            },
                            {
                                "text": "<i class='color' style='background-color: #52c41a;'></i><i class='color' style='background-color: #95de64;'></i>极光绿",
                                "encoded": False,
                                "url": "javascript:changeColor(\"ant_green\", \"#52c41a\", \"#95de64\");"
                            },
                            {
                                "text": "<i class='color' style='background-color: #13c2c2;'></i><i class='color' style='background-color: #5cdbd3;'></i>明青",
                                "encoded": False,
                                "url": "javascript:changeColor(\"ant_cyan\", \"#13c2c2\", \"#5cdbd3\");"
                            },
                            {
                                "text": "<i class='color' style='background-color: #1890ff;'></i><i class='color' style='background-color: #69c0ff;'></i>拂晓蓝",
                                "encoded": False,
                                "url": "javascript:changeColor(\"ant_blue\", \"#1890ff\", \"#69c0ff\");"
                            },
                            {
                                "text": "<i class='color' style='background-color: #2f54eb;'></i><i class='color' style='background-color: #85a5ff;'></i>极客蓝",
                                "encoded": False,
                                "url": "javascript:changeColor(\"ant_geekblue\", \"#2f54eb\", \"#85a5ff\");"
                            },
                            {
                                "text": "<i class='color' style='background-color: #722ed1;'></i><i class='color' style='background-color: #b37feb;'></i>酱紫",
                                "encoded": False,
                                "url": "javascript:changeColor(\"ant_purple\", \"#722ed1\", \"#b37feb\");"
                            },
                            {
                                "text": "<i class='color' style='background-color: #eb2f96;'></i><i class='color' style='background-color: #ff85c0;'></i>法式洋红",
                                "encoded": False,
                                "url": "javascript:changeColor(\"ant_magenta\", \"#eb2f96\", \"#ff85c0\");"
                            }
                        ]
                    },
                    {
                        "text": "<i class='fas fa-genderless'></i>Material Design",
                        "encoded": False,
                        "items": [
                            {
                                "text": "<i class='color' style='background-color: #018786;'></i><i class='color' style='background-color: #79bcbc;'></i>Default",
                                "encoded": False,
                                "url": "javascript:changeColor(\"material_default\", \"#018786\", \"#79bcbc\");"
                            },
                            {
                                "text": "<i class='color' style='background-color: #f44336;'></i><i class='color' style='background-color: #e57373;'></i>Red",
                                "encoded": False,
                                "url": "javascript:changeColor(\"material_red\", \"#f44336\", \"#e57373\");"
                            },
                            {
                                "text": "<i class='color' style='background-color: #e91e63;'></i><i class='color' style='background-color: #f06292;'></i>Pink",
                                "encoded": False,
                                "url": "javascript:changeColor(\"material_pink\", \"#e91e63\", \"#f06292\");"
                            },
                            {
                                "text": "<i class='color' style='background-color: #9c27b0;'></i><i class='color' style='background-color: #ba68c8;'></i>Purple",
                                "encoded": False,
                                "url": "javascript:changeColor(\"material_purple\", \"#9c27b0\", \"#ba68c8\");"
                            },
                            {
                                "text": "<i class='color' style='background-color: #673ab7;'></i><i class='color' style='background-color: #9575cd;'></i>Deep Purple",
                                "encoded": False,
                                "url": "javascript:changeColor(\"material_deep_purple\", \"#673ab7\", \"#9575cd\");"
                            },
                            {
                                "text": "<i class='color' style='background-color: #3f51b5;'></i><i class='color' style='background-color: #7986cb;'></i>Indigo",
                                "encoded": False,
                                "url": "javascript:changeColor(\"material_indigo\", \"#3f51b5\", \"#7986cb\");"
                            },
                            {
                                "text": "<i class='color' style='background-color: #2196f3;'></i><i class='color' style='background-color: #64b5f6;'></i>Blue",
                                "encoded": False,
                                "url": "javascript:changeColor(\"material_blue\", \"#2196f3\", \"#64b5f6\");"
                            },
                            {
                                "text": "<i class='color' style='background-color: #03a9f4;'></i><i class='color' style='background-color: #4fc3f7;'></i>Light Blue",
                                "encoded": False,
                                "url": "javascript:changeColor(\"material_light_blue\", \"#03a9f4\", \"#4fc3f7\");"
                            },
                            {
                                "text": "<i class='color' style='background-color: #00bcd4;'></i><i class='color' style='background-color: #4dd0e1;'></i>Cyan",
                                "encoded": False,
                                "url": "javascript:changeColor(\"material_cyan\", \"#00bcd4\", \"#4dd0e1\");"
                            },
                            {
                                "text": "<i class='color' style='background-color: #009688;'></i><i class='color' style='background-color: #4db6ac;'></i>Teal",
                                "encoded": False,
                                "url": "javascript:changeColor(\"material_teal\", \"#009688\", \"#4db6ac\");"
                            },
                            {
                                "text": "<i class='color' style='background-color: #4caf50;'></i><i class='color' style='background-color: #81c784;'></i>Green",
                                "encoded": False,
                                "url": "javascript:changeColor(\"material_green\", \"#4caf50\", \"#81c784\");"
                            },
                            {
                                "text": "<i class='color' style='background-color: #8bc34a;'></i><i class='color' style='background-color: #aed581;'></i>Light Green",
                                "encoded": False,
                                "url": "javascript:changeColor(\"material_light_green\", \"#8bc34a\", \"#aed581\");"
                            },
                            {
                                "text": "<i class='color' style='background-color: #cddc39;'></i><i class='color' style='background-color: #dce775;'></i>Lime",
                                "encoded": False,
                                "url": "javascript:changeColor(\"material_lime\", \"#cddc39\", \"#dce775\");"
                            },
                            {
                                "text": "<i class='color' style='background-color: #ffeb3b;'></i><i class='color' style='background-color: #fff176;'></i>Yellow",
                                "encoded": False,
                                "url": "javascript:changeColor(\"material_yellow\", \"#ffeb3b\", \"#fff176\");"
                            },
                            {
                                "text": "<i class='color' style='background-color: #ffc107;'></i><i class='color' style='background-color: #ffd54f;'></i>Amber",
                                "encoded": False,
                                "url": "javascript:changeColor(\"material_amber\", \"#ffc107\", \"#ffd54f\");"
                            },
                            {
                                "text": "<i class='color' style='background-color: #ff9800;'></i><i class='color' style='background-color: #ffb74d;'></i>Orange",
                                "encoded": False,
                                "url": "javascript:changeColor(\"material_orange\", \"#ff9800\", \"#ffb74d\");"
                            },
                            {
                                "text": "<i class='color' style='background-color: #ff5722;'></i><i class='color' style='background-color: #ff8a65;'></i>Deep Orange",
                                "encoded": False,
                                "url": "javascript:changeColor(\"material_deep_orange\", \"#ff5722\", \"#ff8a65\");"
                            },
                            {
                                "text": "<i class='color' style='background-color: #795548;'></i><i class='color' style='background-color: #a1887f;'></i>Brown",
                                "encoded": False,
                                "url": "javascript:changeColor(\"material_brown\", \"#795548\", \"#a1887f\");"
                            },
                            {
                                "text": "<i class='color' style='background-color: #9e9e9e;'></i><i class='color' style='background-color: #e0e0e0;'></i>Grey",
                                "encoded": False,
                                "url": "javascript:changeColor(\"material_grey\", \"#9e9e9e\", \"#e0e0e0\");"
                            },
                            {
                                "text": "<i class='color' style='background-color: #607d8b;'></i><i class='color' style='background-color: #90a4ae;'></i>Blue Grey",
                                "encoded": False,
                                "url": "javascript:changeColor(\"material_blue_grey\", \"#607d8b\", \"#90a4ae\");"
                            }
                        ]
                    },
                    {
                        "text": "<i class='fas fa-genderless'></i>Kendo UI",
                        "encoded": False,
                        "items": [
                            {
                                "text": "<i class='color' style='background-color: #f35800;'></i><i class='color' style='background-color: #f0713a;'></i>Default",
                                "encoded": False,
                                "url": "javascript:changeColor(\"kendo_ui_default\", \"#f35800\", \"#f0713a\");"
                            },
                            {
                                "text": "<i class='color' style='background-color: #ff6358;'></i><i class='color' style='background-color: #eb5b51;'></i>Default v2",
                                "encoded": False,
                                "url": "javascript:changeColor(\"kendo_ui_default_v2\", \"#ff6358\", \"#eb5b51\");"
                            },
                            {
                                "text": "<i class='color' style='background-color: #23bde0;'></i><i class='color' style='background-color: #21b0d0;'></i>Default Blue",
                                "encoded": False,
                                "url": "javascript:changeColor(\"kendo_ui_default_blue\", \"#23bde0\", \"#21b0d0\");"
                            },
                            {
                                "text": "<i class='color' style='background-color: #53b827;'></i><i class='color' style='background-color: #4ca924;'></i>Default Green",
                                "encoded": False,
                                "url": "javascript:changeColor(\"kendo_ui_default_green\", \"#53b827\", \"#4ca924\");"
                            },
                            {
                                "text": "<i class='color' style='background-color: #ff9411;'></i><i class='color' style='background-color: #eb8810;'></i>Default Orange",
                                "encoded": False,
                                "url": "javascript:changeColor(\"kendo_ui_default_orange\", \"#ff9411\", \"#eb8810\");"
                            },
                            {
                                "text": "<i class='color' style='background-color: #bf70cc;'></i><i class='color' style='background-color: #b067bc;'></i>Default Purple",
                                "encoded": False,
                                "url": "javascript:changeColor(\"kendo_ui_default_purple\", \"#bf70cc\", \"#b067bc\");"
                            },
                            {
                                "text": "<i class='color' style='background-color: #28bfba;'></i><i class='color' style='background-color: #25b0ab;'></i>Default Turquoise",
                                "encoded": False,
                                "url": "javascript:changeColor(\"kendo_ui_default_turquoise\", \"#28bfba\", \"#25b0ab\");"
                            },
                            {
                                "text": "<i class='color' style='background-color: #007bff;'></i><i class='color' style='background-color: #52b1ff;'></i>Bootstrap v4",
                                "encoded": False,
                                "url": "javascript:changeColor(\"kendo_ui_bootstrap_v4\", \"#007bff\", \"#52b1ff\");"
                            }
                        ]
                    },
                    {
                        "text": "<i class='fas fa-genderless'></i>Bootstrap",
                        "encoded": False,
                        "items": [
                            {
                                "text": "<i class='color' style='background-color: #007bff;'></i><i class='color' style='background-color: #52b1ff;'></i>Bootstrap Blue",
                                "encoded": False,
                                "url": "javascript:changeColor(\"bootstrap_blue\", \"#007bff\", \"#52b1ff\");"
                            },
                            {
                                "text": "<i class='color' style='background-color: #6610f2;'></i><i class='color' style='background-color: #a963ff;'></i>Bootstrap Indigo",
                                "encoded": False,
                                "url": "javascript:changeColor(\"bootstrap_indigo\", \"#6610f2\", \"#a963ff\");"
                            },
                            {
                                "text": "<i class='color' style='background-color: #6f42c1;'></i><i class='color' style='background-color: #b091db;'></i>Bootstrap Purple",
                                "encoded": False,
                                "url": "javascript:changeColor(\"bootstrap_purple\", \"#6f42c1\", \"#b091db\");"
                            },
                            {
                                "text": "<i class='color' style='background-color: #e83e8c;'></i><i class='color' style='background-color: #ff96c0;'></i>Bootstrap Pink",
                                "encoded": False,
                                "url": "javascript:changeColor(\"bootstrap_pink\", \"#e83e8c\", \"#ff96c0\");"
                            },
                            {
                                "text": "<i class='color' style='background-color: #dc3545;'></i><i class='color' style='background-color: #f5898d;'></i>Bootstrap Red",
                                "encoded": False,
                                "url": "javascript:changeColor(\"bootstrap_red\", \"#dc3545\", \"#f5898d\");"
                            },
                            {
                                "text": "<i class='color' style='background-color: #fd7e14;'></i><i class='color' style='background-color: #ffb566;'></i>Bootstrap Orange",
                                "encoded": False,
                                "url": "javascript:changeColor(\"bootstrap_orange\", \"#fd7e14\", \"#ffb566\");"
                            },
                            {
                                "text": "<i class='color' style='background-color: #ffc107;'></i><i class='color' style='background-color: #ffe159;'></i>Bootstrap Yellow",
                                "encoded": False,
                                "url": "javascript:changeColor(\"bootstrap_yellow\", \"#ffc107\", \"#ffe159\");"
                            },
                            {
                                "text": "<i class='color' style='background-color: #28a745;'></i><i class='color' style='background-color: #6bbf79;'></i>Bootstrap Green",
                                "encoded": False,
                                "url": "javascript:changeColor(\"bootstrap_green\", \"#28a745\", \"#6bbf79\");"
                            },
                            {
                                "text": "<i class='color' style='background-color: #20c997;'></i><i class='color' style='background-color: #6de3b8;'></i>Bootstrap Teal",
                                "encoded": False,
                                "url": "javascript:changeColor(\"bootstrap_teal\", \"#20c997\", \"#6de3b8\");"
                            },
                            {
                                "text": "<i class='color' style='background-color: #17a2b8;'></i><i class='color' style='background-color: #5cc9d1;'></i>Bootstrap Cyan",
                                "encoded": False,
                                "url": "javascript:changeColor(\"bootstrap_cyan\", \"#17a2b8\", \"#5cc9d1\");"
                            }
                        ]
                    }
                ]
            },
            {
                "text": "<i class='fas fa-globe'></i>语言",
                "encoded": False,
                "items": [
                    {
                        "text": "<i class='flag-icon flag-icon-cn'></i>中文简体",
                        "encoded": False,
                        "url": "javascript:changeLang(\"zh-CHS\");"
                    },
                    {
                        "text": "<i class='flag-icon flag-icon-hk'></i>中文繁體",
                        "encoded": False,
                        "url": "javascript:changeLang(\"zh-CHT\");"
                    },
                    {
                        "text": "<i class='flag-icon flag-icon-gb'></i>English",
                        "encoded": False,
                        "url": "javascript:changeLang(\"en-US\");"
                    },
                    {
                        "text": "<i class='flag-icon flag-icon-ru'></i>Русский",
                        "encoded": False,
                        "url": "javascript:changeLang(\"ru-RU\");"
                    },
                    {
                        "text": "<i class='flag-icon flag-icon-fr'></i>Français",
                        "encoded": False,
                        "url": "javascript:changeLang(\"fr-FR\");"
                    },
                    {
                        "text": "<i class='flag-icon flag-icon-de'></i>Deutsch",
                        "encoded": False,
                        "url": "javascript:changeLang(\"de-DE\");"
                    },
                    {
                        "text": "<i class='flag-icon flag-icon-it'></i>Italiano",
                        "encoded": False,
                        "url": "javascript:changeLang(\"it-IT\");"
                    },
                    {
                        "text": "<i class='flag-icon flag-icon-pt'></i>Português",
                        "encoded": False,
                        "url": "javascript:changeLang(\"pt-PT\");"
                    },
                    {
                        "text": "<i class='flag-icon flag-icon-es'></i>Español",
                        "encoded": False,
                        "url": "javascript:changeLang(\"es-ES\");"
                    },
                    {
                        "text": "<i class='flag-icon flag-icon-sa'></i>العربية",
                        "encoded": False,
                        "url": "javascript:changeLang(\"ar-SA\");"
                    },
                    {
                        "text": "<i class='flag-icon flag-icon-jp'></i>日本語",
                        "encoded": False,
                        "url": "javascript:changeLang(\"ja-JP\");"
                    },
                    {
                        "text": "<i class='flag-icon flag-icon-kr'></i>한국어",
                        "encoded": False,
                        "url": "javascript:changeLang(\"ko-KR\");"
                    }
                ]
            },
            {
                "text": "<hr>",
                "encoded": False
            },
            {
                "text": "<abbr>"+username+"</abbr><img src='img/IKKI.png' alt='"+username+"'>",
                "encoded": False,
                "items": [

                    {
                        "text": "<i class='fas fa-key'></i>修改密码",
                        "encoded": False,
                        "cssClass": "links-password",
                        "url": "javascript:linkTo(\"/admin/users/\", \"password\");"
                    },
                    {
                        "text": "<i class='fas fa-sign-out-alt'></i>退出登录",
                        "encoded": False,
                        "url": "javascript:confirmMsg(\"退出登录\", \"你确定要退出登录吗？\", \"question\", logout);"
                    }
                ]
            }
        ]
    }

    return Response(json.dumps(result, indent=4), mimetype='application/json')

