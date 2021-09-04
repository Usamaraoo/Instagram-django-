
function follow(username) {
    console.log(username);
    $.ajax({
        url: '/ajax_follow',
        data: {
            'username': username
        },
        datatype: 'json',
        success: function (data) {
            l = document.getElementById('follow')
            if (data.followed === true) {
                l.children[0].innerText = "unfollow"
                l.children[0].style.backgroundColor = "rgb(112, 223, 78)"
            }
            else {
                l.children[0].innerText = "follow"
                l.children[0].style.backgroundColor = " rgb(98, 169, 216)"
            }
        },
        failure: function () {
            console.log('error');
        }
    });
}

// flw = document.getElementById('follow')



