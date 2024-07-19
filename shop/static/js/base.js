document.addEventListener('DOMContentLoaded', function() {
    const selectElement = document.getElementById('sort');

    selectElement.addEventListener('change', function() {
        const selectedValue = this.value;
        sortProducts(selectedValue);
    });

    function sortProducts(criteria) {
        const productsContainer = document.getElementById('products-container'); // Make sure you have this element to hold the products
        const products = Array.from(productsContainer.getElementsByClassName('product-item')); // Assuming each product has a class 'product-item'

        let sortedProducts;
        switch(criteria) {
            case 'recommended':
                sortedProducts = products; 
                break;
            case 'newest':
                sortedProducts = products.sort((a, b) => new Date(b.dataset.date) - new Date(a.dataset.date));
                break;
            case 'priceLowHigh':
                sortedProducts = products.sort((a, b) => parseFloat(a.dataset.price) - parseFloat(b.dataset.price));
                break;
            case 'priceHighLow':
                sortedProducts = products.sort((a, b) => parseFloat(b.dataset.price) - parseFloat(a.dataset.price));
                break;
            case 'nameAZ':
                sortedProducts = products.sort((a, b) => a.dataset.name.localeCompare(b.dataset.name));
                break;
            case 'nameZA':
                sortedProducts = products.sort((a, b) => b.dataset.name.localeCompare(a.dataset.name));
                break;
            default:
                sortedProducts = products;
                break;
        }

        // Clear the container and re-append sorted products
        productsContainer.innerHTML = '';
        sortedProducts.forEach(product => productsContainer.appendChild(product));
    }
});


function hoverEffect(element, color) {
    element.style.color = color;
}
  function confirmUpdateProfile() {
    return confirm('Do you want to update your profile?');
    }

    function toggleNavbar() {
      const menu = document.querySelector('.navbar-menu');
      menu.classList.toggle('active');
    }

    function toggleDropdown(event) {
    event.preventDefault();
    const dropdownMenu = document.getElementById('dropdown-menu');
    dropdownMenu.style.display = dropdownMenu.style.display === 'block' ? 'none' : 'block';
}

// Close the dropdown if the user clicks outside of it
    window.onclick = function(event) {
      if (event.target == document.getElementById('profileModal')) {
      closeModal();
       }
        else if (!event.target.matches('#profileImage')) {
            const dropdownMenu = document.getElementById('dropdown-menu');
            if (dropdownMenu.style.display === 'block') {
                dropdownMenu.style.display = 'none';
            }
        }
    };
 function openModal() {
    document.getElementById('profileModal').style.display = 'block';
  }

  function closeModal() {
    document.getElementById('profileModal').style.display = 'none';
  }