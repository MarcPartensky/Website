Dropzone.autoDiscover = false;
$(function() {
    const dropzone = new Dropzone("#dropzone");

    dropzone.on("success", function(file, responseText) {
        window.location.href = `/article/${file.name.replace('.md', '')}`
    });
})
