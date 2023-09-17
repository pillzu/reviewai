<script>
	import MyLoading from './loading.svelte';
	import VerdictBot from '$lib/assets/verdict.svg';
	import { story, product_1, product_2, isPremium } from '$lib/store';
	import { dev } from '$app/environment';
	const fetchData = (async () => {
		const url = false ? 'http://localhost:5000/' : 'https://review-ai.up.railway.app/';
		const resp = await fetch(url, {
			method: 'POST',
			headers: {
				Accept: 'application/json',
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({
				product_1: $product_1,
				product_2: $product_2,
				story: $story,
				is_premium: $isPremium
			})
		});

		return await resp.json();
	})();
</script>

{#await fetchData}
	<MyLoading />
{:then data}
	<div class="flex overflow-hidden flex-col w-full h-full">
		<div class="flex justify-center w-full">
			<img src={VerdictBot} alt="Best Device of all" class="w-1/6 h-5/6" />
		</div>
		<div class="">
			<h1
				class="block mt-3 mb-1 text-4xl font-medium tracking-tighter leading-tight text-center text-black"
			>
				Voila! Here's your very own <span class="block mt-2 text-secondary"
					>🎉<bold>Product Review</bold>🎉</span
				>
			</h1>
			<div class="flex mt-5 w-full h-1/2 text-center">
				<div class="flex-1">
					<h2
						class="block mt-0 mb-0 text-3xl font-medium tracking-tighter leading-tight text-center text-gray-400"
					>
						Product #1
					</h2>
					<p class="mt-5 w-full text-4xl text-center">Macbook Air M2</p>
				</div>
				<div class="flex-1">
					<button class="mt-5 w-5/6 text-lg text-white btn btn-primary">
						<a href="/">
							<span class="pr-5 scale-150">🙌</span>Generate Another One
							<span class="pl-5 scale-150">🙌</span>
						</a>
					</button>
				</div>
				<div class="flex flex-col flex-1 items-center">
					<h2
						class="block mt-0 mb-0 text-3xl font-medium tracking-tighter leading-tight text-center text-gray-400"
					>
						Product #2
					</h2>
					<p class="mt-5 w-full text-4xl text-center">Dell Latitude Z15</p>
				</div>
			</div>
		</div>
		<div
			class="p-10 my-10 mx-auto mb-20 w-5/6 text-white shadow-2xl min-h-[50%] bg-secondary card card-compact"
		>
			{#if data.is_premium}
				<p>{data}</p>
			{:else}
				<p>The ideal laptop for your usecase would be {data.suggested_product}</p>
			{/if}
		</div>
	</div>
{:catch error}
	<p>An error occurred! {error}</p>
{/await}
