$('.message a').click(function(){
    $('form').animate({height:"toggle", opacity:"toggle"},"slow");
    });

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


// www.reddit.com/r/django/comments/4f7v1n/how_do_i_include_javascript_in_my_django_project/