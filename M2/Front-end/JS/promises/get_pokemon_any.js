function getPokemons(pokemosID) {
  return fetch(`https://pokeapi.co/api/v2/pokemon/${pokemosID}`)
      .then((response) => {
        return response.json()
      })
  };


const pokemosID = [1, 5, 2];
let pokemonsPromise = [];
for (let id of pokemosID) {
    pokemonsPromise.push(getPokemons(id))
}

Promise.any(pokemonsPromise).then((value) => {
    console.log(value.name)
});