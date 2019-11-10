let articles = document.querySelectorAll('article');
paragraphs = [];
articles[0].querySelectorAll('p').forEach((data) => {
    paragraphs.push(data)
});

// fetch("http://localhost:5000");

(async function(contents){
    contents[2].innerHTML = `This is me trying to <mark>whateer whatever whatever</mark> this and that something trying tom ake stuff up.`
    contents[8].innerHTML = `This is me trying to <mark>whateer whatever whatever</mark> this and that something trying tom ake stuff up.`
    // console.log(contents)
    // console.log(contents.map(e => e.textContent))
    
    try {
        chrome.extension.sendMessage({ data: contents.map(e => e.textContent) }, {title: 'postData'}, 
          function (response) {
            console.log('hello')
            console.log('Response From API', response);
        });
      } catch (error) {
        console.error("--------------------------------error--------------------------------");
      }
})(paragraphs);