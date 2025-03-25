<script>
  import { onMount } from 'svelte';
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
</main>