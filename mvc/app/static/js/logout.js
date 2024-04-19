document.addEventListener('DOMContentLoaded', function() {
    // This could be a logout function that clears the session and then redirects or displays the image.
    function logoutUser() {
        // Perform logout operations here
        // For example, clear session storage or local storage if used
        sessionStorage.clear();
        localStorage.removeItem('userLoggedIn');

        // Then you might redirect to the login page or simply display the goodbye image
        window.location.href = '/';
    }

    // Call logout on page load
    logoutUser();
});
