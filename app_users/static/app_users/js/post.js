img = document.getElementById('id_post_img')
img_show = document.getElementById('shwimg')
img.addEventListener("change", function () {
    // Second
    var file = img.files[0];
    var fileType = file["type"];
    var validImageTypes = ["image/gif", "image/jpeg", "image/png", "image/webp"];
    // invalid file type code goes here.
    if ($.inArray(fileType, validImageTypes) < 0) {
        console.log('this is video');
        const url = URL.createObjectURL(file)

        img_show.innerHTML = `
        <video width="320" height="300" controls muted >
            <source src="${url}" type="video/mp4">
            Your browser does not support the video tag.
        </video>
      `
    }
    else {
        console.log('this is image');
        // const img_data = img.files[0]
        const url = URL.createObjectURL(file)
        img_show.innerHTML = `<img  src="${url}" width="300px" height="300px"  >`
    }
});

console.log('New fun');

$("form").submit(function () {
    console.log('file checkk');
    if (window.File && window.FileReader && window.FileList && window.Blob) {
        var file = $('#id_post_img')[0].files[0];

        if (file && file.size > 2 * 1024 * 1024) {
            alert("File " + file.name + " of type " + file.type + " is too big");
            return false;
        }
    }
});
