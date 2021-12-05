function check_username_and_password() {
        if( $("#username_form_login").val()==""){
            alert("Please enter your username")
            return
        }
        if( $("#password_form_login").val().length<6){
            alert("Please enter your password(should longer than 6 characters)")
            return;
        }

        let chosen_user = $("#username_form_login")
        let password =  $("#password_form_login")
        $.post('/checkuser', {
            'username': chosen_user.val(),
            'password':password.val(),
            'type': "check_username_and_password"
        }).done(function (response) {
            let server_response = response['text']
            let server_code = response["returnvalue"]
            if (server_code == 11) {
                alert(server_response)
                chosen_user.attr("class", "success flask_form")
                password.attr("class", "success flask_form")
            } else {
                chosen_user.focus();
                alert(server_response)
                chosen_user.attr("class", "failure flask_form")
                password.attr("class", "failure flask_form")
            }
        }).fail(function () {
            alert(server_response)
            chosen_user.attr("class", "failure flask_form")
        });
    }