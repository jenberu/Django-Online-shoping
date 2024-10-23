document.getElementById('shopForm').addEventListener('submit', function(event) {
    event.preventDefault();

    document.getElementById('shop-name-error').innerHTML = '';
    document.getElementById('address-error').innerHTML = '';
    document.getElementById('contact-number-error').innerHTML = '';

    // Get form values
    var shopName = document.querySelector('input[name="shopName"]').value.trim();
    var address = document.querySelector('input[name="address"]').value.trim();
    var contactNumber = document.querySelector('input[name="contact_number"]').value.trim();

    // Initialize a variable to track errors
    var hasError = false;

    // Validate shop name
    if (shopName === '' || shopName.length < 2) {
        document.getElementById('shop-name-error').innerHTML = 'Business Name must be at least 2 characters long.';
        hasError = true;
    }

    // Validate address
    if (address === '' || address.length < 5) {
        document.getElementById('address-error').innerHTML = 'Address must be at least 5 characters long.';
        hasError = true;
    }

    // Validate contact number (simple validation for format, you may want to enhance this)
    var phonePattern = /^[0-9]{10}$/; 
    if (!phonePattern.test(contactNumber)) {
        document.getElementById('contact-number-error').innerHTML ='Please enter a valid phone number.';
        hasError = true;
    }

    // If there are no errors, submit the form
    if (!hasError) {
        this.submit();
        // Only submit the form if no errors are present
    }
});
