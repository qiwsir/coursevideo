var WEB = "http://127.0.0.1:8888/"

//校验手机号码：必须以数字开头，除数字外，可含有“-”

function isMobil(s)
{
    var patrn=/^(1[3,5,8,7]{1}[\d]{9})|(((400)-(\d{3})-(\d{4}))|^((\d{7,8})|(\d{4}|\d{3})-(\d{7,8})|(\d{4}|\d{3})-(\d{3,7,8})-(\d{4}|\d{3}|\d{2}|\d{1})|(\d{7,8})-(\d{4}|\d{3}|\d{2}|\d{1}))$)$/;
    if (!patrn.exec(s)) return false
    return true
}

//校验登录名：只能输入5-20个以字母开头、可带数字、“_”、“.”的字串

function isRegisterUserName(s)
{
    var patrn=/^[\u4e00-\u9fa5_a-zA-Z0-9]+$/;
    if (!patrn.exec(s)) return false
    return true
}

//检验是否为中文、英文、数字、"_"或减号

function isChinese(s)
{
    var patrn=/^[\u4e00-\u9fa5A-Za-z0-9_\-]+$/;
    if (!patrn.exec(s)) return false
    return true
}

$(document).ready(function(){
    $("#login").click(function(){
        var username = $("#username").val();
        var password = $("#password").val();
        
        var check_input = /^([A-Za-z0-9])+$/;

        var username_checked = check_input.test(username);
        var password_checked = check_input.test(password);

        if (username_checked && password_checked){
            var user_data = {"username":username, "password":password};
            $.ajax({
                type: "post",
                url: "/",
                data: user_data,
                cache: false,
                success: function(e){
                    if (e=="1"){
                        location.href= WEB + "admin?user=" + username
                    }else if (e=="0"){
                        alert("username or passwor is false.")
                    }else {
                        alert("are you a human?")
                    }
                },
                error: function(e){
                    alert("ah");
                },
            })
        } else {
            alert("please go out.")
        }
    })
})

//增加新的场馆
$(document).ready(function(){
    $("#addorg").click(function(){
        var orgname = $("#orgname").val();
        var orgperson = $("#orgperson").val();
        var orgphone = $("#orgphone").val();
        var orgwechat = $("#orgwechat").val();
        var orgaddress = $("#orgaddress").val();

        var isname = isChinese(orgname);
        var isperson = isChinese(orgperson);
        var isphone = isMobil(orgphone);
        var iswechat = isChinese(orgwechat);
        var isaddress = isChinese(orgaddress);

        if (isname && isperson && isphone && iswechat && isaddress){
            var post_data = {"orgname":orgname, "orgperson":orgperson, "orgphone":orgphone, "orgwechat":orgwechat, "orgaddress":orgaddress}

            $.ajax({
                type: "post",
                url: "/neworg",
                data: post_data,
                cache: false,
                async: false,
                success: function(e){
                    if (e=="1"){
                        layer.msg("恭喜！添加成功。还可以继续添加。");
                        location.reload();
                    } else if (e=="-1"){
                        layer.msg("此场馆已经添加了，请不要重复添加。")
                    } else {
                        layer.msg("Sorry!没能添加，请重试。")
                    }
                },
                error: function(e){
                    layer.msg("操作失败，请检查网络。")
                }
            }
            ) 
        } else {
            layer.msg("没有认真填写各项，再来一边。")
        }
    })
})


$(document).ready(function(){
    $("#submitcategory").click(function(){
        var category_name = $("#categoryname").val();
        if (category_name){
            var vategoryname = {"category_name":category_name}
            $.ajax({
                type: "post",
                url: "/audio",
                data: vategoryname,
                success: function(e){
                    if (e=="1"){
                        alert("ok, the category is right.")
                    } else {
                        alert("you are wrong.")
                    }
                }
            })
        } else {
            alert("You should input category name.")
        }
    })
})
