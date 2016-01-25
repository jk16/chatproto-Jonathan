$( document ).ready(function() {
    var $loginForm = $("#loginForm");
    var $chatBarForm = $("#chatBarForm");
    var $login = $("#login");
    var $chatBar = $("#chatBar");
    $loginForm.show();
    
    $login.on('submit', function(e) {

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
                $loginForm.hide();
                $chatBarForm.show();
            }
        })

    }); //end login on submit

    $chatBar.on("submit", function(e) {
        e.preventDefault();

        var $user = $("#username");
        var $msg = $("#msg");

        var data = {
            username: $user.val(),
            message: $msg.val()
        };

        var data_JSON = JSON.stringify(data);

        $.ajax({
            type: 'POST',
            url: '/msg',
            data: data,
            success: function(response) {
                //
                console.log('success');
            }
        });
    });
});