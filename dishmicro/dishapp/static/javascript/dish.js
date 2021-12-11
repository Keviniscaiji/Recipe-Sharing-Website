$(document).ready(function () {
    $(".word_count").bind("input propertychange", function () {
        word_count()
    });
    $(".post_title").bind("input propertychange", function () {
        change_title_style()
    });
    $(".author_link").on("click", function () {
        // console.log(this.classList[1])
        let id = this.classList[1]
        $.post('/checkuser', {
            "type": "get_user_info",
            "id": id
        }).done(function (response) {
            let server_response = response["text"]
            if (response["returnvalue"] == 0) {
                alert(server_response)
            } else if (response["returnvalue"] == 1) {
                alert(server_response + ": \n\n" +
                    "date of birth: " + response["dob"] + "\n"
                    + "country: " + response["country"] + "\n" +
                    "gender: " + response["gender"])
            }
        }).fail(function () {
            alert("The user may not in database")
        })
    })

// check post's format and return the problem of it
    $("#submit_post").on("click", function (event) {
        let msg = ""
        if ($("#post_title").val().length > 0 && $("#post_title").val().length < 30 && $("#post_body").val().length > 0 && $("#post_body").val().length < 10000
            && $("#post_pic").val() != "") {
            alert("Post Success")
            return
        }
        if ($("#post_title").val().length == 0 || $("#post_title").val().length > 30) {
            msg += ("Please check your title(length should smaller than 30) \n")
        }
        if ($("#post_body").val().length == 0 || $("#post_body").val().length > 10000) {
            msg += ("Please check your body(length should smaller the 10000)\n")
        }
        if ($("#post_pic").val().length == 0) {
            msg += ("Please add an picture for your post\n")
        }

        if (msg != "") {
            alert("Your post have following problems\n\n" + msg)
        }
    })
});

// code for word count and change the style of post when user enter
function word_count() {
    let char_len = $(".word_count").val().match(/[a-zA-Z]+/mg).length
    document.getElementById("show_word_count").innerHTML = "Number of words: " + char_len + "";
    if (char_len > 0 && $(".word_count").val().length > 0) {
        document.querySelector(".word_count").style.backgroundColor = "grey"
    }
}
//Change the style of the input box when the user enters text
function change_title_style() {
    let char_len = $(".post_title").val().match(/[a-zA-Z]+/mg).length
    if (char_len > 0 && $(".post_title").val().length > 0) {
        document.querySelector(".post_title").style.backgroundColor = "grey"
    }
}


// code for transform between light mode and dark mode
function changeStyle() {
    let sty = $('#select_style  option:selected').val();
    if (sty == "white") {
        $.post("/change_style", {
            style_location: 'style/mystyle_white.css'
        }).done(function (response) {
            let server_response = response["text"]
            alert(server_response)
            location.reload();
        }).fail(function () {
            alert("change style fail")
        })

    } else if (sty == "black") {
        $.post("/change_style", {
            style_location: 'style/mystyle_black.css'
        }).done(function (response) {
            let server_response = response["text"]
            alert(server_response)
            location.reload();
        }).fail(function () {
            alert("change style fail")
        })
    }
}

