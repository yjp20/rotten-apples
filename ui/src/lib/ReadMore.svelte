<script>
	/** @type {String} */
	export let text
	export let cutoff = 250
	export let active = false

	$: first = text.slice(0, cutoff)
	$: second = text.slice(cutoff, text.length)
</script>

{first}<span class:hidden={!active}>{second}</span><button class="readmore" class:hidden={active || second.length == 0} on:click={() => (active = true)}>(read more)</button>

<style>
	.readmore {
		display: inline;
		margin-left: 0.25em;
		border: 0;
		outline: 0;
		padding: 0;
		background: none;
		color: blue;
		appearance: link;
	}

	.readmroe:hover {
		text-decoration: underline;
	}

	.hidden {
		display: none;
	}
</style>
