document.addEventListener('DOMContentLoaded', function() {
    new WOW().init();
    
    // Плавный скролл
    const links = document.querySelectorAll('a[href^="#"]');
    
    for (const link of links) {
      link.addEventListener('click', function(e) {
        e.preventDefault();
        
        const targetID = this.getAttribute('href').substring(1);
        const targetElement = document.getElementById(targetID);
        
        if (targetElement) {
          window.scrollTo({
            top: targetElement.offsetTop,
            behavior: 'smooth'
          });
        }
      });
    }
  });
  