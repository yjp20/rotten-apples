/**
 * @typedef {Object} Review
 * @property {string} review
 * @property {string} author
 * @property {number} rating
 */

/**
 * @typedef {Object} Show
 * @property {number} id
 * @property {string} name
 * @property {string} img
 * @property {number} members
 * @property {number} ranked
 * @property {number} star
 * @property {Review[]} reviews
 */

/** @type {Show[]} */
const shows = [{
	id: 1,
	name: "Full Metal Alchemist: Brotherhood",
	img: "https://cdn.myanimelist.net/images/anime/1223/96541.jpg",
	desc: `<p>After a horrific alchemy experiment goes wrong in the Elric household, brothers Edward and Alphonse are left in a catastrophic new reality. Ignoring the alchemical principle banning human transmutation, the boys attempted to bring their recently deceased mother back to life. Instead, they suffered brutal personal loss: Alphonse's body disintegrated while Edward lost a leg and then sacrificed an arm to keep Alphonse's soul in the physical realm by binding it to a hulking suit of armor.<p>The brothers are rescued by their neighbor Pinako Rockbell and her granddaughter Winry. Known as a bio-mechanical engineering prodigy, Winry creates prosthetic limbs for Edward by utilizing "automail," a tough, versatile metal used in robots and combat armor. After years of training, the Elric brothers set off on a quest to restore their bodies by locating the Philosopher's Stone—a powerful gem that allows an alchemist to defy the traditional laws of Equivalent Exchange.<p>As Edward becomes an infamous alchemist and gains the nickname "Fullmetal," the boys' journey embroils them in a growing conspiracy that threatens the fate of the world.`,
	members: 3001460,
	ranked: 1,
	reviews: [
		{ review: "First of all, I have seen the original FMA and although it was very popular and original, the pacing and conclusion did not sit too well with me. Brotherhood is meant to be a remake of the original, this time sticking to the manga all the way through, but there were people who thought it would spoil the franchise. That myth should be dispelled, as there's only one word to describe this series - EPIC.", author: "tazillo", rating: 10 },
	]
}]

export async function getShows() {
	return shows
}

export async function getShow(id) {
	return shows.find((show) => show.id == id)
}
