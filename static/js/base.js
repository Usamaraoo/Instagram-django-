console.log('base js');



function clicked_soty(user_id, user_img, user_name) {
    console.log(
        'this is user id', user_id, user_img
    );
    // Get the modal
    var modal = document.getElementById("storyModal");
    var modal_content = document.getElementsByClassName("modal-content");

    // Get the button that opens the modal
    var btn = document.getElementById(`storybtn${user_id}`);

    // Get the <span> element that closes the modal
    var span = document.getElementsByClassName("close")[0];

    // When the user clicks the button, open the modal 
    btn.onclick = function () {
        modal.style.display = "block";
        // setting username and story image
        var name = document.getElementById('stryusername');
        name.innerHTML = user_name;
        img = document.getElementById('storyimg')
        img.src = user_img;

        $('#storyModal').delay(3000).hide(0);

    }

    // When the user clicks on <span> (x), close the modal
    span.onclick = function () {
        modal.style.display = "none";
        // modal_content[0].children[1].remove()
        // modal_content[0].children[2].remove()


    }

    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function (event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }


    load_bar();

}

var i = 0;
function load_bar() {
    if (i == 0) {
        i = 1;
        var elem = document.getElementById("myBar");
        var width = 1;
        var id = setInterval(frame, 40);
        function frame() {
            if (width >= 100) {
                clearInterval(id);
                i = 0;
            } else {
                width++;
                elem.style.width = width + "%";
            }
        }
    }
}
