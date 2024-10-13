document.addEventListener('DOMContentLoaded', function () {
    
   
    const selectElement = document.getElementById('sort');
    if (selectElement) {
        selectElement.addEventListener('change', function () {
            const selectedValue = this.value;
            sortProducts(selectedValue);
        });

        function sortProducts(criteria) {
            const productsContainer = document.getElementById('products-container'); // Make sure you have this element to hold the products
            const products = Array.from(productsContainer.getElementsByClassName('product-item')); // Assuming each product has a class 'product-item'

            let sortedProducts;
            switch (criteria) {
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
    }
       // Language selection functionality
       var languageLinks = document.querySelectorAll('.languages a[data-lang-code]');
       languageLinks.forEach(function(link) {
           link.addEventListener('click', function(event) {
               event.preventDefault();
               var langCode = this.getAttribute('data-lang-code');
               var currentUrl = window.location.pathname;
               var newUrl = '/' + langCode + currentUrl.substring(3); // Skip the current language code in the URL
               window.location.href = newUrl;
           });
       });
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
    function toggleSidebar() {
        const menu = document.querySelector('.sidebar-menu');
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
  

function filterByShop() {
    const selectElement = document.getElementById('filter');
    const selectedValue = selectElement.value;
    const productsContainer = document.getElementById('products-container'); 
    const products = Array.from(productsContainer.getElementsByClassName('product-item'));
    const oneShopPro = document.getElementById('one-shop-pro');
    const allShopPro=document.getElementById('all-pro');
    let anyProductVisible = false;
       products.forEach(product => {
        const productShopName = product.dataset.shopname;
        let isVisible = true;
        if (selectedValue !== 'all') {
            isVisible = productShopName === selectedValue;
        }
        product.style.display = isVisible ? '' : 'none';
        if (isVisible) {
            anyProductVisible = true;
        }
    });
    if (anyProductVisible && oneShopPro !== null) {
        
        oneShopPro.innerHTML = "Products from " + selectedValue;
    }

    else if (anyProductVisible && allShopPro !== null) {
        allShopPro.innerHTML =  "Products from " + selectedValue;

    }
    else if (!anyProductVisible && oneShopPro !== null) {
        oneShopPro.innerHTML =  selectedValue + " have no product Yet";

    }
  
    else if (!anyProductVisible && allShopPro !== null) {
        allShopPro.innerHTML =  selectedValue + " have no product Yet";

    }

    
}

