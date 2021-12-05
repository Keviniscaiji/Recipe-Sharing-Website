function remove_dish(id) {
    let a = confirm("Are you sure?")
    if (a) {
        $.post('/manage_database', {
            "type": "remove_single_dish",
            "id":id
        }).done(function (response) {
            let server_response = response["text"]
            alert(server_response)
            location.reload();
        }).fail(function (){
            alert("remove dish fail")
        })
    }
}

function remove_all_dishes() {
    let a = confirm("Are you sure?")
    if (a) {
        $.post('/manage_database', {
            "type": "remove_all_dishes"
        }).done(function (response) {
            let server_response = response["text"]
            alert(server_response)
            location.reload();
        }).fail(function (){
            alert("remove dishes fail")
        })
    }
}

function remove_user(id) {
    let a = confirm("Are you sure?")
    if (a) {
        $.post('/manage_database', {
            "type": "remove_single_user",
            "id": id
        }).done(function (response) {
            let server_response = response["text"]
            alert(server_response)
            location.reload();
        }).fail(function (){
            alert("remove user fail")
        })
    }
}

function remove_all_users() {
    let a = confirm("Are you sure?")
    if (a) {
        $.post('/manage_database', {
            "type": "remove_all_users"
        }).done(function (response) {
            let server_response = response["text"]
            alert(server_response)
            location.reload();
        }).fail(function (){
            alert("remove users fail")
        })
    }
}