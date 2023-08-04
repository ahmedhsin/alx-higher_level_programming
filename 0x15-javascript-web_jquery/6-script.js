const click = $('DIV#update_header');
click.on('click', function () {
  const header = $('header');
  header.text('New Header!!!');
});
