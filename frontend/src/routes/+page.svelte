<script>
  import { onMount } from 'svelte';
  import { animate } from "animejs";
  let pokemonId = '';
  let pokemon = null;
  let error = '';

  // Funcion para peticiones a la pokeapi
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

<main class="bg-gray-900 text-gray-200 min-h-screen p-2">
    <div class="flex">
        <h1 class="text-3xl font-semibold w-[50%]">PokeChat</h1>
        <nav class="flex justify-end w-[50%]">
            <ul class="flex gap-4">
                <li class="text-lg hover:font-semibold hover:text-xl duration-200"><a href="/pokedex">Pokedex</a></li>
                <li class="text-lg hover:font-semibold hover:text-xl duration-200"><a href="/">Sobre mi</a></li>
                <li class="text-lg hover:font-semibold hover:text-xl duration-200"><a href="/">Contacto</a></li>
            </ul>
        </nav>
    </div>
    <div class="flex flex-col items-center p-4">
        <h1 class="text-2xl font-bold mb-4 text-gray-100">Buscar Pokémon</h1>
        <input type="number" bind:value={pokemonId} class="bg-gray-800 border border-gray-700 text-white p-2 rounded mb-2" placeholder="Número de Pokédex" />
        <button on:click={fetchPokemon} class="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded">Buscar</button>
      
        {#if error}
          <p class="text-red-400 mt-2">{error}</p>
        {/if}
      
        {#if pokemon}
          <div class="mt-4 p-4 border border-gray-700 rounded shadow-lg text-center bg-gray-800">
            <h2 class="text-xl font-semibold text-gray-100">{pokemon.name} (#{pokemon.id})</h2>
            <img src={pokemon.image} alt={pokemon.name} class="w-32 h-32 mx-auto bg-gray-700 p-2 rounded" />
            <p class="mt-2 text-gray-300">Tipo: {pokemon.types.join(', ')}</p>
          </div>
        {/if}
      </div>
</main>