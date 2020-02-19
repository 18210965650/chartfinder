function load(){
    var div = document.getElementById("showtime");
    div.innerHTML = showtime();
setInterval(function() {div.innerHTML = showtime();}, 1000); 
}