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

fetch("../data/pokemon-mega.json")
  .then((r1) => r1.json())
  .then((data) => {
    console.log("Fetched data:", data);
    const tableBody = document.querySelector("#pokemonTable tbody");

    // Loop through each Pokémon in the data
    for (const pokemonName in data) {
      const pokemon = data[pokemonName];

      fetch("../data/fast_moves_pve.json")
        .then((r2) => r2.json())
        .then((fast_moves) => {

          for (const fastMove of pokemon.fast_moves) {
            const fm = fast_moves[fastMove];

            fetch("../data/charged_moves_pve.json")
              .then((r3) => r3.json())
              .then((charged_moves) => {
                
                for (const chargedMove of pokemon.charged_moves) {
                  const cm = charged_moves[chargedMove];

                  // Create a table row for each Pokémon
                  const row = document.createElement("tr");
                  row.innerHTML = `
                    <td><img src="${pokemon.image}">${pokemonName}</td>
                    <td><img src="${fm.image}">${fastMove}</td>
                    <td><img src="${cm.image}">${chargedMove}</td>
                    <td>Blah</td>
                    <td>Blah</td>
                    <td>Blah</td>
                    <td>${calcMaxCP(pokemon, true)}</td>
                  `;
                  tableBody.appendChild(row);
                }
              });
          }
        });
    }
  });

// Changes image sizes to fit cells
// window.onload = function () {
//   var images = document.querySelectorAll("table img");

//   images.forEach(function (img) {
//     var originalWidth = img.naturalWidth;
//     var originalHeight = img.naturalHeight;

//     if (img.src.includes("assets/types")) {
//       img.style.width = originalWidth * 0.45 + "px";
//       img.style.height = originalHeight * 0.45 + "px";
//     } else if (originalWidth > 40 && originalHeight > 30) {
//       img.style.width = originalWidth * 0.5882 + "px";
//       img.style.height = originalHeight * 0.5357 + "px";
//     }
//   });
// };
