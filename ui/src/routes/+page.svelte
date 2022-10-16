<script>
	/** @type {import('./$types').PageData} */
	export let data
</script>

<div class="section is-small">
	<div class="container">
		<h1 class="title is-family-secondary"> Shows </h1>
		<div class="columns is-multiline">
			{#each data.shows as show}
				<div class="column is-6">
					<a class="card show" href="show/{show.id}">
						<div class="card-image">
							<figure class="image is-2by3 show-image">
								<img src={show.img || "https://bulma.io/images/placeholders/1280x960.png"} alt="Placeholder image">
							</figure>
						</div>
						<div class="card-content">
							<h3 class="subtitle has-text-weight-bold"> {show.name} </h3>
							<p class="paragraph show-info">
								<span><i class="fa-solid fa-ranking-star"></i> #{show.ranked}</span>
								<span class="has-text-info"><i class="fa-solid fa-star"></i> 8.6</span>
								<span class="has-text-danger"><i class="fa-solid fa-user"></i> {(new Intl.NumberFormat()).format(show.members)}</span>
							</p>
						</div>
					</a>
				</div>
			{/each}
		</div>
	</div>
</div>

<style>
	.show {
		display: flex;
	}

	.show-image {
		width: 120px;
	}

	.show-image > img {
		object-fit: cover;
	}

	.show-info > span + span {
		margin-left: 12px;
	}
</style>
