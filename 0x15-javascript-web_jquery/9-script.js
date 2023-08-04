$.get('https://hellosalut.stefanbohacek.dev/?lang', function (data, status) {
  const char = $('DIV#hello');
  char.text(data.hello);
});
