

document.getElementById('profileImageForm').addEventListener('submit', function (event) {
    // Get form fields
    var firstName = document.getElementById('id_first_name');
    var lastName = document.getElementById('id_last_name');
    var email = document.getElementById('id_email');
    var bio = document.getElementById('id_bio');
    var image = document.getElementById('id_image');
    
    // Initialize error variables
    var hasError = false;

    // Clear previous errors
    document.getElementById('first-name-error').innerHTML = '';
    document.getElementById('last-name-error').innerHTML = '';
    document.getElementById('email-error').innerHTML = '';
    document.getElementById('bio-error').innerHTML = '';
    document.getElementById('image-error').innerHTML = '';

    // Validate first name
    if (firstName.value.trim() === '' || firstName.value.length < 2) {
        document.getElementById('first-name-error').innerHTML = 'First Name must be at least 2 characters long.';
        hasError = true;
    }

    // Validate last name
    if (lastName.value.trim() === '' || lastName.value.length < 2) {
        document.getElementById('last-name-error').innerHTML = 'Last Name must be at least 2 characters long.';
        hasError = true;
    }

    var emailPattern = /^$|^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    if (!emailPattern.test(email.value)) {
        document.getElementById('email-error').innerHTML = 'Please enter a valid email address.';
        hasError = true;
    }

    // Validate bio (minimum length of 10 characters)
    if (bio.value.trim() === '' || bio.value.length < 10) {
        document.getElementById('bio-error').innerHTML = 'Biography must be at least 10 characters long.';
        hasError = true;
    }

    // If there are errors, prevent the form from submitting
    if (hasError) {
        event.preventDefault();
    }
});
