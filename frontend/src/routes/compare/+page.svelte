<script>
	import { goto } from '$app/navigation';
	import PhoneWorld from '$lib/assets/phone.svg';
	import { product_1, product_2 } from '$lib/store';

	function handleSubmit() {
		goto('/verdict');
	}
</script>

<div class="flex overflow-hidden flex-col w-full h-full">
	<div class="w-full h-1/2 text-center">
		<h1
			class="block mt-0 mb-1 text-5xl font-medium tracking-tighter leading-tight text-center text-gray-400"
		>
			What Products are you looking to <span class="block">compare?</span>
		</h1>

		<p class="mt-3 mb-0 text-lg font-extralight text-primary">
			🔍 You give us the name, we’ll do the research for you 🔍
		</p>

		<button
			disabled={$product_1 == '' || $product_2 == '' ? true : false}
			class="mt-2 w-1/4 text-lg text-white btn btn-primary"
			on:click={handleSubmit}
		>
			🥳 Give me my review 🥳
		</button>
	</div>
	<div class="flex w-full h-1/2 text-center">
		<div class="flex-1">
			<h2
				class="block mt-0 mb-0 text-3xl font-medium tracking-tighter leading-tight text-center text-black"
			>
				Product #1
			</h2>
			<input
				type="text"
				placeholder="Type here (Eg. Macbook Air M2 2022)"
				class="mt-5 w-5/6 max-w-xs text-xl text-center bg-base-100 input"
				maxlength="94"
				bind:value={$product_1}
			/>
		</div>
		<div class="flex-1">
			<img src={PhoneWorld} alt="Best Device of all" class="mt-7 scale-105" />
		</div>
		<div class="flex flex-col flex-1 items-center">
			<h2 class="block mt-0 mb-0 text-3xl font-medium tracking-tighter leading-tight text-black">
				Product #2
			</h2>
			<input
				type="text"
				placeholder="Type here (Eg. Dell Latitude 7277 2022)"
				class="mt-5 w-5/6 max-w-xs text-xl text-center input"
				maxlength="94"
				bind:value={$product_2}
			/>
		</div>
	</div>
</div>
