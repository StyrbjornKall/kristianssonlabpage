fetch('footer.html')
    .then(response => response.text())
    .then(data => {
        document.getElementById('footer-placeholder').innerHTML = data;
        document.body.classList.remove('is-preload');
    })
    .catch(error => console.error('Error loading footer:', error));