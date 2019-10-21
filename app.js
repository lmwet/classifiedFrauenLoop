$('.message a').click(function(){
    $('form').animate({height:"toggle", opacity:"toggle"},"slow");
    });
    // $('#submit-button').on("click" , function(e){
        // e.preventDefault();
    //     const username = $("#username").val();
    //     const whatever = $("#password").val();
    //     $.post( "ajax/test.html", function( data ) {
    //         $( ".result" ).html( data );
    //       });

    // })

    const navDrop = () => {
   
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.nav-links');
    const navLinks = document.querySelectorAll('.nav-links li');
    
    burger.addEventListener('click', () =>{
        nav.classList.toggle('nav-active');
    });

     navLinks.forEach((link,index) =>{
       link.style.animation =`navLinkFade 0.5s ease forwards ${index/7+2}s`;
     });
    }  
    navDrop(); 

