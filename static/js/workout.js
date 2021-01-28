let workout1 = document.querySelector('#workout1');
let workout2 = document.querySelector('#workout2');
let workout3 = document.querySelector('#workout3');
let workout4 = document.querySelector('#workout4');
let workout5 = document.querySelector('#workout5');
let workout6 = document.querySelector('#workout6');
let workout7 = document.querySelector('#workout7');
let workout8 = document.querySelector('#workout8');
let workout9 = document.querySelector('#workout9');
let workout10 = document.querySelector('#workout10');
let whattodo = document.querySelector(".whatto");

function apicall(a){
    if (a == 'legs'){
        readJson('https://wger.de/api/v2/exercise/?language=2&muscles=10&format=json&limit=10')
    }
    else if (a == 'arms'){
        readJson('https://wger.de/api/v2/exercise/?language=2&muscles=1&format=json&limit=10')
    }
    else if (a == 'abs'){
        readJson('https://wger.de/api/v2/exercise/?language=2&muscles=6&format=json&limit=10')
    }
    else{
        console.log('Invalid');
    }
}

let readJson = async (url) => {
    try {
      whattodo.style.display = "block";
      whattodo.textContent = "Loading....";
      let response = await fetch(url);
      let data = await response.json();
      displayOutput(data);
      whattodo.style.display = "none";
    } catch (err) {
      whattodo.style.display = "block";
      whattodo.textContent = "Something Went Wrong!";
      console.log(err);
    }
  };

  let displayOutput = (result) => {
    output = result.results
    output.forEach((element, i) => {
      let display = `<div class="onework">
      <h3 class="onehead">${element.name}</h3><br>${element.description}
      </div>`;
      eval(`workout${i+1}`).innerHTML = display;
      console.log(output[i]);
    });
  };

