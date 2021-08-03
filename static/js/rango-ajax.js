$(document).ready(function() {
    $('#like_btn').click(function() {
        var catecategoryIdVar;
        catecategoryIdVar = $(this).attr('data-categoryid');

        $.get('/rango/like_category/',
             {'category_id': catecategoryIdVar},
             function(data) {
                $('#like_count').html(data);
                $('#like_btn').hide();
            })
        });

   
    $( "#post_btn" ).click(function( event ) {
        // Stop form from submitting normally
        event.preventDefault();
        var catecategoryIdVar, comments, rating;

        catecategoryIdVar = $(this).attr('data-categoryid');
        comments = $('#txt_comment').val()
        rating = $("input[name='RatingRadioOptions']:checked").val();

        $.ajax({
            type:'GET',
            url: '/rango/post_comment/',
            data: {'category_id': catecategoryIdVar, 'comments':comments, 'rating':rating},
            success: function(data){
                $('#option_msg').html('Thanks for your opinion.');
                $('#post_btn').prop('disabled', true);
                $('#txt_comment').prop('disabled', true);
                $("input[type=radio]").attr('disabled', true);
            },
            contentType: "application/json",
            dataType: 'json'
        });
        
    });
});