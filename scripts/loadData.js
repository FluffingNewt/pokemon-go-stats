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

function fetchDataAndRender() {
  // Adds megas to table
  fetch("../lib/pokemon.json")
    .then((r1) => r1.json())
    .then((data) => {
      console.log("Fetched data:", data);
      const tableBody = document.querySelector("#pokemonTable tbody");

      // Loop through each Pokémon in the data
      for (const pokemonName in data) {
        const pokemon = data[pokemonName];

        for (fastMove in pokemon.fast_moves) {
          const fm = pokemon.fast_moves[fastMove];

          for (chargedMove in pokemon.charged_moves) {
            const cm = pokemon.charged_moves[chargedMove];

            // Create a table row for each Pokémon
            const row = document.createElement("tr");
            row.innerHTML = `
                      <td><img src="${pokemon.image}">${pokemonName}</td>
                      <td id="type-img"><img src="${fm.image}">${fastMove}</td>
                      <td id="type-img"><img src="${cm.image}">${chargedMove}</td>
                      <td>Blah</td>
                      <td>Blah</td>
                      <td>Blah</td>
                      <td>${calcMaxCP(pokemon, true)}</td>
                    `;
            tableBody.appendChild(row);
          }
        }
      }
    }
  );
}

// Function to filter the table based on user input
function filterTable() {
  const filterValue = document
    .getElementById("filterInput")
    .value.toLowerCase();
  const rows = document.querySelectorAll("#pokemonTable tbody tr");

  rows.forEach((row) => {
    const typeCell = row
      .querySelector("td:nth-child(1)")
      .textContent.toLowerCase();
    if (typeCell.includes(filterValue)) {
      row.style.display = "";
    } else {
      row.style.display = "none";
    }
  });
}

// Fetch data and render the table on page load
fetchDataAndRender();

// Add event listener for the filter input box
document.getElementById("filterInput").addEventListener("input", filterTable);
