import adapter from '@sveltejs/adapter-auto';
import { optimizeImports } from 'carbon-preprocess-svelte';
import preprocess from 'svelte-preprocess';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	// Consult https://github.com/sveltejs/svelte-preprocess
	// for more information about preprocessors
	preprocess: [
		preprocess(),
		optimizeImports()
	],

	kit: {
		adapter: adapter(),
		alias: {
			"src": "./src",
			"/src": "./src",
			"$components": "./src/components"
		}
		// prerender: {
		// 	enabled: false
		// }
	},

};

export default config;
