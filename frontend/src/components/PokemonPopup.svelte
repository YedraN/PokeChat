<script>
  export let pokemon = null;
  export let closePopup;
</script>

{#if pokemon}
  <div class="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center">
    <div class="bg-gray-900 text-gray-200 p-6 rounded-lg max-w-md w-full shadow-xl relative">
      <button class="absolute top-2 right-2 text-gray-400 hover:text-white text-2xl" on:click={closePopup}>&times;</button>
      
      <h2 class="text-2xl font-bold capitalize text-center">{pokemon.name}</h2>
      <img class="w-32 h-32 mx-auto mt-4" src={pokemon.sprites.front_default} alt={pokemon.name} />
      
      <div class="mt-4 space-y-2">
        <p><strong>ID:</strong> {pokemon.id}</p>
        <p><strong>Altura:</strong> {pokemon.height / 10} m</p>
        <p><strong>Peso:</strong> {pokemon.weight / 10} kg</p>
        <p><strong>Habilidades:</strong> {pokemon.abilities.map(a => a.ability.name).join(', ')}</p>
        <p><strong>Tipos:</strong> {pokemon.types.map(t => t.type.name).join(', ')}</p>
        <p><strong>Stats:</strong></p>
        <ul class="list-disc list-inside">
          {#each pokemon.stats as stat}
            <li><strong>{stat.stat.name}:</strong> {stat.base_stat}</li>
          {/each}
        </ul>
      </div>
    </div>
  </div>
{/if}