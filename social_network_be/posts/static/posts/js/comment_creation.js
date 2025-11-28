$(document).ready(function () {
    $(".comment-form").submit(function (e) {
        e.preventDefault();

        let form = $(this);
        let postId = form.data("post-id");
        let input = form.find(".comment-input");
        let text = input.val().trim();
        if (!text) return;

        let csrfToken = form.find("input[name=csrfmiddlewaretoken]").val();

        $.ajax({
            url: `/create-comment/${postId}/`,
            type: "POST",
            dataType: "json",
            data: {
                text: text,
                csrfmiddlewaretoken: csrfToken
            },
            success: function (response) {

            let newComment = $(`
                    <div class="comment">
                        <div class="comment-body">
                            <span class="comment-user">${response.user}</span>
                            <p class="comment-text">${response.text}</p>
                        </div>
                    </div>
                `);

                $(`#comment-list-${postId}`).prepend(newComment);

                // добавляем класс для анимации
                setTimeout(() => {
                    newComment.addClass("show");
                }, 10); // add the comment in above
                input.val("");
            }
        });
    });
});


