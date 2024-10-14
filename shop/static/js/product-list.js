// Wait until the document is fully loaded
document.addEventListener('DOMContentLoaded', function() {
  let slides = document.querySelectorAll('.slide');
  let currentIndex = 0;
  const slideInterval = 8000; // Time interval between slides (milliseconds)
  let interval;
  let isTransitioning = false;

  // Function to show the next slide
  function nextSlide() {
    if (isTransitioning) return;
    isTransitioning = true;

    currentIndex++;
    if (currentIndex === slides.length) {
      // When reaching the last slide, transition back to the first slide
      setTimeout(function() {
        const logoImageSlider = document.querySelector('.logo-image-slider');
        logoImageSlider.style.transition = 'none'; // Disable transition momentarily
        currentIndex = 0; // Jump back to the first slide
        updateSlidePosition();

        // Re-enable the transition after the position has been reset
        setTimeout(function() {
          logoImageSlider.style.transition = 'transform 4s ease-in-out'; // Smooth transition back
          isTransitioning = false;
        }, 50);
      }, 1000);
    } else {
      updateSlidePosition();
      setTimeout(() => isTransitioning = false, 1000); // Reset after transition
    }
  }

  // Function to show the previous slide
  function prevSlide() {
    if (isTransitioning) return;
    isTransitioning = true;

    currentIndex = (currentIndex - 1 + slides.length) % slides.length;
    updateSlidePosition();
    setTimeout(() => isTransitioning = false, 1000); // Reset after transition
  }

  // Function to update the slide position based on currentIndex
  function updateSlidePosition() {
    const logoImageSlider = document.querySelector('.logo-image-slider');
    const offset = -currentIndex * 100; // Each slide takes 100% of the container width
    logoImageSlider.style.transform = `translateX(${offset}%)`;
  }

  // Automatically change to the next slide
  function startAutoSlide() {
    interval = setInterval(nextSlide, slideInterval);
  }

  // Stop automatic slide when the user clicks the buttons
  function stopAutoSlide() {
    clearInterval(interval);
  }

  // Set up the initial automatic slide
  startAutoSlide();

  // Add event listeners to stop the auto-slide when a user clicks on buttons
  document.querySelector('.prev').addEventListener('click', function() {
    stopAutoSlide();
    prevSlide();
    startAutoSlide();
  });

  document.querySelector('.next').addEventListener('click', function() {
    stopAutoSlide();
    nextSlide();
    startAutoSlide();
  });
});
