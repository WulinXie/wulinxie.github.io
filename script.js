(() => {
  const status = document.getElementById('filter-status');
  function updateCount() {
    const count = document.querySelectorAll('.paper:not([hidden])').length;
    status.textContent = `Showing ${count} publications`;
  }
  updateCount();
  document.querySelectorAll('[data-filter]').forEach(button => {
    button.addEventListener('click', () => {
      const filter = button.dataset.filter;
      document.querySelectorAll('[data-filter]').forEach(other => {
        other.classList.toggle('active', other === button);
        other.setAttribute('aria-pressed', String(other === button));
      });
      document.querySelectorAll('.paper').forEach(paper => {
        paper.hidden = filter !== 'all' && !paper.dataset.tags.split(' ').includes(filter);
      });
      updateCount();
    });
  });
  const sections = [...document.querySelectorAll('main section[id]')];
  const navLinks = [...document.querySelectorAll('.section-nav a')];
  let scheduled = false;
  function updateNavigation() {
    const active = sections.filter(section => section.getBoundingClientRect().top < 180).at(-1) || sections[0];
    navLinks.forEach(link => {
      const isActive = link.hash === '#' + active.id;
      link.classList.toggle('active', isActive);
      if (isActive) link.setAttribute('aria-current', 'location'); else link.removeAttribute('aria-current');
    });
    document.getElementById('back-top').classList.toggle('visible', window.scrollY > 400);
    scheduled = false;
  }
  window.addEventListener('scroll', () => {
    if (!scheduled) { scheduled = true; requestAnimationFrame(updateNavigation); }
  }, { passive: true });
  updateNavigation();
})();
