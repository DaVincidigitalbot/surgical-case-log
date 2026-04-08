// Service Worker for CYRIONYX | ClinicalCaseLog PWA
const CACHE_NAME = 'caselog-v4';
const ASSETS_TO_CACHE = [
  '/',
  '/index.html',
  '/icon-192.png',
  '/icon-512.png',
  '/manifest.json'
];

// Install - cache core assets
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => {
      return cache.addAll(ASSETS_TO_CACHE);
    })
  );
  self.skipWaiting();
});

// Activate - clean old caches
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys => {
      return Promise.all(
        keys.filter(key => key !== CACHE_NAME).map(key => caches.delete(key))
      );
    })
  );
  self.clients.claim();
});

// Fetch - network first, fallback to cache
self.addEventListener('fetch', event => {
  // Skip API calls, app pages, and auth pages - always go to network
  const url = event.request.url;
  if (url.includes('/api/') || url.includes('/demo') || url.includes('/login') || url.includes('/signin') || url.includes('/register') || url.includes('/admin') || url.includes('/prep')) {
    return event.respondWith(fetch(event.request));
  }
  
  event.respondWith(
    fetch(event.request)
      .then(response => {
        // Cache successful responses
        if (response.status === 200) {
          const clone = response.clone();
          caches.open(CACHE_NAME).then(cache => cache.put(event.request, clone));
        }
        return response;
      })
      .catch(() => {
        // Offline - serve from cache
        return caches.match(event.request).then(cached => {
          return cached || caches.match('/');
        });
      })
  );
});
