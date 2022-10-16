import {getShow} from "$lib/api.js"

/** @type {import('./$types').PageLoad} */
export async function load({params}) {
	console.log(params.id)
	return {
		show: await getShow(params.id)
	}
}
