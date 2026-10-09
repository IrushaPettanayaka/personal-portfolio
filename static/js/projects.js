// All projects are rendered by Flask. JavaScript only narrows the visible list.
(() => {
    const controls = document.querySelector('.project-filters');
    const archive = document.getElementById('project-archive');
    const count = document.getElementById('project-count');
    if (!controls || !archive || !count) return;

    const buttons = [...controls.querySelectorAll('button[data-filter]')];
    const projects = [...archive.querySelectorAll('[data-category]')];
    const groups = [...archive.querySelectorAll('[data-project-group]')];
    const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
    let requestedFilter = 'all';
    let filterTimer;
    let revealFrame;

    function filterProjects(category) {
        let visibleCount = 0;
        projects.forEach(project => {
            const visible = category === 'all' || project.dataset.category === category;
            project.hidden = !visible;
            if (visible) visibleCount += 1;
        });
        groups.forEach(group => {
            group.hidden = ![...group.querySelectorAll('[data-category]')]
                .some(project => !project.hidden);
        });
        buttons.forEach(button => {
            button.setAttribute('aria-pressed', String(button.dataset.filter === category));
        });
        count.textContent = visibleCount;
    }

    function requestFilter(category) {
        if (category === requestedFilter) return;
        requestedFilter = category;
        clearTimeout(filterTimer);
        cancelAnimationFrame(revealFrame);

        if (reducedMotion.matches) {
            archive.classList.remove('is-filtering');
            filterProjects(category);
            return;
        }

        archive.classList.add('is-filtering');
        filterTimer = setTimeout(() => {
            filterProjects(requestedFilter);
            revealFrame = requestAnimationFrame(() => {
                archive.classList.remove('is-filtering');
            });
        }, 160);
    }

    buttons.forEach(button => {
        // Native buttons support Tab, Enter, and Space without custom key handlers.
        button.addEventListener('click', () => requestFilter(button.dataset.filter));
    });
    filterProjects('all');
    controls.hidden = false;
})();
