const toggelHeader = $('DIV#toggle_header');
const header = $('header');
toggelHeader.on('click', function () {
  if (header.hasClass('red')) {
    header.addClass('green');
    header.removeClass('red');
  } else {
    header.addClass('red');
    header.removeClass('green');
  }
});
