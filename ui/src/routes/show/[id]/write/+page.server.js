import {postReview} from "$lib/api.js"

export function load({params}) {
	return {
		id: params.id
	}
}

/** @type {import('./$types').Actions} */
export const actions = {
  default: async (event) => {
		let data = await event.request.formData()
		let author = data.get("author")
		let review = data.get("review")
		let score = 5
		postReview(event.params.id, author, review, score)
  }
};
