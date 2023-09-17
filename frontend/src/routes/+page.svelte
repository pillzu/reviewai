<script>
	import TechReviewer from '$lib/assets/old_uncle.svg';
	import { story } from '$lib/store';
	import { goto } from '$app/navigation';

	function handleSubmit(params) {
		goto('/compare');
	}
</script>

<div class="flex h-full">
	<div class="grid justify-center items-end h-100% w-1/2">
		<img src={TechReviewer} alt="Your own tech reviewer" class="w-[88%] h-full" />
	</div>
	<div class="flex flex-col justify-center w-1/2">
		<hgroup class="mt-0.5">
			<h2 class="block mt-0 mb-0 text-5xl font-medium tracking-tighter leading-tight text-gray-400">
				Welcome to
			</h2>
			<h1
				class="block mt-0 mb-1 text-8xl font-medium tracking-tighter leading-tight text-secondary"
			>
				Review AI
			</h1>
		</hgroup>

		<p class="block mt-1 mb-3 ml-1 text-xl font-medium tracking-widest text-primary">
			Your one-stop shop for Laptop Comparison
		</p>

		<textarea
			name="text"
			class="p-3 w-5/6 h-40 rounded-lg border-2 resize-none focus:outline-primary"
			placeholder="Tell us about yourself and we'll help you find your next laptop..."
			bind:value={$story}
		/>
		<button
			disabled={$story == '' ? true : false}
			class="mt-12 w-5/6 text-lg text-white btn btn-secondary"
			on:click={handleSubmit}
		>
			👉 Let's go 👈
		</button>
	</div>
</div>

<style>
	* {
		font-family: 'Mohave', 'serif';
	}
</style>
