
document.addEventListener('DOMContentLoaded', function () {
    // Get references to the buttons by their IDs
    const understandButton = document.getElementById('understand-button');
    const notYetButton = document.getElementById('not-yet-button');

    // Add click event listeners to the buttons
    understandButton.addEventListener('click', () => {
        // Change the color of the button when clicked
        understandButton.style.backgroundColor = 'green';
    });

    notYetButton.addEventListener('click', () => {
        // Change the color of the button when clicked
        notYetButton.style.backgroundColor = 'red';
    });
});