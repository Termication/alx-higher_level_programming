// Wait for the document to be fully loaded
$(document).ready(function () {
  // Add a click event listener to the element with id 'btn_translate'
  $('INPUT#btn_translate').click(translate);
  
  // Add a focus event listener to the input field with id 'language_code'
  $('INPUT#language_code').focus(function () {
    // Add a keydown event listener to the input field
    $(this).keydown(function (e) {
      // Check if the pressed key is the Enter key (key code 13)
      if (e.keyCode === 13) {
        // Call the translate function when Enter key is pressed
        translate();
      }
    });
  });
});

// Define the translate function
function translate () {
  // Define the base URL for the API request
  const url = 'https://www.fourtonfish.com/hellosalut/?';
  
  // Make an AJAX GET request with the query parameter 'lang' set to the value of the input field with id 'language_code'
  $.get(url + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
    // Update the content of the <DIV> with id 'hello' with the 'hello' property from the response data
    $('DIV#hello').html(data.hello);
  });
}
