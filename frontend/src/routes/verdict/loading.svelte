<script>
	import { onMount, onDestroy } from 'svelte';
	import { slide } from 'svelte/transition';
	import LoadingBot from '$lib/assets/loading-bot.svg';

	let greetings = ['Verge', 'CNET', 'PC Mag'];
	let index = 0;
	let roller;

	onMount(() => {
		roller = setInterval(() => {
			if (index === greetings.length - 1) index = 0;
			else index++;
		}, 1250);
	});

	onDestroy(() => {
		clearInterval(roller);
	});
</script>

<div class="flex overflow-hidden w-full h-full">
	<div class="pt-10 pl-10 w-1/2">
		<h1
			class="inline-block mt-0 mb-1 text-8xl font-medium tracking-tighter leading-tight text-secondary"
		>
			Analysing Data <span class="block"
				>from

				{#key index}
					<span transition:slide class="text-primary">
						{greetings[index]}
					</span>
				{/key}
			</span>
		</h1>
		<span class="block mx-auto mt-20 scale-[5] text-primary loading loading-infinity loading-lg" />
	</div>
	<div class="flex place-content-center w-1/2">
		<img src={LoadingBot} alt="Loading your customized review" class="w-3/6 h-full" />
	</div>
</div>
