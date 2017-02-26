var h = document.getElementsByClassName("hours")[0];
var m = document.getElementsByClassName("minutes")[0];
var s = document.getElementsByClassName("seconds")[0];
var d = document.getElementsByClassName("days")[0];
var eventDate = new Date("March 10, 2017 00:00:00");

function updateCountdown() {
    var currentDate = new Date();
    t = eventDate - currentDate;
    var seconds = Math.floor((t / 1000) % 60);
    var minutes = Math.floor((t / 1000 / 60) % 60);
    var hours = Math.floor((t / (1000 * 60 * 60)) % 24);
    var days = Math.floor(t / (1000 * 60 * 60 * 24));
    h.innerHTML = (hours / 10) < 1 ? "0" + hours : "   " + hours;
    m.innerHTML = (minutes / 10) < 1 ? "0" + minutes : "" + minutes;
    s.innerHTML = (seconds / 10) < 1 ? "0" + seconds : "" + seconds;
    d.innerHTML = (days / 10) < 1 ? "0" + days : "" + days;
}

setInterval(updateCountdown, 1000);

$(document).ready(function() {
    // any code goes here
    var delayMillis = 1000; //1 second

    setTimeout(function() {
        //your code to be executed after 1 second
        var ldr = document.querySelectorAll(".loader")[0];
        ldr.style.display = "none";
    }, delayMillis);
});