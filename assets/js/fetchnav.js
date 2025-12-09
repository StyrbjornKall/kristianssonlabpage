fetch('nav.html')
    .then(response => response.text())
    .then(data => {
        document.getElementById('nav-placeholder').innerHTML = data;
        document.body.classList.remove('is-preload');
    })
    .catch(error => console.error('Error loading nav:', error));