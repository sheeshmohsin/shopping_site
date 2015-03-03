$(document).ready(function() {
	$('#lightSlider').lightSlider({
		gallery:true,
		minSlide:1,
		maxSlide:1,
		auto:true     
	});  
});
$(document).ready(function(){
  $('#myCarousel').carousel();
});
$('#myCarousel').carousel({
  interval: 4000
});
$('.carousel .aitem').each(function(){
  var next = $(this).next();
  if (!next.length) {
    next = $(this).siblings(':first');
  }
  next.children(':first-child').clone().appendTo($(this));
  
  for (var i=0;i<2;i++) {
    next=next.next();
    if (!next.length) {
      next = $(this).siblings(':first');
    }
    
    next.children(':first-child').clone().appendTo($(this));
  }
});
