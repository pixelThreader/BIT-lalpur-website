// Create disabled Tippy instances when the page loads
document.querySelectorAll('.msg').forEach(button => {
    button._tippy = tippy(button, {
        content: 'Tooltip content',
        animation: (button.dataset.tippyAnimation == null) ? 'scale' : button.dataset.tippyAnimation,
        inertia: true,
        theme: 'light',
        enabled: false,
        hideOnClick: false  // Tooltip will not hide on click
    });
});

// Enable the Tippy instances on hover
document.querySelectorAll('.msg').forEach(button => {
    button.addEventListener('mouseenter', function () {
        this._tippy.enable();
    });
});

function changeTippy(selector, newContent) {
    // Get the DOM element from the selector
    let elem = document.querySelector(selector);
    // Check if the element has a Tippy instance
    if (elem && elem._tippy) {
        // Change the tooltip content
        elem._tippy.setContent(newContent);
    }
}
