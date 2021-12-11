let msg2 = ""
let msg3 = ""
$(document).ready(function () {
    $("#signup_username").bind("input propertychange", function () {
        check_username()
    });
    $("#signup_email").bind("input propertychange", function () {
        check_email()
    });
})
$(function () {

    $("#signup_email").bind('input propertychange', function () {
        let a = $("#signup_email").val()
        if (/^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/.test(a)) {
        }
    })
    //check whether password longer than 6 charachers
    $("#signup_password1").bind('input propertychange', function () {
        let a = $("#signup_password1").val()
        if (a.length < 6) {
            $("#signup_password1").attr("class", "failure flask_form")
            $("#check_signup_password1").html(('<span class="alert_span_password1"> not longer than 6 characters </span>'))
        } else {
            $("#signup_password1").attr("class", "success flask_form")
            let alert_span = document.querySelector(".alert_span_password1") || null
            if (alert_span != null) {
                alert_span.remove()
            }
        }
    })
    //check whether password are consistent
    $("#signup_password2").bind('input propertychange', function () {
        let a = $("#signup_password2").val()
        let b = $("#signup_password1").val()
        if (a != b) {
            password2_pass = false
            $("#signup_password2").attr("class", "failure flask_form")
            $("#check_signup_password2").html(('<span class="alert_span_password2"> Passwords inconsistent</span>'))
        } else {
            password2_pass = true
            $("#signup_password2").attr("class", "success flask_form")
            let alert_span = document.querySelector(".alert_span_password2") || null
            if (alert_span != null) {
                alert_span.remove()
            }
        }
    })



    //The error message is displayed so that the user can know which parts need to be modified, all the
    //things that user need to change will be displayed
    $("#sign_up_button").on("click", function () {
        let msg = ""
        if ($("#signup_password1").val().length < 6) {
            msg += "the length of password should not be shorter than 6\n"
        }
        if ($("#signup_password1").val() != $("#signup_password2").val()) {
            msg += "Two passwords are inconsistent\n"
        }
        if ($("#signup_username").val() == "") {
            msg += "please enter a username\n"
        }
        if ($("#signup_email").val() == "") {
            msg += "please enter a email\n"
        }
        if ($("#signup_username").val() == "manager") {
            msg += "sorry, you can not use \"manager\" as your username \n"
        }
        check_username()
        check_email()
        msg += msg2
        msg += msg3

        if (msg == "") {
            alert("sign up success :-D")
        } else {
            alert("Sorry, your input have problems below：\n" + msg)
        }
    })
})
 //check whether the username is already used
 function check_username() {
        let chosen_user = $("#signup_username")
        $.post('/checkuser', {
            'username': chosen_user.val(),
            'type': "username"
        }).done(function (response) {
            let server_response = response['text']
            let server_code = response["returnvalue"]
            if (server_code == 0) {
                // $("#password").focus();
                $("#check_username").html(('<span>' + server_response + '</span>'))
                chosen_user.attr("class", "success flask_form")
                msg2 = ""
            } else {
                // chosen_user.val("");
                chosen_user.focus();
                $("#check_username").html(('<span>' + server_response + '</span>'))
                chosen_user.attr("class", "failure flask_form")
                msg2 = "The user name has already be used \n"
            }
        }).fail(function () {
            $("#check_username").html("<span>Error contacting server</span>")
            chosen_user.attr("class", "failure flask_form")
            msg2 = "The user name has already be used \n"
        });
    }
    //check whether the email meet the format requirement and whether the email is already used
    function check_email() {
        let chosen_email = $("#signup_email")
        // $("#check_signup_email").html("<img src='../style/loading.gif' class='loading_pic'> ")
        $.post('/checkuser', {
            'email': chosen_email.val(),
            'type': "email"
        }).done(function (response) {
            let server_response = response['text']
            let server_code = response["returnvalue"]
            if (server_code == 0 && /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/.test(chosen_email.val())) {
                // $("#password").focus();
                $("#check_signup_email").html(('<span>' + server_response + '</span>'))
                chosen_email.attr("class", "success flask_form")
                msg3 = ""
            } else if (!/^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/.test(chosen_email.val())) {
                $("#check_signup_email").html(('<span>' + "Check the format of emial" + '</span>'))
                chosen_email.attr("class", "failure flask_form")
                msg3 = "The email format have some problem\n"
            } else {
                $("#check_signup_email").html('<span>' + server_response + '</span>')
                chosen_email.attr("class", "failure flask_form")
                msg3 = "The email has already be used \n"
            }
        }).fail(function () {
            $("#check_signup_email").html("<span>Error contacting server</span>")
            chosen_email.attr("class", "failure flask_form")
            return ""
        });
    }