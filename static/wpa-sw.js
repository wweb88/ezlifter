/* Asignar nombre y versión de la caché */

const CACHE_NAME = 'v1_cache_ezlifter_pwa';

/* Ficheros a cachear en la aplicación */
var urlsToCache = [
	'./',
];

/*
Evento install
Instalación del service worker y guardar en cache los recursos estaticos
*/
self.addEventListener('install', e => {
	e.waitUntil(
		caches.open(CACHE_NAME)
			.then(cache => {
				return cache.addAll(urlsToCache)
					.then(() => {
						self.skipWaiting();
					});
			})
		.catch(err => console.log('No se ha registrado el cache', err))
	);
});

/*
Evento activate
Que la app funcione sin conexiÃ³n
*/
self.addEventListener('activate', e => {
	const cacheWhitelist = [CACHE_NAME];
	e.waitUntil(
		caches.keys()
			.then(cacheNames => {
				return Promise.all(
					cacheNames.map(cacheName => {
						if(cacheWhitelist.indexOf(cacheName) === -1){
							/* Borrar elementos que no se necesitan */
							return caches.delete(cacheName);
						}
					})
				);
			})
		.then(() => {
			/* Activar cache */
			self.clients.claim();
		})
	);
});

/*
Evento fetch
*/
self.addEventListener('fetch', e => {
	e.respondWith(
		caches.match(e.request)
			.then(res => {
				if(res){
					/* devuelvo datos desde cache */
					return res;
				}
				return fetch(e.request);
			})
	)
});