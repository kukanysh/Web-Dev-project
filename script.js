const input = document.querySelector("#movieTitle")
const btn = document.querySelector("#btn")
const cataloge = document.querySelector(".cataloge")

async function getData(input){
    const url = 'https://imdb8.p.rapidapi.com/title/find?q=' + input;
    const options = {
        method: 'GET',
        headers: {
            'X-RapidAPI-Key': '17b95ea668mshfb6244025ea21c3p1611a6jsne752a33b0344',
            'X-RapidAPI-Host': 'imdb8.p.rapidapi.com'
        }
    };
    const response = await fetch(url, options);
    const result = await response.json();
    return result;
    
}


btn.addEventListener("click", async () => {
    const result = await getData(input.value)
    const results = result.results
    for(let item = 0; item < results.length; item++){
        if(results[item].titleType === "movie"){
            cataloge.innerHTML += `
                <div class="film">
                    <div class="img"><img src=${results[item].image.url} alt=""></div>
                    <div class="title">${results[item].title}</div>
                    <div class="runTime">${results[item].runningTimeInMinutes} min</div>
                    <div class="year">${results[item].year}</div>
                </div>
            `
        }
    }
})
