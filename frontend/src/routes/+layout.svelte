<script>
	import '$lib/global.css';
	import '@fontsource/playfair-display';
	import '@fontsource/mohave';
	import { isPremium } from '$lib/store';
	import logo from '$lib/assets/logo.png';
	import { fade } from 'svelte/transition';
</script>

<div class="flex flex-col min-h-screen">
	<nav class="flex justify-between py-6 pr-10 pl-20 w-full">
		<div class="flex items-center">
			<img src={logo} alt="ReviewAI logo" class="w-12" />
			<a href="/">
				<h1 class="pl-3 text-3xl">ReviewAI</h1>
			</a>
		</div>
		<label class="swap swap-rotate">
			<input type="checkbox" bind:checked={$isPremium} />
			<svg
				fill="#000000"
				version="1.1"
				id="Layer_1"
				xmlns="http://www.w3.org/2000/svg"
				xmlns:xlink="http://www.w3.org/1999/xlink"
				viewBox="0 0 330 330"
				xml:space="preserve"
				class="swap-on"
			>
				<g id="XMLID_516_">
					<path
						id="XMLID_517_"
						d="M15,160c8.284,0,15-6.716,15-15V85c0-30.327,24.673-55,55-55c30.327,0,55,24.673,55,55v45h-25
		c-8.284,0-15,6.716-15,15v170c0,8.284,6.716,15,15,15h200c8.284,0,15-6.716,15-15V145c0-8.284-6.716-15-15-15H170V85
		c0-46.869-38.131-85-85-85S0,38.131,0,85v60C0,153.284,6.716,160,15,160z"
					/>
				</g>
			</svg>

			<svg
				fill="#000000"
				version="1.1"
				id="Layer_1"
				xmlns="http://www.w3.org/2000/svg"
				xmlns:xlink="http://www.w3.org/1999/xlink"
				viewBox="0 0 330 330"
				xml:space="preserve"
				class="w-10 h-10 swap-off"
			>
				<g id="XMLID_509_">
					<path
						id="XMLID_510_"
						d="M65,330h200c8.284,0,15-6.716,15-15V145c0-8.284-6.716-15-15-15h-15V85c0-46.869-38.131-85-85-85
		S80,38.131,80,85v45H65c-8.284,0-15,6.716-15,15v170C50,323.284,56.716,330,65,330z M180,234.986V255c0,8.284-6.716,15-15,15
		s-15-6.716-15-15v-20.014c-6.068-4.565-10-11.824-10-19.986c0-13.785,11.215-25,25-25s25,11.215,25,25
		C190,223.162,186.068,230.421,180,234.986z M110,85c0-30.327,24.673-55,55-55s55,24.673,55,55v45H110V85z"
					/>
				</g>
			</svg>

			<!-- <svg class="w-10 h-10 swap-off" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" -->
			<!-- 	><path -->
			<!-- 		d="M21.64,13a1,1,0,0,0-1.05-.14,8.05,8.05,0,0,1-3.37.73A8.15,8.15,0,0,1,9.08,5.49a8.59,8.59,0,0,1,.25-2A1,1,0,0,0,8,2.36,10.14,10.14,0,1,0,22,14.05,1,1,0,0,0,21.64,13Zm-9.5,6.69A8.14,8.14,0,0,1,7.08,5.22v.27A10.15,10.15,0,0,0,17.22,15.63a9.79,9.79,0,0,0,2.1-.22A8.11,8.11,0,0,1,12.14,19.73Z" -->
			<!-- 	/></svg -->
			<!-- > -->
		</label>
	</nav>

	<div class="flex-1">
		<slot />
	</div>
</div>
