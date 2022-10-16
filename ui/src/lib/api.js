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
 * @property {string} desc
 * @property {string} img
 * @property {number} members
 * @property {number} ranked
 * @property {number} rating
 * @property {Review[]} reviews
 */

import db from "$lib/db.js"

/** @type {Show} */
const show = {
	id: 1,
	name: "Full Metal Alchemist: Brotherhood",
	img: "https://cdn.myanimelist.net/images/anime/1223/96541.jpg",
	desc: `After a horrific alchemy experiment goes wrong in the Elric household, brothers Edward and Alphonse are left in a catastrophic new reality. Ignoring the alchemical principle banning human transmutation, the boys attempted to bring their recently deceased mother back to life. Instead, they suffered brutal personal loss: Alphonse's body disintegrated while Edward lost a leg and then sacrificed an arm to keep Alphonse's soul in the physical realm by binding it to a hulking suit of armor.
	The brothers are rescued by their neighbor Pinako Rockbell and her granddaughter Winry. Known as a bio-mechanical engineering prodigy, Winry creates prosthetic limbs for Edward by utilizing "automail," a tough, versatile metal used in robots and combat armor. After years of training, the Elric brothers set off on a quest to restore their bodies by locating the Philosopher's Stone—a powerful gem that allows an alchemist to defy the traditional laws of Equivalent Exchange.
	As Edward becomes an infamous alchemist and gains the nickname "Fullmetal," the boys' journey embroils them in a growing conspiracy that threatens the fate of the world.`,
	members: 3001460,
	ranked: 1,
}

/** @type {Review} */
const review = {
	review:
		"First of all, I have seen the original FMA and although it was very popular and original, the pacing and conclusion did not sit too well with me. Brotherhood is meant to be a remake of the original, this time sticking to the manga all the way through, but there were people who thought it would spoil the franchise. That myth should be dispelled, as there's only one word to describe this series - EPIC.",
	author: "tazillo",
	rating: 10,
}

function initialize() {
	db.serialize(() => {
		db.run("CREATE TABLE IF NOT EXISTS shows (id INTEGER PRIMARY KEY, name TEXT, desc TEXT, img TEXT, members INT, ranked REAL, rating REAL)")
		db.run("CREATE TABLE IF NOT EXISTS reviews (id INTEGER PRIMARY KEY, show_id INT, review TEXT, author TEXT, rating INT, old INT)")
		// db.run("INSERT INTO shows (name, desc, img, members, ranked, rating) VALUES (?, ?, ?, ?, ?, ?)", [show.name, show.desc, show.img, show.members, show.ranked, show.rating])
		// db.run("INSERT INTO reviews (show_id, review, author, rating, old) VALUES (?, ?, ?, ?, ?)", [1, review.review, review.author, review.rating, 10])
	})
}

export const ok = initialize()

export function getShows() {
	return new Promise((resolve, reject) => {
		db.all("SELECT * FROM shows", [], (err, rows) => {
			if (err) reject(err)
			resolve(rows)
		})
	})
}

export function getShow(id) {
	return new Promise((resolve, reject) => {
		db.get("SELECT * FROM shows", [], (err, row) => {
			if (err) reject(err)
			resolve(row)
		})
	})
}

export function getReviews(id) {
	return new Promise((resolve, reject) => {
		db.all(
			"SELECT reviews.id as id, reviews.review as review, reviews.author as author, reviews.rating as rating, reviews.old as old  FROM shows JOIN reviews ON reviews.show_id=shows.id WHERE shows.id=?",
			[id],
			(err, rows) => {
				if (err) reject(err)
				resolve(rows)
			}
		)
	})
}

export function postReview(id, author, review, rating) {
	return new Promise((resolve, reject) => {
		db.run("INSERT INTO reviews (author, review, rating, show_id) VALUES (?, ?, ?, ?)", [author, review, rating, id], (err, rows) => {
			if (err) reject(err)
			resolve(rows)
		})
	})
}
