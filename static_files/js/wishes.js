$(function() {
    var link = null;
    $("#wishes").on("click", ".comment", function(event) {
        event.preventDefault();
        link = $(this).attr("href");
        $( "#comments" ).load( link,  function() {
            $('.modal').modal('open');
        });
    });

    $(document).on("submit", "#add_comment", function(event) {
        event.preventDefault();
        console.log("Submit");
        var postData = {
            name: $("#name").val(),
            comment: $("#comment").val(),
        };

        $.post(link, postData, function(){
            $( "#comments" ).load( link );
        });
    });
});