console.log("LOADED!!!")

$(document).ready(function(){
  $("#btn1").click(function(){
  console.log("Left button clicked!");
  $.ajax({
    url: "/left",
    method: "get",
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
    url: "/up",
    method: "get",
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
    url: "/right",
    method: "get",
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
    url: "/down",
    method: "get",
    success: function(){
      console.log("sent request!")
    },
    error: function(){
      console.log("failed!")
    }
    })
});
});
