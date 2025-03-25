<script>
  import { onMount } from 'svelte';
  import PokemonPopup from '../../components/PokemonPopup.svelte';

  let pokemons = [];
  let selectedPokemon = null;
  let loading = false;

  // Cargar la lista de Pokémon
  onMount(async () => {
    try {
      const res = await fetch('https://pokeapi.co/api/v2/pokemon?limit=151');
      const data = await res.json();
      pokemons = data.results.map((pokemon, index) => ({
        ...pokemon,
        id: index + 1, // Agregar ID manualmente
      }));
    } catch (error) {
      console.error("Error al cargar la Pokédex:", error);
    }
  });

  // Función para abrir el popup y obtener la información detallada
  async function openPopup(pokemon) {
    loading = true;
    console.log("Cargando datos de:", pokemon.name);

    try {
      const res = await fetch(`https://pokeapi.co/api/v2/pokemon/${pokemon.id}`);
      selectedPokemon = await res.json();
      console.log("Datos cargados:", selectedPokemon);
    } catch (error) {
      console.error("Error al cargar los datos del Pokémon:", error);
    }

    loading = false;
  }

  // Cerrar el popup
  function closePopup() {
    selectedPokemon = null;
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
    
    <br>

    <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-6 gap-4">
        {#each pokemons as pokemon, i}
          <div class="bg-gray-800 p-4 rounded-lg text-center shadow-lg">
            <img 
              src={`https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/${i + 1}.png`} 
              alt={pokemon.name} 
              class="w-24 h-24 mx-auto"
            />
            <p class="text-lg font-semibold capitalize mt-2">{pokemon.name}</p>
          </div>
        {/each}
    </div>

    {#if loading}
        <p class="text-center text-xl mt-6">Cargando...</p>
    {/if}

    {#if selectedPokemon}
        <PokemonPopup pokemon={selectedPokemon} closePopup={closePopup} />
    {/if}
</main>