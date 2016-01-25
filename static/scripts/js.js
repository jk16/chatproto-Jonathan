$( document ).ready(function() {
    var $loginForm = $("#loginForm");
    var $chatBarForm = $("#chatBarForm");
    $loginForm.show();
    
    $('#login').on('submit', function(e) {

        e.preventDefault();

        var $user = $("#username");
       
        var message = {
            username: $user.val()
        };

        var message_JSON = JSON.stringify(message);

        $.ajax({
            type: 'POST',
            url: '/login',
            data: message,
            success: function(response) {
                //server response that the data was received 
                console.log("success");
                $loginForm.hide();
                $chatBarForm.show();
            }
        })

    }); //end login on submit
});