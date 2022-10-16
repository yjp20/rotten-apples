import {getShow, getReviews} from "$lib/api.js"

/** @type {import('./$types').PageLoad} */
export async function load({params}) {
	const show = await getShow(params.id)
	show.reviews = await getReviews(params.id)
	return {show}
}
