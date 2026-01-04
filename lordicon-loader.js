/**
 * Lordicon Animated Icons Loader for Stenox Docs
 *
 * This script loads the Lordicon player and provides enhanced
 * animation controls for documentation pages.
 */

(function() {
  // Check if Lordicon is already loaded
  if (window.lordicon) return;

  // Create and inject the Lordicon script
  const script = document.createElement('script');
  script.src = 'https://cdn.lordicon.com/lordicon.js';
  script.async = true;

  script.onload = function() {
    // Initialize all lord-icon elements with enhanced behavior
    initializeLordicons();

    // Re-initialize on route changes (for SPA navigation)
    observeRouteChanges();
  };

  document.head.appendChild(script);

  function initializeLordicons() {
    const icons = document.querySelectorAll('lord-icon');
    icons.forEach(icon => {
      // Add smooth entrance animation
      icon.style.opacity = '0';
      icon.style.transform = 'translateY(8px)';
      icon.style.transition = 'opacity 0.4s ease, transform 0.4s ease';

      // Stagger the entrance
      setTimeout(() => {
        icon.style.opacity = '1';
        icon.style.transform = 'translateY(0)';
      }, 100);
    });
  }

  function observeRouteChanges() {
    // Watch for DOM changes (Mintlify uses client-side routing)
    const observer = new MutationObserver((mutations) => {
      mutations.forEach((mutation) => {
        if (mutation.addedNodes.length) {
          mutation.addedNodes.forEach((node) => {
            if (node.nodeType === 1) {
              const icons = node.querySelectorAll ? node.querySelectorAll('lord-icon') : [];
              if (icons.length || node.tagName === 'LORD-ICON') {
                setTimeout(initializeLordicons, 50);
              }
            }
          });
        }
      });
    });

    observer.observe(document.body, {
      childList: true,
      subtree: true
    });
  }
})();
