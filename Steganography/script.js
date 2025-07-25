const container = document.getElementById('container');
const registerBtn = document.getElementById('register');
const loginBtn = document.getElementById('login');

registerBtn.addEventListener('click', () => {
    container.classList.add("active");
});
loginBtn.addEventListener('click', () => {
    container.classList.remove("active");
});

if (window.innerWidth <= 600) {
    var link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = 'mobile.css';  // your mobile CSS file path
    document.head.appendChild(link);
  }