document.addEventListener('DOMContentLoaded', function () {
 
    const relatedImages = document.querySelectorAll('.related-image');
    const mainImage = document.getElementById('mainImage');
    const prevButton = document.querySelector('.previmg');
    const nextButton = document.querySelector('.nextimg');
   
    let currentImageIndex = 0;
   
    function updateMainImage(index) {
        //add css styling
        relatedImages.forEach(img => img.classList.remove('active'));
        currentImageIndex = index; 
        mainImage.src = relatedImages[currentImageIndex].src; // Change the main image
        //add active class currently displayed image
        relatedImages[currentImageIndex].classList.add('active')
    }
   
    function nextSlide() {
        currentImageIndex = (currentImageIndex + 1) % relatedImages.length; // Loop to the next image
        updateMainImage(currentImageIndex);
    }
   
    // Function for the previous button
    function prevSlide() {
        currentImageIndex = (currentImageIndex - 1 + relatedImages.length) % relatedImages.length; // Loop to the previous image
        updateMainImage(currentImageIndex);
    }
   
    // Initially set the main image to the first image
    updateMainImage(0);
   
    // Add event listeners for buttons
    prevButton.addEventListener('click', prevSlide);
    nextButton.addEventListener('click', nextSlide);

    // for each image add event listner
    
    relatedImages.forEach((image,index) => {
        image.addEventListener('click', function () {
            updateMainImage(index)
        })
    })
    
   });
   