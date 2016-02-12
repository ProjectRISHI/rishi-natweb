// Filter
var $boxs = $("#parent > .row > .col-md-4");
var $btns = $(".btn").on("click", function() {
  
  var active = 
    $btns.removeClass("active")
      .filter(this)
      .addClass("active")
      .data("filter");
  
  $boxs
    .hide()
    .filter( "." + active )
    .fadeIn(450);

});


