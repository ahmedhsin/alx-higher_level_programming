const redHeader = $('DIV#red_header');
const header = $('header');
redHeader.on('click', function () {
  header.color = '#FF0000';
});
