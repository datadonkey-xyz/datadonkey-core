import { sveltekit } from '@sveltejs/kit/vite';
import type { UserConfig } from 'vite';

const config: UserConfig = {
	plugins: [sveltekit()],
	ssr: {
		noExternal: ['@carbon/charts', 'carbon-components'],
	},
	resolve: {
		alias: {
			"src": "./src",
			"/src": "./src",
			"$lib": "./src/lib",
		}
	}
};

export default config;
