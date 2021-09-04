

// Ajax Like
function liked(id) {
    // e.preventDefault();
    // alert($(this).val())
    var post_id = id
    $.ajax({
        url: '/liked/',
        data: {
            'post_id': post_id
        },
        dataType: 'json',
        success: function (data) {
            like_btn = document.getElementById(`${post_id}`)
            if (data.status) {
                like_btn.style.fill = 'red'
            }
            else {
                like_btn.style.fill = 'black'
            }
        }
    });
}
// Ajax comment
function add_comment(e, postid) {
    e.preventDefault();

    $.ajax({
        type: "POST",
        // url: "{% url 'ajax_posting' %}",
        url: "/comment/",

        data: {
            post_id: postid,
            comment: $('#cmntinput' + postid).val(),

            csrfmiddlewaretoken: '{{ csrf_token }}',
            dataType: "json",
        },

        success: function (data) {
            $('#cmntinput' + postid).val('') // clearing input field
            form = document.getElementById('cmntpost' + postid)
            div = document.getElementsByClassName(postid)[0]
            img = document.createElement('img')
            inner_div = document.createElement('div') // inner div
            inner_div.classList.add('cmnt_div');
            cmnt = document.createElement('p')
            username = document.createElement('strong')

            img.src = data.img_url
            img.style.width = '30px'
            img.style.height = '30px'
            img.style.borderRadius = '50%'
            img.style.float = 'left'

            n = document.createTextNode(data.username)
            text = document.createTextNode(data.comment)
            username.appendChild(n)
            cmnt.appendChild(text)
            div.insertBefore(img, form)// adding imgd 
            inner_div.appendChild(username)
            inner_div.appendChild(cmnt)
            div.insertBefore(inner_div, form) //adding inner div
            console.log(data);
        },

        failure: function () {
            console.log('error');
        }
    });
}

// Comments Collapse

var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
    coll[i].addEventListener("click", function () {
        this.classList.toggle("active");
        var content = this.nextElementSibling;
        if (content.style.display === "block") {
            content.style.display = "none";
        } else {
            content.style.display = "block";
        }
    });
}