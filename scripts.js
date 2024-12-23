// Fetch form data and simulate submission for the contact form
document.getElementById('contact-form').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent the default form submission behavior
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const message = document.getElementById('message').value;

    console.log('Form Submitted', { name, email, message });

    alert(`Thank you for your message, ${name}! We will get back to you soon.`);
    this.reset(); // Reset the form fields
});

// Simulate running a Python script
function runScript() {
    console.log('Running Python script...');
    fetch("/run-authentication")
        .then(response => {
            if (response.ok) {
                console.log('Script executed successfully');
            } else {
                console.error('Error running script');
            }
        })
        .catch(error => console.error('Error:', error));
}
