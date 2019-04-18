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
from flask_jwt import jwt_required, current_identity
from flask_uploads import UploadSet, extension
from PIL import Image

# from com.db import MongoDB, Database
from com.minerequest import jwt_auth
from com.utils import encrypt_password
from app import mongo


from . import api


@api.route('/nav',methods=['POST'])
@jwt_required()
def getNav():
    userid = current_identity.id
    result = {
        "result": "y",
        "msg": "",
        "data": [
            {
                "id": "01",
                "text": "<i class='fas fa-object-group'></i><sup></sup><abbr>综合<small>Dashboard</small><sub class='theme-l'>Hot</sub></abbr>",
                "encoded": False,
                "expanded": True,
                "items": [
                    {
                        "id": "0101",
                        "text": "<i class='fas fa-tasks'></i>表单<small>Forms</small>",
                        "encoded": False,
                        "expanded": True,
                        "items": [
                            {
                                "id": "010101",
                                "text": "<i class='fas fa-genderless'></i>表单 Post 提交",
                                "encoded": False,
                                "cssClass": "links-form_post",
                                "url": "javascript:linkTo(\"/dashboard/forms/\", \"form_post\");"
                            },
                            {
                                "id": "010102",
                                "text": "<i class='fas fa-genderless'></i>表单 Ajax 提交",
                                "encoded": False,
                                "cssClass": "links-form_ajax",
                                "url": "javascript:linkTo(\"/dashboard/forms/\", \"form_ajax\");"
                            },
                            {
                                "id": "010103",
                                "text": "<i class='fas fa-genderless'></i>范围选择",
                                "encoded": False,
                                "cssClass": "links-form_range",
                                "url": "javascript:linkTo(\"/dashboard/forms/\", \"form_range\");"
                            },
                            {
                                "id": "010104",
                                "text": "<i class='fas fa-genderless'></i>下拉分组多选级联",
                                "encoded": False,
                                "cssClass": "links-form_cascade",
                                "url": "javascript:linkTo(\"/dashboard/forms/\", \"form_cascade\");"
                            },
                            {
                                "id": "010105",
                                "text": "<i class='fas fa-genderless'></i>地图联动选择",
                                "encoded": False,
                                "cssClass": "links-form_map",
                                "url": "javascript:linkTo(\"/dashboard/forms/\", \"form_map\");"
                            }
                        ]
                    },
                    {
                        "id": "0102",
                        "text": "<i class='fas fa-table'></i>表格<small>Grids</small><sub class='theme-l'>ing</sub>",
                        "encoded": False,
                        "expanded": True,
                        "items": [
                            {
                                "id": "010201",
                                "text": "<i class='fas fa-genderless'></i>全功能搜索及自定义编辑",
                                "encoded": False,
                                "cssClass": "links-grid_custom",
                                "url": "javascript:linkTo(\"/dashboard/grids/\", \"grid_custom\");"
                            },
                            {
                                "id": "010202",
                                "text": "<i class='fas fa-genderless'></i>弹出框带校验编辑",
                                "encoded": False,
                                "cssClass": "links-grid_popup",
                                "url": "javascript:linkTo(\"/dashboard/grids/\", \"grid_popup\");"
                            },
                            {
                                "id": "010203",
                                "text": "<i class='fas fa-genderless'></i>行内带校验编辑",
                                "encoded": False,
                                "cssClass": "links-grid_inline",
                                "url": "javascript:linkTo(\"/dashboard/grids/\", \"grid_inline\");"
                            },
                            {
                                "id": "010204",
                                "text": "<i class='fas fa-genderless'></i>单元格带校验编辑",
                                "encoded": False,
                                "cssClass": "links-grid_incell",
                                "url": "javascript:linkTo(\"/dashboard/grids/\", \"grid_incell\");"
                            },
                            {
                                "id": "010205",
                                "text": "<i class='fas fa-genderless'></i>复制新增及数据联动编辑",
                                "encoded": False,
                                "cssClass": "links-grid_copy",
                                "url": "javascript:linkTo(\"/dashboard/grids/\", \"grid_copy\");"
                            },
                            {
                                "id": "010206",
                                "text": "<i class='fas fa-genderless'></i>自定义功能按钮<sub class='theme-l'>Update</sub>",
                                "encoded": False,
                                "cssClass": "links-grid_button",
                                "url": "javascript:linkTo(\"/dashboard/grids/\", \"grid_button\");"
                            },
                            {
                                "id": "010207",
                                "text": "<i class='fas fa-genderless'></i>自定义选择提交",
                                "encoded": False,
                                "cssClass": "links-grid_select",
                                "url": "javascript:linkTo(\"/dashboard/grids/\", \"grid_select\");"
                            },
                            {
                                "id": "010208",
                                "text": "<i class='fas fa-genderless'></i>分组合计排序筛选",
                                "encoded": False,
                                "cssClass": "links-grid_group",
                                "url": "javascript:linkTo(\"/dashboard/grids/\", \"grid_group\");"
                            },
                            {
                                "id": "010209",
                                "text": "<i class='fas fa-genderless'></i>子表详情及滚动翻页",
                                "encoded": False,
                                "cssClass": "links-grid_detail",
                                "url": "javascript:linkTo(\"/dashboard/grids/\", \"grid_detail\");"
                            },
                            {
                                "id": "010210",
                                "text": "<i class='fas fa-genderless'></i>合并表头及行内拆分<sub class='theme-l'>New</sub>",
                                "encoded": False,
                                "cssClass": "links-grid_merge",
                                "url": "javascript:linkTo(\"/dashboard/grids/\", \"grid_merge\");"
                            }
                        ]
                    },
                    {
                        "id": "0103",
                        "text": "<i class='fas fa-tree'></i>树形<small>Trees</small>",
                        "encoded": False,
                        "items": [
                            {
                                "id": "010301",
                                "text": "<i class='fas fa-genderless'></i>敬请期待……",
                                "encoded": False,
                                "cssClass": "",
                                "url": "javascript:;"
                            }
                        ]
                    },
                    {
                        "id": "0104",
                        "text": "<i class='fas fa-list'></i>列表<small>Lists</small>",
                        "encoded": False,
                        "items": [
                            {
                                "id": "010401",
                                "text": "<i class='fas fa-genderless'></i>敬请期待……",
                                "encoded": False,
                                "cssClass": "",
                                "url": "javascript:;"
                            }
                        ]
                    },
                    {
                        "id": "0105",
                        "text": "<i class='fas fa-pause'></i>分配<small>Assigns</small>",
                        "encoded": False,
                        "items": [
                            {
                                "id": "010501",
                                "text": "<i class='fas fa-genderless'></i>敬请期待……",
                                "encoded": False,
                                "cssClass": "",
                                "url": "javascript:;"
                            }
                        ]
                    }
                ]
            },
            {
                "id": "02",
                "text": "<i class='fas fa-cubes'></i><abbr>框架<small>Framework</small></abbr>",
                "encoded": False,
                "items": [
                    {
                        "id": "0201",
                        "text": "<i class='globalizationIcon'></i>全球化<small>Globalization</small>",
                        "encoded": False,
                        "cssClass": "links-globalization",
                        "url": "javascript:linkTo(\"/framework/\", \"globalization\");"
                    },
                    {
                        "id": "0202",
                        "text": "<i class='mvvmIcon'></i>视图模型<small>MVVM</small>",
                        "encoded": False,
                        "cssClass": "links-mvvm",
                        "url": "javascript:linkTo(\"/framework/\", \"mvvm\");"
                    },
                    {
                        "id": "0203",
                        "text": "<i class='dataSourceIcon'></i>数据源<small>DataSource</small>",
                        "encoded": False,
                        "cssClass": "links-datasource",
                        "url": "javascript:linkTo(\"/framework/\", \"datasource\");"
                    },
                    {
                        "id": "0204",
                        "text": "<i class='templatesIcon'></i>模版<small>Templates</small>",
                        "encoded": False,
                        "cssClass": "links-templates",
                        "url": "javascript:linkTo(\"/framework/\", \"templates\");"
                    },
                    {
                        "id": "0205",
                        "text": "<i class='drawingIcon'></i>绘图<small>Drawing</small>",
                        "encoded": False,
                        "cssClass": "links-drawing",
                        "url": "javascript:linkTo(\"/framework/\", \"drawing\");"
                    },
                    {
                        "id": "0206",
                        "text": "<i class='spaIcon'></i>单页应用<small>SPA</small>",
                        "encoded": False,
                        "cssClass": "links-spa",
                        "url": "javascript:linkTo(\"/framework/\", \"spa\");"
                    },
                    {
                        "id": "0207",
                        "text": "<i class='pdfIcon'></i>PDF导出<small>PDF Export</small>",
                        "encoded": False,
                        "cssClass": "links-pdf_export",
                        "url": "javascript:linkTo(\"/framework/\", \"pdf_export\");"
                    },
                    {
                        "id": "0208",
                        "text": "<i class='mobileAppIcon'></i>触摸事件<small>Touch Events</small>",
                        "encoded": False,
                        "cssClass": "links-touch_events",
                        "url": "javascript:linkTo(\"/framework/\", \"touch_events\");"
                    },
                    {
                        "id": "0209",
                        "text": "<i class='integrationIcon'></i>整合<small>Integration</small>",
                        "encoded": False,
                        "cssClass": "links-integration",
                        "url": "javascript:linkTo(\"/framework/\", \"integration\");"
                    }
                ]
            },
            {
                "id": "03",
                "text": "<i class='fas fa-columns'></i><abbr>布局<small>Layout</small></abbr>",
                "encoded": False,
                "items": [
                    {
                        "id": "0301",
                        "text": "<i class='splitterIcon'></i>页面布局<small>Splitter</small>",
                        "encoded": False,
                        "cssClass": "links-splitter",
                        "url": "javascript:linkTo(\"/layout/\", \"splitter\");"
                    },
                    {
                        "id": "0302",
                        "text": "<i class='responsivePanelIcon'></i>响应面板<small>Responsive Panel</small>",
                        "encoded": False,
                        "cssClass": "links-responsive_panel",
                        "url": "javascript:linkTo(\"/layout/\", \"responsive_panel\");"
                    },
                    {
                        "id": "0303",
                        "text": "<i class='windowIcon'></i>模态框<small>Window</small>",
                        "encoded": False,
                        "cssClass": "links-window",
                        "url": "javascript:linkTo(\"/layout/\", \"window\");"
                    },
                    {
                        "id": "0304",
                        "text": "<i class='dialogIcon'></i>对话框<small>Dialog</small>",
                        "encoded": False,
                        "cssClass": "links-dialog",
                        "url": "javascript:linkTo(\"/layout/\", \"dialog\");"
                    },
                    {
                        "id": "0305",
                        "text": "<i class='notificationIcon'></i>通知框<small>Notification</small>",
                        "encoded": False,
                        "cssClass": "links-notification",
                        "url": "javascript:linkTo(\"/layout/\", \"notification\");"
                    },
                    {
                        "id": "0306",
                        "text": "<i class='tooltipIcon'></i>提示框<small>Tooltip</small>",
                        "encoded": False,
                        "cssClass": "links-tooltip",
                        "url": "javascript:linkTo(\"/layout/\", \"tooltip\");"
                    }
                ]
            },
            {
                "id": "04",
                "text": "<i class='fas fa-map-signs'></i><abbr>导航<small>Navigation</small></abbr>",
                "encoded": False,
                "items": [
                    {
                        "id": "0401",
                        "text": "<i class='menuIcon'></i>菜单<small>Menu</small>",
                        "encoded": False,
                        "cssClass": "links-menu",
                        "url": "javascript:linkTo(\"/navigation/\", \"menu\");"
                    },
                    {
                        "id": "0402",
                        "text": "<i class='panelBarIcon'></i>折叠面板<small>PanelBar</small>",
                        "encoded": False,
                        "cssClass": "links-panelbar",
                        "url": "javascript:linkTo(\"/navigation/\", \"panelbar\");"
                    },
                    {
                        "id": "0403",
                        "text": "<i class='tabStripIcon'></i>选项卡<small>TabStrip</small>",
                        "encoded": False,
                        "cssClass": "links-tabstrip",
                        "url": "javascript:linkTo(\"/navigation/\", \"tabstrip\");"
                    },
                    {
                        "id": "0404",
                        "text": "<i class='toolbarIcon'></i>工具栏<small>ToolBar</small>",
                        "encoded": False,
                        "cssClass": "links-toolbar",
                        "url": "javascript:linkTo(\"/navigation/\", \"toolbar\");"
                    },
                    {
                        "id": "0405",
                        "text": "<i class='treeViewIcon'></i>树形视图<small>TreeView</small>",
                        "encoded": False,
                        "cssClass": "links-treeview",
                        "url": "javascript:linkTo(\"/navigation/\", \"treeview\");"
                    },
                    {
                        "id": "0406",
                        "text": "<i class='buttonIcon'></i>按钮<small>Button</small>",
                        "encoded": False,
                        "cssClass": "links-button",
                        "url": "javascript:linkTo(\"/navigation/\", \"button\");"
                    },
                    {
                        "id": "0407",
                        "text": "<i class='mobileButtonGroupIcon'></i>按钮组<small>ButtonGroup</small>",
                        "encoded": False,
                        "cssClass": "links-buttongroup",
                        "url": "javascript:linkTo(\"/navigation/\", \"buttongroup\");"
                    }
                ]
            },
            {
                "id": "05",
                "text": "<i class='fas fa-tasks'></i><abbr>表单<small>Forms</small></abbr>",
                "encoded": False,
                "items": [
                    {
                        "id": "0501",
                        "text": "<i class='mobileSwitchIcon'></i>转换框<small>Switch</small>",
                        "encoded": False,
                        "cssClass": "links-switch",
                        "url": "javascript:linkTo(\"/forms/\", \"switch\");"
                    },
                    {
                        "id": "0502",
                        "text": "<i class='numericTextBoxIcon'></i>数字框<small>NumericTextBox</small>",
                        "encoded": False,
                        "cssClass": "links-numerictextbox",
                        "url": "javascript:linkTo(\"/forms/\", \"numerictextbox\");"
                    },
                    {
                        "id": "0503",
                        "text": "<i class='datePickerIcon'></i>日期框<small>DatePicker</small>",
                        "encoded": False,
                        "cssClass": "links-datepicker",
                        "url": "javascript:linkTo(\"/forms/\", \"datepicker\");"
                    },
                    {
                        "id": "0504",
                        "text": "<i class='dateRangePickerIcon'></i>日期范围框<small>DateRangePicker</small>",
                        "encoded": False,
                        "cssClass": "links-daterangepicker",
                        "url": "javascript:linkTo(\"/forms/\", \"daterangepicker\");"
                    },
                    {
                        "id": "0505",
                        "text": "<i class='timePickerIcon'></i>时间框<small>TimePicker</small>",
                        "encoded": False,
                        "cssClass": "links-timepicker",
                        "url": "javascript:linkTo(\"/forms/\", \"timepicker\");"
                    },
                    {
                        "id": "0506",
                        "text": "<i class='dateTimePickerIcon'></i>时日框<small>DateTimePicker</small>",
                        "encoded": False,
                        "cssClass": "links-datetimepicker",
                        "url": "javascript:linkTo(\"/forms/\", \"datetimepicker\");"
                    },
                    {
                        "id": "0507",
                        "text": "<i class='dateInputIcon'></i>时日掩码框<small>DateInput</small>",
                        "encoded": False,
                        "cssClass": "links-dateinput",
                        "url": "javascript:linkTo(\"/forms/\", \"dateinput\");"
                    },
                    {
                        "id": "0508",
                        "text": "<i class='maskedtextboxIcon'></i>掩码框<small>MaskedTextBox</small>",
                        "encoded": False,
                        "cssClass": "links-maskedtextbox",
                        "url": "javascript:linkTo(\"/forms/\", \"maskedtextbox\");"
                    },
                    {
                        "id": "0509",
                        "text": "<i class='autoCompleteIcon'></i>自动完成框<small>AutoComplete</small>",
                        "encoded": False,
                        "cssClass": "links-autocomplete",
                        "url": "javascript:linkTo(\"/forms/\", \"autocomplete\");"
                    },
                    {
                        "id": "0510",
                        "text": "<i class='dropDownListIcon'></i>单选下拉框<small>DropDownList</small>",
                        "encoded": False,
                        "cssClass": "links-dropdownlist",
                        "url": "javascript:linkTo(\"/forms/\", \"dropdownlist\");"
                    },
                    {
                        "id": "0511",
                        "text": "<i class='comboBoxIcon'></i>输入下拉框<small>ComboBox</small>",
                        "encoded": False,
                        "cssClass": "links-combobox",
                        "url": "javascript:linkTo(\"/forms/\", \"combobox\");"
                    },
                    {
                        "id": "0512",
                        "text": "<i class='multiColumnComboBoxIcon'></i>表格下拉框<small>MultiColumnComboBox</small>",
                        "encoded": False,
                        "cssClass": "links-multicolumncombobox",
                        "url": "javascript:linkTo(\"/forms/\", \"multicolumncombobox\");"
                    },
                    {
                        "id": "0513",
                        "text": "<i class='multiselectIcon'></i>多选下拉框<small>MultiSelect</small>",
                        "encoded": False,
                        "cssClass": "links-multiselect",
                        "url": "javascript:linkTo(\"/forms/\", \"multiselect\");"
                    },
                    {
                        "id": "0514",
                        "text": "<i class='dropDownTreeIcon'></i>树形下拉框<small>DropDownTree</small>",
                        "encoded": False,
                        "cssClass": "links-dropdowntree",
                        "url": "javascript:linkTo(\"/forms/\", \"dropdowntree\");"
                    },
                    {
                        "id": "0515",
                        "text": "<i class='colorPickerIcon'></i>颜色框<small>ColorPicker</small>",
                        "encoded": False,
                        "cssClass": "links-colorpicker",
                        "url": "javascript:linkTo(\"/forms/\", \"colorpicker\");"
                    },
                    {
                        "id": "0516",
                        "text": "<i class='sliderIcon'></i>滑块框<small>Slider</small>",
                        "encoded": False,
                        "cssClass": "links-slider",
                        "url": "javascript:linkTo(\"/forms/\", \"slider\");"
                    },
                    {
                        "id": "0517",
                        "text": "<i class='progressBarIcon'></i>进度框<small>ProgressBar</small>",
                        "encoded": False,
                        "cssClass": "links-progressbar",
                        "url": "javascript:linkTo(\"/forms/\", \"progressbar\");"
                    },
                    {
                        "id": "0518",
                        "text": "<i class='listBoxIcon'></i>穿梭框<small>ListBox</small>",
                        "encoded": False,
                        "cssClass": "links-listbox",
                        "url": "javascript:linkTo(\"/forms/\", \"listbox\");"
                    },
                    {
                        "id": "0519",
                        "text": "<i class='editorIcon'></i>富文本框<small>Editor</small>",
                        "encoded": False,
                        "cssClass": "links-editor",
                        "url": "javascript:linkTo(\"/forms/\", \"editor\");"
                    },
                    {
                        "id": "0520",
                        "text": "<i class='uploadIcon'></i>上传框<small>Upload</small>",
                        "encoded": False,
                        "cssClass": "links-upload",
                        "url": "javascript:linkTo(\"/forms/\", \"upload\");"
                    },
                    {
                        "id": "0521",
                        "text": "<i class='validatorIcon'></i>验证<small>Validator</small>",
                        "encoded": False,
                        "cssClass": "links-validator",
                        "url": "javascript:linkTo(\"/forms/\", \"validator\");"
                    }
                ]
            },
            {
                "id": "06",
                "text": "<i class='fas fa-database'></i><abbr>数据<small>Data</small></abbr>",
                "encoded": False,
                "items": [
                    {
                        "id": "0601",
                        "text": "<i class='gridIcon'></i>表格<small>Grid</small>",
                        "encoded": False,
                        "cssClass": "links-grid",
                        "url": "javascript:linkTo(\"/data/\", \"grid\");"
                    },
                    {
                        "id": "0602",
                        "text": "<i class='treeListIcon'></i>树形列表<small>TreeList</small>",
                        "encoded": False,
                        "cssClass": "links-treelist",
                        "url": "javascript:linkTo(\"/data/\", \"treelist\");"
                    },
                    {
                        "id": "0603",
                        "text": "<i class='listViewIcon'></i>列表视图<small>ListView</small>",
                        "encoded": False,
                        "cssClass": "links-listview",
                        "url": "javascript:linkTo(\"/data/\", \"listview\");"
                    },
                    {
                        "id": "0604",
                        "text": "<i class='spreadsheetIcon'></i>电子表格<small>Spreadsheet</small>",
                        "encoded": False,
                        "cssClass": "links-spreadsheet",
                        "url": "javascript:linkTo(\"/data/\", \"spreadsheet\");"
                    },
                    {
                        "id": "0605",
                        "text": "<i class='pivotGridIcon'></i>透视表格<small>PivotGrid</small>",
                        "encoded": False,
                        "cssClass": "links-pivotgrid",
                        "url": "javascript:linkTo(\"/data/\", \"pivotgrid\");"
                    }
                ]
            },
            {
                "id": "07",
                "text": "<i class='fas fa-calendar-alt'></i><abbr>日程<small>Scheduling</small></abbr>",
                "encoded": False,
                "items": [
                    {
                        "id": "0701",
                        "text": "<i class='calendarIcon'></i>日历<small>Calendar</small>",
                        "encoded": False,
                        "cssClass": "links-calendar",
                        "url": "javascript:linkTo(\"/scheduling/\", \"calendar\");"
                    },
                    {
                        "id": "0702",
                        "text": "<i class='multiViewCalendarIcon'></i>多重日历<small>MultiViewCalendar</small>",
                        "encoded": False,
                        "cssClass": "links-multiviewcalendar",
                        "url": "javascript:linkTo(\"/scheduling/\", \"multiviewcalendar\");"
                    },
                    {
                        "id": "0703",
                        "text": "<i class='schedulerIcon'></i>日程表<small>Scheduler</small>",
                        "encoded": False,
                        "cssClass": "links-scheduler",
                        "url": "javascript:linkTo(\"/scheduling/\", \"scheduler\");"
                    },
                    {
                        "id": "0704",
                        "text": "<i class='ganttIcon'></i>甘特图<small>Gantt</small>",
                        "encoded": False,
                        "cssClass": "links-gantt",
                        "url": "javascript:linkTo(\"/scheduling/\", \"gantt\");"
                    }
                ]
            },
            {
                "id": "08",
                "text": "<i class='fas fa-comments'></i><abbr>会话<small>Conversational</small></abbr>",
                "encoded": False,
                "items": [
                    {
                        "id": "0801",
                        "text": "<i class='chatIcon'></i>聊天<small>Chat</small>",
                        "encoded": False,
                        "cssClass": "links-chat",
                        "url": "javascript:linkTo(\"/conversational/\", \"chat\");"
                    }
                ]
            },
            {
                "id": "09",
                "text": "<i class='fas fa-play-circle'></i><abbr>媒体<small>Media</small></abbr>",
                "encoded": False,
                "items": [
                    {
                        "id": "0901",
                        "text": "<i class='mediaPlayerIcon'></i>媒体播放器<small>MediaPlayer</small>",
                        "encoded": False,
                        "cssClass": "links-mediaplayer",
                        "url": "javascript:linkTo(\"/media/\", \"mediaplayer\");"
                    },
                    {
                        "id": "0902",
                        "text": "<i class='mobileScrollViewIcon'></i>滚动视图<small>ScrollView</small>",
                        "encoded": False,
                        "cssClass": "links-scrollview",
                        "url": "javascript:linkTo(\"/media/\", \"scrollview\");"
                    }
                ]
            },
            {
                "id": "10",
                "text": "<i class='fas fa-hand-pointer'></i><abbr>交互<small>Interactivity</small></abbr>",
                "encoded": False,
                "items": [
                    {
                        "id": "1001",
                        "text": "<i class='dragDropIcon'></i>拖放<small>Drag and Drop</small>",
                        "encoded": False,
                        "cssClass": "links-drag_and_drop",
                        "url": "javascript:linkTo(\"/interactivity/\", \"drag_and_drop\");"
                    },
                    {
                        "id": "1002",
                        "text": "<i class='sortableIcon'></i>拖放排序<small>Sortable</small>",
                        "encoded": False,
                        "cssClass": "links-sortable",
                        "url": "javascript:linkTo(\"/interactivity/\", \"sortable\");"
                    },
                    {
                        "id": "1003",
                        "text": "<i class='stylingIcon'></i>样式<small>Styling</small>",
                        "encoded": False,
                        "cssClass": "links-styling",
                        "url": "javascript:linkTo(\"/interactivity/\", \"styling\");"
                    },
                    {
                        "id": "1004",
                        "text": "<i class='effectsIcon'></i>特效<small>Effects</small>",
                        "encoded": False,
                        "cssClass": "links-effects",
                        "url": "javascript:linkTo(\"/interactivity/\", \"effects\");"
                    },
                    {
                        "id": "1005",
                        "text": "<i class='stylingIcon'></i>波纹效果<small>Ripple Container</small>",
                        "encoded": False,
                        "cssClass": "links-ripple_container",
                        "url": "javascript:linkTo(\"/interactivity/\", \"ripple_container\");"
                    }
                ]
            },
            {
                "id": "11",
                "text": "<i class='fas fa-chart-bar'></i><abbr>图表<small>Charts</small></abbr>",
                "encoded": False,
                "items": [
                    {
                        "id": "1101",
                        "text": "<i class='chartAreaIcon'></i>区域图<small>Area Charts</small>",
                        "encoded": False,
                        "cssClass": "links-area_charts",
                        "url": "javascript:linkTo(\"/charts/\", \"area_charts\");"
                    },
                    {
                        "id": "1102",
                        "text": "<i class='chartBarIcon'></i>条形图<small>Bar Charts</small>",
                        "encoded": False,
                        "cssClass": "links-bar_charts",
                        "url": "javascript:linkTo(\"/charts/\", \"bar_charts\");"
                    },
                    {
                        "id": "1103",
                        "text": "<i class='chartBoxPlotIcon'></i>箱线图<small>Box Plot Charts</small>",
                        "encoded": False,
                        "cssClass": "links-box_plot_charts",
                        "url": "javascript:linkTo(\"/charts/\", \"box_plot_charts\");"
                    },
                    {
                        "id": "1104",
                        "text": "<i class='chartBubbleIcon'></i>气泡图<small>Bubble Charts</small>",
                        "encoded": False,
                        "cssClass": "links-bubble_charts",
                        "url": "javascript:linkTo(\"/charts/\", \"bubble_charts\");"
                    },
                    {
                        "id": "1105",
                        "text": "<i class='chartBulletIcon'></i>子弹图<small>Bullet Charts</small>",
                        "encoded": False,
                        "cssClass": "links-bullet_charts",
                        "url": "javascript:linkTo(\"/charts/\", \"bullet_charts\");"
                    },
                    {
                        "id": "1106",
                        "text": "<i class='chartDonutIcon'></i>环形图<small>Donut Charts</small>",
                        "encoded": False,
                        "cssClass": "links-donut_charts",
                        "url": "javascript:linkTo(\"/charts/\", \"donut_charts\");"
                    },
                    {
                        "id": "1107",
                        "text": "<i class='chartFunnelIcon'></i>漏斗图<small>Funnel Charts</small>",
                        "encoded": False,
                        "cssClass": "links-funnel_charts",
                        "url": "javascript:linkTo(\"/charts/\", \"funnel_charts\");"
                    },
                    {
                        "id": "1108",
                        "text": "<i class='chartLineIcon'></i>折线图<small>Line Charts</small>",
                        "encoded": False,
                        "cssClass": "links-line_charts",
                        "url": "javascript:linkTo(\"/charts/\", \"line_charts\");"
                    },
                    {
                        "id": "1109",
                        "text": "<i class='chartPieIcon'></i>饼图<small>Pie Charts</small>",
                        "encoded": False,
                        "cssClass": "links-pie_charts",
                        "url": "javascript:linkTo(\"/charts/\", \"pie_charts\");"
                    },
                    {
                        "id": "1110",
                        "text": "<i class='chartPolarIcon'></i>极坐标图<small>Polar Charts</small>",
                        "encoded": False,
                        "cssClass": "links-polar_charts",
                        "url": "javascript:linkTo(\"/charts/\", \"polar_charts\");"
                    },
                    {
                        "id": "1111",
                        "text": "<i class='chartRadarIcon'></i>雷达图<small>Radar Charts</small>",
                        "encoded": False,
                        "cssClass": "links-radar_charts",
                        "url": "javascript:linkTo(\"/charts/\", \"radar_charts\");"
                    },
                    {
                        "id": "1112",
                        "text": "<i class='chartScatterIcon'></i>散点图<small>Scatter Charts</small>",
                        "encoded": False,
                        "cssClass": "links-scatter_charts",
                        "url": "javascript:linkTo(\"/charts/\", \"scatter_charts\");"
                    },
                    {
                        "id": "1113",
                        "text": "<i class='sparklineIcon'></i>波形图<small>Sparklines</small>",
                        "encoded": False,
                        "cssClass": "links-sparklines",
                        "url": "javascript:linkTo(\"/charts/\", \"sparklines\");"
                    },
                    {
                        "id": "1114",
                        "text": "<i class='chartStockIcon'></i>股票图<small>Stock Charts</small>",
                        "encoded": False,
                        "cssClass": "links-stock_charts",
                        "url": "javascript:linkTo(\"/charts/\", \"stock_charts\");"
                    },
                    {
                        "id": "1115",
                        "text": "<i class='treemapIcon'></i>树图<small>TreeMap</small>",
                        "encoded": False,
                        "cssClass": "links-treemap",
                        "url": "javascript:linkTo(\"/charts/\", \"treemap\");"
                    },
                    {
                        "id": "1116",
                        "text": "<i class='chartWaterfallIcon'></i>瀑布图<small>Waterfall Charts</small>",
                        "encoded": False,
                        "cssClass": "links-waterfall_charts",
                        "url": "javascript:linkTo(\"/charts/\", \"waterfall_charts\");"
                    },
                    {
                        "id": "1117",
                        "text": "<i class='chartRangeAreaIcon'></i>范区域图<small>Range Area Charts</small>",
                        "encoded": False,
                        "cssClass": "links-range_area_charts",
                        "url": "javascript:linkTo(\"/charts/\", \"range_area_charts\");"
                    },
                    {
                        "id": "1118",
                        "text": "<i class='chartRangeBarIcon'></i>范条形图<small>Range Bar Charts</small>",
                        "encoded": False,
                        "cssClass": "links-range_bar_charts",
                        "url": "javascript:linkTo(\"/charts/\", \"range_bar_charts\");"
                    },
                    {
                        "id": "1119",
                        "text": "<i class='fas fa-thermometer-half'></i>量规<small>Gauges</small>",
                        "encoded": False,
                        "items": [
                            {
                                "id": "111901",
                                "text": "<i class='gaugeLinearIcon'></i>线性计<small>Linear Gauge</small>",
                                "encoded": False,
                                "cssClass": "links-linear_gauge",
                                "url": "javascript:linkTo(\"/charts/gauges/\", \"linear_gauge\");"
                            },
                            {
                                "id": "111902",
                                "text": "<i class='gaugeRadialIcon'></i>径向计<small>Radial Gauge</small>",
                                "encoded": False,
                                "cssClass": "links-radial_gauge",
                                "url": "javascript:linkTo(\"/charts/gauges/\", \"radial_gauge\");"
                            },
                            {
                                "id": "111903",
                                "text": "<i class='gaugeArcIcon'></i>弧形计<small>Arc Gauge</small>",
                                "encoded": False,
                                "cssClass": "links-arc_gauge",
                                "url": "javascript:linkTo(\"/charts/gauges/\", \"arc_gauge\");"
                            }
                        ]
                    },
                    {
                        "id": "1120",
                        "text": "<i class='fas fa-barcode'></i>条码<small>Barcodes</small>",
                        "encoded": False,
                        "items": [
                            {
                                "id": "112001",
                                "text": "<i class='barcodeIcon'></i>条形码<small>Barcode</small>",
                                "encoded": False,
                                "cssClass": "links-barcode",
                                "url": "javascript:linkTo(\"/charts/barcodes/\", \"barcode\");"
                            },
                            {
                                "id": "112002",
                                "text": "<i class='qrcodeIcon'></i>二维码<small>QR Code</small>",
                                "encoded": False,
                                "cssClass": "links-qr_code",
                                "url": "javascript:linkTo(\"/charts/barcodes/\", \"qr_code\");"
                            }
                        ]
                    },
                    {
                        "id": "1121",
                        "text": "<i class='fas fa-map'></i>地图<small>Maps</small>",
                        "encoded": False,
                        "items": [
                            {
                                "id": "112101",
                                "text": "<i class='diagramIcon'></i>架构图<small>Diagram</small>",
                                "encoded": False,
                                "cssClass": "links-diagram",
                                "url": "javascript:linkTo(\"/charts/maps/\", \"diagram\");"
                            },
                            {
                                "id": "112102",
                                "text": "<i class='mapIcon'></i>地图<small>Map</small>",
                                "encoded": False,
                                "cssClass": "links-map",
                                "url": "javascript:linkTo(\"/charts/maps/\", \"map\");"
                            }
                        ]
                    }
                ]
            },
            {
                "id": "12",
                "text": "<i class='fas fa-mobile-alt'></i><abbr>移动端<small>Hybrid</small></abbr>",
                "encoded": False,
                "items": [
                    {
                        "id": "1201",
                        "text": "<i class='fas fa-genderless'></i>敬请期待……",
                        "encoded": False,
                        "cssClass": "",
                        "url": "javascript:;"
                    }
                ]
            },
            {
                "id": "99",
                "text": "<i class='fas fa-list-ol'></i><abbr>一级菜单</abbr>",
                "encoded": False,
                "items": [
                    {
                        "id": "9901",
                        "text": "二级菜单"
                    },
                    {
                        "id": "9902",
                        "text": "二级菜单",
                        "items": [
                            {
                                "id": "990201",
                                "text": "三级菜单"
                            },
                            {
                                "id": "990202",
                                "text": "三级菜单",
                                "items": [
                                    {
                                        "id": "99020201",
                                        "text": "四级菜单"
                                    },
                                    {
                                        "id": "99020202",
                                        "text": "四级菜单",
                                        "items": [
                                            {
                                                "id": "9902020201",
                                                "text": "五级菜单"
                                            },
                                            {
                                                "id": "9902020202",
                                                "text": "五级菜单"
                                            },
                                            {
                                                "id": "9902020203",
                                                "text": "五级菜单"
                                            }
                                        ]
                                    },
                                    {
                                        "id": "99020203",
                                        "text": "四级菜单"
                                    }
                                ]
                            },
                            {
                                "id": "990203",
                                "text": "三级菜单"
                            }
                        ]
                    },
                    {
                        "id": "9903",
                        "text": "二级菜单"
                    }
                ]
            }
        ]
    }

    return Response(json.dumps(result, indent=4), mimetype='application/json')

