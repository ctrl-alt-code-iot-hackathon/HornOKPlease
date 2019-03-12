console.log("LOADED!!!")

var lat = (Math.random()*180);
var long = (Math.random()*180);

console.log(lat);
console.log(long);
$(document).ready(function(){
  document.all.setme1.innerHTML = lat;
  document.all.setme2.innerHTML = long;
});
$(document).ready(function(){
  $("#btn1").click(function(){
  console.log("Left button clicked!");
  $.ajax({
    url: "http://192.168.43.6/left",
    method: "get",
    crossDomain : true,
    success: function(){
      console.log("sent request!")
    },
    error: function(){
      console.log("failed!")
    }
    })
});
});

$(document).ready(function(){
  $("#btn2").click(function(){
  console.log("Up button clicked!");
  $.ajax({
    url: "http://192.168.43.6/forward",
    method: "get",
    crossDomain : true,
    success: function(){
      console.log("sent request!")
    },
    error: function(){
      console.log("failed!")
    }
    })
});
});

$(document).ready(function(){
  $("#btn3").click(function(){
  console.log("Right button clicked!");
  $.ajax({
    url: "http://192.168.43.6/right",
    method: "get",
    crossDomain : true,
    success: function(){
      console.log("sent request!")
    },
    error: function(){
      console.log("failed!")
    }
    })
});
});

$(document).ready(function(){
  $("#btn4").click(function(){
  console.log("Down button clicked!");
  $.ajax({
    url: "http://192.168.43.6/down",
    method: "get",
    crossDomain : true,
    success: function(){
      console.log("sent request!")
    },
    error: function(){
      console.log("failed!")
    }
    })
});
});

$(document).ready(function(){
  $("#btn5").click(function(){
  console.log("Halt button clicked!");
  $.ajax({
    url: "http://192.168.43.6/off",
    method: "get",
    crossDomain : true,
    success: function(){
      console.log("sent request!")
    },
    error: function(){
      console.log("failed!")
    }
    })
});
});