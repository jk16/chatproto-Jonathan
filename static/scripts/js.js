$( document ).ready(function() {
    var $loginForm = $("#loginForm");
    var $logoutForm = $("#logoutForm");
    var $chatBoxForm = $("#chatBoxForm");
    $loginForm.show();
    
    $loginForm.on('submit', function(e) {

        e.preventDefault();

        var $user = $("#username");
       
        var message = {
            username: $user.val()
        };

        $.ajax({
            type: 'POST',
            url: '/login',
            data: message,
            success: function(response) {
                //server response that the data was received 
                $loginForm.hide();
                $chatBoxForm.show();
                $logoutForm.show();
            }
        })

    }); //end login on submit

    $chatBoxForm.on("submit", function(e) {
        e.preventDefault();
        var $user = $("#username");
        var $msg = $("#msg");

        var data = {
            username: $user.val(),
            message: $msg.val()
        };

        $.ajax({
            type: 'POST',
            url: '/msg',
            data: data,
            success: function(response) {
                console.log('success: chatBarForm submit');
            }
        });
    }); //end chatBar on submit

    $logoutForm.on("submit", function(e){
        e.preventDefault();
        var $user = $("#username");

        var message = {
            username: $user.val()
        };

        $.ajax({
            type: 'POST',
            url: '/logout',
            data: message,
            success: function(response) {
                $loginForm.show();
                $chatBoxForm.hide();
                $logoutForm.hide();
            }
        })
    }); //end logoutForm on submit
});