<script>
	export let data;

	$: id = data.id;
</script>
<div class="section is-small">
	<div class="container">
		<form method="POST" >
			<h1 class="title"> Write Review </h1>
			<div class="field">
				<label class="label" for="author"> Author </label>
				<input name="author" class="input" placeholder="John Doe" type="text" />
			</div>
			<div class="field">
				<label class="label" for="review"> Review </label>
				<textarea name="review" class="textarea" />
			</div>
			<div class="buttons">
				<a class="button" href="/show/{id}">Cancel</a>
				<button class="button is-primary">Submit</button>
			</div>
		</form>
	</div>
</div>

<style>
</style>
