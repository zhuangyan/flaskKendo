$(function() {
    // 表单验证
    var validator = $('form').kendoValidator({
        rules: {
            // 匹配密码
            matchPassword: function(input) {
                if (!input.is('[name=confirmPassword]')) {
                    return true;
                }
                return (input.val() === $('[name=newpassword]').val());
            }
        },
        messages: {
            matchPassword: '两次输入的密码不一致！'
        }
    }).data('kendoValidator');
    // 表单提交
    $('#submitBtn').unbind('click').click(function() {
        if (validator.validate()) {
            $(this).removeClass('k-state-selected').addClass('k-state-disabled').prop('disabled', true);
            noticeMsg('开始提交表单……', 'success', 'center', 500, function() {
                oldpassword = $('[name=oldpassword]').val();
                newpassword = $('[name=newpassword]').val();
                 $.fn.ajaxPost({
                        ajaxData: {"oldpassword":oldpassword,"newpassword":newpassword},
                        ajaxType: 'post',
                        ajaxUrl: "/_api/auth/password/",
                        succeed: function(res) {
                            // alert("修改完成");
                             $("#submitBtn").removeClass('k-state-disabled').addClass('k-state-selected').prop('disabled', false);

                        },
                        failed: function(res) {
                            //options.error(res);
                            // alert("旧密码不正确");
                            $("#submitBtn").removeClass('k-state-disabled').addClass('k-state-selected').prop('disabled', false);
                        }
                    });
            });
        } else {
            noticeMsg('表单中有选项未填写正确！请检查……', 'error', 'center', 2000, function() {
                // 出错定位
                $('.k-invalid-msg:visible').first().parents('.form-group').focus();
            });
        }
    });
});