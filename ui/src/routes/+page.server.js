import {getShows} from "$lib/api.js"

/** @type {import('./$types').PageLoad} */
export async function load(event) {
  return { shows: await getShows() }
}
