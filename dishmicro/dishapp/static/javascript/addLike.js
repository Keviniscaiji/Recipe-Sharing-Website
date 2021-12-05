
function addLike(id){
$.post('/addlike', {
        'dish_id': id
    }).done (function (response) {
        let server_response = response['text']
        alert(server_response)
        location.reload();
    })
}
