function getTimeRemaining(starttime, expire){

  if (starttime < 0) {
    var total = 0
  }
  else {
    var total = expire - (Math.floor(new Date() / 1000) - starttime)
  }
  
  var seconds = total % 60;
  var minutes = Math.floor(total/60) % 60;
  var hours = Math.floor(total/(60*60)) % 24;

  return {
    'total': total,
    'hours': hours,
    'minutes': minutes,
    'seconds': seconds
  };

}

function initializeClock(id, starttime, expire) {
  var clock = document.getElementById(id);
  var hoursSpan = clock.querySelector('.hours');
  var minutesSpan = clock.querySelector('.minutes');
  var secondsSpan = clock.querySelector('.seconds');

  function updateClock() {
    var t = getTimeRemaining(starttime, expire);

    hoursSpan.innerHTML = ('0' + t.hours).slice(-2);
    minutesSpan.innerHTML = ('0' + t.minutes).slice(-2);
    secondsSpan.innerHTML = ('0' + t.seconds).slice(-2);

    if (t.total <= 0) {
      clearInterval(timeinterval);
    }
  }

  updateClock();
  var timeinterval = setInterval(updateClock, 1000);
}
