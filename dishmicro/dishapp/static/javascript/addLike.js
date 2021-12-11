//Allow users to likedish and record the number of likes in the database
function addLike(id){
$.post('/addlike', {
        'dish_id': id
    }).done (function (response) {
        let server_response = response['text']
        alert(server_response)
        location.reload();
    })
}
