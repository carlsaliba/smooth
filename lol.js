$('.navbar a').on('click', function (e) {
 
    if (this.hash !== '') {
      e.preventDefault();
     
      const hash = this.hash;
      console.log("bati2");
      console.log($(hash).offset().top);
      $('html, body')
      
       .animate({
          scrollTop: $(hash).offset().top
           },2600);
    } 
    
 });

 window.addEventListener("load", event => {
  
    var image = document.querySelector('#about');
    console.log(image);
    //var load = image.complete;
    alert("ejit l about");
  
  
  });

 


$('.navbar a').on('click', function (e) {
    
    console.log(this.hash);
 
});






