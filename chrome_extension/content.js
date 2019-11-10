let articles = document.querySelectorAll('article');
paragraphs = [];
articles[0].querySelectorAll('p').forEach((data) => {
    paragraphs.push(data)
});

// fetch("http://localhost:5000");

(async function(contents){
    contents[2].innerHTML = `This is me trying to <mark>whateer whatever whatever</mark> this and that something trying tom ake stuff up.`
    contents[8].innerHTML = `This is me trying to <mark>whateer whatever whatever</mark> this and that something trying tom ake stuff up.`
    console.log(contents)
    console.log(contents.map(e => e.textContent))
    
    try {
        console.error("--------------------------------error--------------------------------");
        const data = await postData('http://localhost:5000', { data: contents.map(e => e.textContent.trim()) });
        console.log(data); // JSON-string from `response.json()` call
      } catch (error) {
        console.error("--------------------------------error--------------------------------");
      }
})(paragraphs);
  
async function postData(url = '', data = {}) {
    // Default options are marked with *
    const response = await fetch(url, {
      method: 'POST', // *GET, POST, PUT, DELETE, etc.
      mode: 'cors', // no-cors, *cors, same-origin
      cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
      credentials: 'same-origin', // include, *same-origin, omit
      headers: {
        'Content-Type': 'application/json'
        // 'Content-Type': 'application/x-www-form-urlencoded',
      },
      redirect: 'follow', // manual, *follow, error
      referrer: 'no-referrer', // no-referrer, *client
      body: JSON.stringify(data) // body data type must match "Content-Type" header
    });
    return await response.json(); // parses JSON response into native JavaScript objects
  }