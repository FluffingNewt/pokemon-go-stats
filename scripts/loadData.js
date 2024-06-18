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

function fetchDataAndRender(includeUnavailable) {
      return new Promise((resolve, reject) => {
        fetch("../lib/pokemon.json")
          .then((r1) => r1.json())
          .then((data) => {
            const tableBody = document.querySelector("#pokemonTable tbody");
            tableBody.innerHTML = '';  // Clear existing rows

            for (const pokemonName in data) {
              const pokemon = data[pokemonName];

              if (!includeUnavailable && !pokemon.available) {
                continue;  // Skip unavailable Pokémon if the checkbox is not checked
              }

              for (const fastMove in pokemon.fast_moves) {
                const fm = pokemon.fast_moves[fastMove];

                for (const chargedMove in pokemon.charged_moves) {
                  const cm = pokemon.charged_moves[chargedMove];

                  const row = document.createElement("tr");
                  row.innerHTML = `
                    <td><img src="${pokemon.image}">${pokemon.name}</td>
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
            resolve();
          })
          .catch((error) => {
            console.error('Error fetching data:', error);
            reject(error);
          });
      });
    }

// !!!!!!!!!!!!!!! Script Calls !!!!!!!!!!!!!!!

$(document).ready(function() {

  function renderTable() {
    const includeUnavailable = $('#includeUnavailable').is(':checked');

    fetchDataAndRender(includeUnavailable).then(function() {
      var table = $('#pokemonTable').DataTable();

      table.clear().draw();

      // $('#pokemonFilter').on('keyup change', function() {
      //   table.column(0).search(this.value).draw();
      // });

      // $('#moveFilter').on('keyup change', function() {
      //   table.columns([1, 2]).search(this.value).draw();
      // });

      // Re-populate DataTable with updated data
      fetchDataAndRender(includeUnavailable).then(function() {
        table.rows.add($('#pokemonTable tbody tr')).draw();
      });
    }).catch(function(error) {
      console.error('Error rendering table:', error);
    });
  }

  // Initial rendering
  renderTable();

  // Event listener for checkbox change
  $('#includeUnavailable').on('change', function() {
    renderTable();
  });
});