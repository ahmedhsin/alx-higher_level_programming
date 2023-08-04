$.ajax({
  url: 'https://fourtonfish.com/hellosalut/?lang=fr/',
  method: 'GET',
  xhrFields: {
    withCredentials: true
  },
  headers: {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Credentials': 'True'

  },
  success: function (data) {
    const char = $('DIV#hello');
    char.text(data.hello);
  }
});
