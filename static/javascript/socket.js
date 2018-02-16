$(document).ready(function() {
  // Connect to localhost.
  var socket = io.connect(location.origin);

  // Sent when socket is connected.
  socket.on('connect', function() {
    socket.send('User has connected!');
  });

  // Append message to div on socket call.
  socket.on('append-to-div', function(msg) {
    $("#messages").append('<li>' + msg + '</li>');
    console.log('Received message');
  });

  // Emits socket
  $('#sendbutton').on('click', function() {
    socket.emit("grab-field-data", $('#myMessage').val());
    $('#myMessage').val('');
  });

});