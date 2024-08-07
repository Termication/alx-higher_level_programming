// Wait for the document to be fully loaded
$(document).ready(function () {
  // Make an AJAX GET request to the specified URL
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
    // Set the text of the <DIV> with id 'hello' to the 'hello' property of the response data
    $('DIV#hello').text(data.hello);
  });
});
