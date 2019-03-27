/*!
 * Kendo UI Admin v1.0.0 by IKKI & Amikoko - https://ikki2000.github.io/
 * Copyright 2018-2019 IKKI Studio
 * Released under the MIT License - https://ikki2000.github.io/KendoUI-Admin-Site/LICENSE
 */

/* JS for Layout | Written by IKKI | 2018-02-03 */

// 配置路径
var path = "/",
    webType = "",
    accentColor,
    minorColor,
    navUrl = '/_api/nav',
    menuUrl = '/_api/menu';

/* 初始化 ****************************************************************************/
$(function() {
    // 刷新接管
    document.onkeydown = function() {
        var e = window.event || arguments[0];
        // 屏蔽 F5 和 Ctrl + F5
        if (e.keyCode === 116 || ((e.ctrlKey) && (e.keyCode === 116))) {
            refresh();
            return false;
        }
    };
    // 颜色
    if (localStorage.hasOwnProperty('colorName')) {
        accentColor = localStorage.getItem('accentColor');
        minorColor = localStorage.getItem('minorColor');
        changeColor(localStorage.getItem('colorName'), accentColor, minorColor);
    } else {
        accentColor = '#1890ff';
        minorColor = '#69c0ff';
        changeColor('default', accentColor, minorColor);
    }
    // 语言
    kendo.culture('zh-CN');
    // 左侧导航数据获取
    $.fn.ajaxPost({
        ajaxUrl: navUrl,
        ajaxType:"post",
        succeed: function(res) {
            $('#navPanelBar').kendoPanelBar({
                dataSource: res.data
            });
            $('#navMenu').kendoMenu({
                orientation: 'vertical',
                dataSource: res.data
            });
        }
    });
    // 顶部菜单数据获取
    $.fn.ajaxPost({
        ajaxUrl: menuUrl,
        ajaxType:"post",
        succeed: function(res) {
            if (/Android|iPhone|iPad|iPod|Windows Phone|webOS|SymbianOS|BlackBerry/i.test(navigator.userAgent)) {
                $('#menuV').kendoMenu({
                    orientation: 'vertical',
                    dataSource: res.data
                });
            } else {
                $('#menuH').kendoMenu({
                    dataSource: res.data
                });
            }
        }
    });
    // 全屏
    $('#header').on('click', '.fullscreen', function() {
        var fullscreenEnabled = document.fullscreenEnabled       ||
                                document.webkitFullscreenEnabled ||
                                document.mozFullScreenEnabled    ||
                                document.msFullscreenEnabled;
        if (fullscreenEnabled) {
            var isFullscreen = document.fullscreenElement        ||
                               document.webkitFullscreenElement  ||
                               document.mozFullScreenElement     ||
                               document.msFullscreenElement;
            if (isFullscreen) {
                exitFullscreen();
                $(this).find('.fa-compress').addClass('fa-expand').removeClass('fa-compress');
            } else {
                enterFullscreen();
                $(this).find('.fa-expand').addClass('fa-compress').removeClass('fa-expand');
            }
        } else {
            alertMsg('当前浏览器不支持全屏！', 'error');
        }
    });
    // 回车解锁
    $('body').on('keyup', '#locking input', function(event) {
        if(event.keyCode === 13){
            unlockScreen();
        }
    });
});


// 面包屑导航
function showPath(hash) {
    $('#path').html('');
    $.each($('#navMenu, #menuH, #menuV').find('.links-'+ hash).children('.k-link').parents('.k-item'), function(i, doms) {
        $('#path').prepend('<span><i class="fas fa-angle-double-right"></i>' + $(doms).children('.k-link').html() + '</span>');
    });
    if (hash === '404') {
        $('#path').prepend('<span><i class="fas fa-angle-double-right"></i><i class="fas fa-info-circle"></i>404<small>Error</small></span>');
    }
    var homePath = '';
    if ($('iframe').length === 1) {
        homePath = 'javascript:linkTo(\'/\', \'home\');';
    } else {
        homePath = webType + '/#/home';
    }
    $('#path').prepend('<a href="/#/home"><i class="fas fa-home"></i>首页<span><small>Home</small></span></a>');
}

// 进入全屏
function enterFullscreen(element) {
    var el = element instanceof HTMLElement ? element : document.documentElement;
    var infs = el.requestFullscreen       ||
               el.webkitRequestFullscreen ||
               el.mozRequestFullScreen    ||
               el.msRequestFullscreen;
    if (infs) {
        infs.call(el);
    } else if (window.ActiveXObject) {
        var ws = new ActiveXObject('WScript.Shell');
        ws && ws.SendKeys('{F11}');
    }
}

// 退出全屏
function exitFullscreen() {
    var outfs = document.exitFullscreen       ||
                document.webkitExitFullscreen ||
                document.mozCancelFullScreen  ||
                document.msExitFullscreen;
    if (outfs) {
        outfs.call(document);
    } else if (window.ActiveXObject) {
        var ws = new ActiveXObject('WScript.Shell');
        ws && ws.SendKeys('{F11}');
    }
}

// 锁屏
function lockScreen() {
    document.onkeydown = function() {
        var e = window.event || arguments[0];
        // 屏蔽 F12
        if (e.keyCode === 123) {
            return false;
        // 屏蔽 Ctrl+Shift+I
        } else if ((e.ctrlKey) && (e.shiftKey) && (e.keyCode === 73)) {
            return false;
        // 屏蔽 Shift+F10
        } else if ((e.shiftKey) && (e.keyCode === 121)) {
            return false;
        }
    };
    // 屏蔽右键单击
    document.oncontextmenu = function() {
        return false;
    };
    $('#locking').remove();
    $('body').append('<div id="locking"><figure onclick="lockInput(this);"><img src="' + sessionStorage.getItem("avatar") + '" alt="' + sessionStorage.getItem("username") + '"></figure><h3>' + sessionStorage.getItem("username") + '</h3></div>');
    setTimeout(function() {
        $('#locking').addClass('lock-ani');
    }, 200);
    sessionStorage.setItem('locked', true);
}

// 锁屏输入
function lockInput(dom) {
    $(dom).find('img').unwrap();
    $('#locking').append('<div class="input-group"><input class="form-control form-control-lg" type="password" placeholder="请输入登录密码解锁"><div class="input-group-append" onclick="unlockScreen();"><span class="input-group-text"><i class="fas fa-key"></i></span></div></div>');
    setTimeout(function() {
        $('#locking .input-group').addClass('lock-input-ani');
    }, 200);
    $('#locking input').focus();
}

// 解锁
function unlockScreen() {
    if ($('#locking input').val() === sessionStorage.getItem('password')) {
        $('#locking').fadeOut(300, function() {
            $('#locking').remove();
        });
        sessionStorage.removeItem('locked');
        document.onkeydown = function() {
            var e = window.event || arguments[0];
            // 屏蔽 F12
            if (e.keyCode === 123) {
                return true;
                // 屏蔽 Ctrl+Shift+I
            } else if ((e.ctrlKey) && (e.shiftKey) && (e.keyCode === 73)) {
                return true;
                // 屏蔽 Shift+F10
            } else if ((e.shiftKey) && (e.keyCode === 121)) {
                return true;
            }
        };
        // 屏蔽右键单击
        document.oncontextmenu = function() {
            return true;
        };
    } else {
        noticeMsg('密码错误！请重新输入~', 'error', 'top', 3000);
    }
}

// 配色
function changeColor(color, accent, minor) {
    $('#Amikoko').attr('href', 'css/themes/theme_' + color + '.min.css');
    if ($('#hasChart').length > 0) {
        setTimeout(function() {
            kendo.dataviz.autoTheme(true);
            refresh();
        }, 100);
    }
    localStorage.setItem('colorName', color);
    localStorage.setItem('accentColor', accent);
    accentColor = accent;
    localStorage.setItem('minorColor', minor);
    minorColor = minor;
}

// 语言
function changeLang(lang) {
    $.getScript('js/global/kendo.' + lang + '.js', function() {
        kendo.culture(lang);
        refresh();
    });
}

// 退出登录
function logout() {
    sessionStorage.clear();
    location.href = '/auth/login/';
}