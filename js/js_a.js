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