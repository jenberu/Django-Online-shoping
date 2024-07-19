function handleAddsButtonClicked(containerId) {
    // Get the ad-container with the specific ID
    const adsContainer = document.getElementById(`ad-container-${containerId}`);
    if (adsContainer) {
        adsContainer.style.visibility = 'hidden';
    }
}

document.addEventListener('DOMContentLoaded', function() {
    const adContainers = document.querySelectorAll('.ad-container');
    adContainers.forEach((container, index) => {
        const ads = container.querySelectorAll('.add-item');
        let currentIndex = 0;

        function showNextAd() {
            ads[currentIndex].classList.remove('active');
            currentIndex = (currentIndex + 1) % ads.length;
            ads[currentIndex].classList.add('active');
        }

        if (ads.length > 0) {
            ads[0].classList.add('active');
            setInterval(showNextAd, 3000); // Change ad every 3 seconds
        }
    });
});