(function () {
  const pages = {
    home: { aboutHref: '#testimonial', loginHref: '/login', loginLabel: 'Sign In' },
    prep: { aboutHref: '/#testimonial', loginHref: '/login', loginLabel: 'Sign In' },
    blog: { aboutHref: '/#testimonial', loginHref: '/login', loginLabel: 'Sign In' },
    login: { aboutHref: '/#testimonial', loginHref: '/login', loginLabel: 'Dashboard Login' },
    admin: { aboutHref: '/#testimonial', loginHref: '/login', loginLabel: 'Dashboard Login' },
    legal: { aboutHref: '/#testimonial', loginHref: '/login', loginLabel: 'Sign In' },
    privacy: { aboutHref: '/#testimonial', loginHref: '/login', loginLabel: 'Sign In' },
    fallback: { aboutHref: '/#testimonial', loginHref: '/login', loginLabel: 'Sign In' }
  };

  const page = document.body.dataset.brandPage || 'fallback';
  const config = pages[page] || pages.fallback;
  const headerMount = document.getElementById('cyr-site-header');
  const footerMount = document.getElementById('cyr-site-footer');

  const logo = `
    <a href="/" class="cyr-brand-wordmark" aria-label="ClinicalCaseLog home">
      <span class="cyr-brand-badge" aria-hidden="true">⚕</span>
      <span class="brand-name">ClinicalCaseLog</span>
    </a>`;

  const navLinks = `
    <div class="cyr-products">
      <button class="cyr-products-trigger" type="button" aria-expanded="false">Products</button>
      <div class="cyr-products-menu">
        <a href="https://freecptcodefinder.com">FreeCPTCodeFinder</a>
        <a href="/">ClinicalCaseLog</a>
      </div>
    </div>
    <a href="${config.aboutHref}">About</a>
    <a href="${config.loginHref}">${config.loginLabel}</a>`;

  if (headerMount) {
    headerMount.innerHTML = `
      <header class="cyr-site-header">
        <div class="cyr-site-header__inner">
          ${logo}
          <nav class="cyr-site-nav" aria-label="Primary">
            <div class="cyr-site-nav__group">${navLinks}</div>
          </nav>
          <button class="cyr-mobile-toggle" type="button" aria-label="Open menu" aria-expanded="false">☰</button>
        </div>
        <div class="cyr-mobile-drawer" aria-hidden="true">
          <div class="cyr-mobile-drawer__inner">
            <div class="cyr-mobile-products-label">Products</div>
            <div class="cyr-mobile-products">
              <a href="https://freecptcodefinder.com">FreeCPTCodeFinder</a>
              <a href="/">ClinicalCaseLog</a>
            </div>
            <a href="${config.aboutHref}">About</a>
            <a href="${config.loginHref}">${config.loginLabel}</a>
          </div>
        </div>
      </header>`;

    const toggle = headerMount.querySelector('.cyr-mobile-toggle');
    const drawer = headerMount.querySelector('.cyr-mobile-drawer');
    const productWrap = headerMount.querySelector('.cyr-products');
    const productButton = headerMount.querySelector('.cyr-products-trigger');
    toggle?.addEventListener('click', () => {
      const open = drawer.classList.toggle('open');
      drawer.setAttribute('aria-hidden', String(!open));
      toggle.setAttribute('aria-expanded', String(open));
    });
    productButton?.addEventListener('click', () => {
      const open = productWrap.classList.toggle('open');
      productButton.setAttribute('aria-expanded', String(open));
    });
    document.addEventListener('click', (event) => {
      if (productWrap && !productWrap.contains(event.target)) {
        productWrap.classList.remove('open');
        productButton?.setAttribute('aria-expanded', 'false');
      }
    });
  }

  if (footerMount) {
    footerMount.innerHTML = `
      <footer class="cyr-site-footer">
        <div class="cyr-site-footer__inner">
          <p>© ClinicalCaseLog</p>
          <p class="footer-label">Case logging for surgical trainees and clinical programs</p>
          <p class="footer-label">Products:</p>
          <ul>
            <li>• <a href="https://freecptcodefinder.com">FreeCPTCodeFinder</a></li>
            <li>• <a href="/">ClinicalCaseLog</a></li>
          </ul>
        </div>
      </footer>`;
  }
})();
