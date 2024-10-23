document.getElementById('orderForm').addEventListener('submit', function(event) {
    let hasError = false;
    
    // Clear any previous errors
    document.querySelectorAll('.text-danger').forEach(el => el.innerHTML = '');

    // Validate First Name
    const firstName = document.getElementById('id_first_name');
    if (!firstName.value.trim() || firstName.value.length < 2) {
        document.getElementById('first-name-error').innerHTML = 'First Name must be at least 2 characters long.';
        hasError = true;
    }

    // Validate Last Name
    const lastName = document.getElementById('id_last_name');
    if (!lastName.value.trim() || lastName.value.length < 2) {
        document.getElementById('last-name-error').innerHTML = 'Last Name must be at least 2 characters long.';
        hasError = true;
    }

    // Validate Email
    const email = document.getElementById('id_email');
    var emailPattern = /^$|^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    if (!emailPattern.test(email.value.trim())) {
        document.getElementById('email-error').innerHTML = 'Please enter a valid email address.';
        hasError = true;
    }

    // Validate Phone Number (Example for Ethiopian numbers)
    const phoneNumber = document.getElementById('id_phone_number');
    const phoneRegex = /^(\+251|0)?[1-9]\d{8}$/;
    if (!phoneRegex.test(phoneNumber.value.trim())) {
        document.getElementById('phone-error').innerHTML = 'Please enter a valid Ethiopian phone number.';
        hasError = true;
    }

    // Validate Address
    const address = document.getElementById('id_address');
    if (!address.value.trim()) {
        document.getElementById('address-error').innerHTML = 'Address is required.';
        hasError = true;
    }

    // Validate City
    const city = document.getElementById('id_city');
    if (!city.value.trim()) {
        document.getElementById('city-error').innerHTML = 'City is required.';
        hasError = true;
    }

    // Validate Delivery Date
    const deliveryDate = document.getElementById('id_delivery_date');
    const today = new Date().toISOString().split('T')[0];
    if (deliveryDate.value < today) {
        document.getElementById('date-error').innerHTML = 'Delivery date cannot be in the past.';
        hasError = true;
    }

    // Prevent form submission if there's an error
    if (hasError) {
        event.preventDefault();
    }
})