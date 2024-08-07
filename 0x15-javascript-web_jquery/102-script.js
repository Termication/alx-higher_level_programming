// Wait for the document to be fully loaded
$(document).ready(function () {
  // Define the base URL for the API request
  const url = 'https://www.fourtonfish.com/hellosalut/?';
  
  // Add a click event listener to the element with id 'btn_translate'
  $('INPUT#btn_translate').click(function () {
    // Construct the full URL with query parameters based on the value of the input field with id 'language_code'
    $.get(url + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
      // Update the content of the <DIV> with id 'hello' with the 'hello' property from the response data
      $('DIV#hello').html(data.hello);
    });
  });
});
