document.addEventListener('DOMContentLoaded', () => {
    // alert('youre here!')
    username = document.getElementById('username');
    if (username === null) {
    } else {
        alert("your username is {%s}", username);
    }
    });