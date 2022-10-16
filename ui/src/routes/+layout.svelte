<div class="container">
	<nav class="navbar" aria-label="main navigation">
		<div class="navbar-brand">
			<a class="navbar-item is-family-secondary" href="/">
				Rotten Apples
			</a>

			<a
				role="button"
				class="navbar-burger"
				aria-label="menu"
				aria-expanded="false"
				data-target="navbar"
			>
				<span aria-hidden="true" />
				<span aria-hidden="true" />
				<span aria-hidden="true" />
			</a>
		</div>

		<div id="navbar" class="navbar-menu">
			<div class="navbar-start">
				<a class="navbar-item" href="/"> Home </a>
			</div>
		</div>
		<div class="navbar-end">
			<div class="navbar-item">
				<input class="input" type="text" placeholder="Text input">
				<button class="button is-primary">Search</button>
			</div>
		</div>
	</nav>
</div>

<main>
	<slot />
</main>

<style>
	main {
		background: linear-gradient(#0e61a411 0px, #0e61a400 400px);
	}
</style>
