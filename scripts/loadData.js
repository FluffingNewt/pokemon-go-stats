// function calcDPS() {

// }

// function calcTDO() {

// }

// function calcER() {

// }

function fetchDataAndRender(level, includeUnavailable, includeBest) {
      return new Promise((resolve, reject) => {
        fetch("lib/pokemon.json")
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
                    <td>${pokemon.maxCP[level]}</td>
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
    const level = document.querySelector('#level').value;
    const includeUnavailable = $('#includeUnavailable').is(':checked');
    const includeBest = $('#best').is(':checked');

    fetchDataAndRender(level, includeUnavailable, includeBest).then(function() {
      var table = $('#pokemonTable').DataTable();

      table.clear().draw();

      // Re-populate DataTable with updated data
      fetchDataAndRender(level, includeUnavailable, includeBest).then(function() {
        table.rows.add($('#pokemonTable tbody tr')).draw();
      });

    }).catch(function(error) {
      console.error('Error rendering table:', error);
    });
  }

  // Initial rendering
  renderTable();

  // Event listeners for checkbox changes
  $('#includeUnavailable').on('change', function() {
    renderTable();
  });
  $('#best').on('change', function() {
    renderTable();
  });
  $('#level').on('change', function() {
    renderTable();
  });
  
});