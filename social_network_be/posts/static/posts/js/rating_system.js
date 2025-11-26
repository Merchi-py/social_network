$(".likeBtn").click(function() {
    let post_id = $(this).data("post-id");

    $.ajax(`/like_system/${post_id}/`, {
        "type": 'POST',
        "async": true,
        "dataType": 'json',
        "data": {
            "csrfmiddlewaretoken": $('[name="csrfmiddlewaretoken"]').val()
        },
        "success": function(response) {
            $(`.like-count[data-post-id="${post_id}"]`).text(response.response.likes_count);
            $(`.dislike-count[data-post-id="${post_id}"]`).text(response.response.dislikes_count);
        }
    });
});


$(".dislikeBtn").click(function() {
    let post_id = $(this).data("post-id");

    $.ajax(`/dislike_system/${post_id}/`, {
        "type": 'POST',
        "async": true,
        "dataType": 'json',
        "data": {
            "csrfmiddlewaretoken": $('[name="csrfmiddlewaretoken"]').val()
        },
        "success": function(response) {
                $(`.dislike-count[data-post-id="${post_id}"]`).text(response.response.dislikes_count);
            $(`.like-count[data-post-id="${post_id}"]`).text(response.response.likes_count);
        }
    });
});
