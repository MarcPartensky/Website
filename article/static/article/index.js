$(function() {
  var dropzone = new Dropzone("#dropzone");
    dropzone.on("success", function(file, responseText) {
      window.location.href = "/api/addition?a=1?b=2"
    });
})


