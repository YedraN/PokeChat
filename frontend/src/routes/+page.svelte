<script>
	import { onMount } from 'svelte';
	let pokemonId = '';
	let pokemon = null;
	let error = '';

	async function fetchPokemon() {
		if (!pokemonId) {
			error = 'Por favor, introduce un número de Pokédex';
			return;
		}

		error = '';
		pokemon = null;

		try {
			const res = await fetch(`http://localhost:5000/pokemon?id=${pokemonId}`);
			const data = await res.json();

			if (data.error) {
				error = data.error;
			} else {
				pokemon = data;
			}
		} catch (err) {
			error = 'Error al obtener los datos del Pokémon';
		}
	}
</script>

<main class="min-h-screen bg-gray-900 p-2 text-gray-200">
	<div class="flex">
		<h1 class="w-[50%] text-3xl font-semibold">PokeChat</h1>
		<nav class="flex w-[50%] justify-end">
			<ul class="flex gap-4">
				<li class="text-lg duration-200 hover:text-xl hover:font-semibold">
					<a href="/pokedex">Pokedex</a>
				</li>
				<li class="text-lg duration-200 hover:text-xl hover:font-semibold">
					<a href="/">Sobre mi</a>
				</li>
				<li class="text-lg duration-200 hover:text-xl hover:font-semibold">
					<a href="/">Contacto</a>
				</li>
			</ul>
		</nav>
	</div>
	<div class="flex flex-col items-center p-4">
		<h1 class="mb-4 text-2xl font-bold text-gray-100">Buscar Pokémon</h1>
		<input
			type="number"
			bind:value={pokemonId}
			class="mb-2 rounded border border-gray-700 bg-gray-800 p-2 text-white"
			placeholder="Número de Pokédex"
		/>
		<button
			on:click={fetchPokemon}
			class="rounded bg-blue-600 px-4 py-2 text-white hover:bg-blue-700">Buscar</button
		>

		{#if error}
			<p class="mt-2 text-red-400">{error}</p>
		{/if}

		{#if pokemon}
			<div class="mt-4 rounded border border-gray-700 bg-gray-800 p-4 text-center shadow-lg">
				<h2 class="text-xl font-semibold text-gray-100">{pokemon.name} (#{pokemon.id})</h2>
				<img
					src={pokemon.image}
					alt={pokemon.name}
					class="mx-auto h-32 w-32 rounded bg-gray-700 p-2"
				/>
				<p class="mt-2 text-gray-300">Tipo: {pokemon.types.join(', ')}</p>
			</div>
		{/if}
	</div>
</main>
