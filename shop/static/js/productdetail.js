document.addEventListener('DOMContentLoaded', function () {
 
    // Get all related images and the main image
    const relatedImages = document.querySelectorAll('.related-image');
    const mainImage = document.getElementById('mainImage');
    const prevButton = document.querySelector('.previmg');
    const nextButton = document.querySelector('.nextimg');
   
    // Variable to track the current index of the displayed image
    let currentImageIndex = 0;
   
    // Function to update the main image
    function updateMainImage(index) {
        currentImageIndex = index; // Update the current index
        mainImage.src = relatedImages[currentImageIndex].src; // Change the main image
    }
   
    // Function for the next button
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
    
   });
   