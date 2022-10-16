<script>
	/** @type {import('./$types').PageData} */
	export let data;

	let show = data.show;
	console.log(data.show);
</script>

<div class="section is-small">
	<div class="container">
		<h3 class="title has-text-weight-bold"> {show.name} </h3>
		<div class="columns">
			<div class="column is-3 content">
				<p class="image is-2by3 show-image">
						<img src={show.img || "https://bulma.io/images/placeholders/1280x960.png"} alt="Placeholder image">
				</p>
				<p class="show-info">
					<span><i class="fa-solid fa-ranking-star"></i> #{show.ranked}</span>
					<span class="has-text-info"><i class="fa-solid fa-star"></i> 8.6</span>
					<span class="has-text-danger"><i class="fa-solid fa-user"></i> {(new Intl.NumberFormat()).format(show.members)}</span>
				</p>
			</div>
			<div class="column show-desc">
				<div class="content">
					<h3 class="subtitle">Synopsis</h3>
					<p> {@html show.desc} </p>
					<h3 class="subtitle">Reviews</h3>
					{#each show.reviews as review}
						<div class="box review">
							<div class="review-author"><b>{review.author}</b></div>
							<div class="review-desc">{review.review}</div>
						</div>
					{/each}
				</div>
			</div>
		</div>
	</div>
</div>

<style>
	.show-header {
		display: flex;
		align-items: flex-end;
	}


	.show-image {
	}

	.show-image > img {
		border-radius: 5px;
		object-fit: cover;
	}

	.show-info > span + span {
		margin-left: 12px;
	}
</style>

