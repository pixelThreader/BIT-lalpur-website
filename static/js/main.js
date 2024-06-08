// Function to change the logo based on the theme
function changelogo(theme) {
    var logoSrc = theme === 'dark' ?
        "/static/assets/brand/bit_logo.png" :
        "/static/assets/brand/bit_logo_light.png";
    $('#bit_header_logo').attr('src', logoSrc);
}

    // Function to update the toggle button based on the theme
    function updateToggleButton(theme) {
        $('#toggle-theme').attr('title', theme === 'light' ? 'Dark' : 'Light');
        $('#toggle-theme ion-icon').attr('name', theme === 'light' ? 'moon' : 'sunny');
    }

// Function to set the theme for the session
function setThemeForSession(theme) {
    sessionStorage.setItem('theme', theme);
    $('body').attr('data-bs-theme', theme);
    changelogo(theme);
    updateToggleButton(theme);
}
$(document).ready(function () {

    // Check if a theme is already set for the session
    var storedTheme = sessionStorage.getItem('theme');
    if (storedTheme) {
        // If theme is already set, apply it
        setThemeForSession(storedTheme);
    } else {
        // If theme is not set, default to 'light'
        setThemeForSession('light');
    }

    // Event listener for theme toggle button
    $('#toggle-theme').click(function () {
        var body = $('body');
        var currentTheme = body.attr('data-bs-theme');
        var newTheme = currentTheme === 'light' ? 'dark' : 'light';
        body.attr('data-bs-theme', newTheme);
        // Set the new theme for the session
        setThemeForSession(newTheme);
    });
});
