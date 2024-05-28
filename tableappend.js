// function calcDPS() {

// }

// function calcTDO() {

// }

// function calcER() {

// }

function calcMaxCP(pokemon, level50) {
  level50 ? (cpm = 0.84029999) : (cpm = 0.7903);
  cp =
    ((pokemon.stats.attack + 15) *
      Math.pow(pokemon.stats.defense + 15, 0.5) *
      Math.pow(pokemon.stats.hp + 15, 0.5) *
      Math.pow(cpm, 2)) /
    10;
  return Math.floor(Math.max(10, cp));
}

fetch("pokemon-mega.json")
  .then((response) => response.json())
  .then((data) => {
    console.log("Fetched data:", data);
    const tableBody = document.querySelector("#pokemonTable tbody");

    // Loop through each Pokémon in the data
    for (const pokemonName in data) {
      const pokemon = data[pokemonName];

      // Create a table row for each Pokémon
      const row = document.createElement("tr");
      row.innerHTML = `
              <td>${pokemonName}</td>
              <td>Blah</td>
              <td>Blah</td>
              <td>Blah</td>
              <td>Blah</td>
              <td>Blah</td>
              <td>${calcMaxCP(pokemon, true)}</td>
        `;
      tableBody.appendChild(row);
    }
  });

// Changes image sizes to fit cells
window.onload = function () {
  var images = document.querySelectorAll("table img");

  images.forEach(function (img) {
    var originalWidth = img.naturalWidth;
    var originalHeight = img.naturalHeight;

    if (img.src.includes("assets/types")) {
      img.style.width = originalWidth * 0.45 + "px";
      img.style.height = originalHeight * 0.45 + "px";
    } else if (originalWidth > 40 && originalHeight > 30) {
      img.style.width = originalWidth * 0.5882 + "px";
      img.style.height = originalHeight * 0.5357 + "px";
    }
  });
};
