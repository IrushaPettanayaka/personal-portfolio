(() => {
    const root = document.documentElement;
    const toggle = document.querySelector('[data-theme-toggle]');
    const label = document.querySelector('[data-theme-label]');
    const themeColor = document.querySelector('meta[name="theme-color"]');
    if (!toggle || !label) return;

    function applyTheme(theme, persist = true) {
        const normalized = theme === 'light' ? 'light' : 'dark';
        const next = normalized === 'dark' ? 'light' : 'dark';
        root.dataset.theme = normalized;
        label.textContent = normalized === 'dark' ? 'Dark' : 'Light';
        toggle.setAttribute('aria-pressed', String(normalized === 'light'));
        toggle.setAttribute('aria-label', `Switch to ${next} theme`);
        if (themeColor) {
            themeColor.setAttribute('content', normalized === 'dark' ? '#0C0D0F' : '#F2EFE8');
        }
        if (persist) {
            try {
                localStorage.setItem('portfolio-theme', normalized);
            } catch (error) {
                // The selected theme still applies for the current page.
            }
        }
    }

    applyTheme(root.dataset.theme, false);
    toggle.hidden = false;
    toggle.addEventListener('click', () => {
        applyTheme(root.dataset.theme === 'dark' ? 'light' : 'dark');
    });
})();
