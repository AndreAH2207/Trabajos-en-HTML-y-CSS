const body = document.querySelector('body'),
    sidebar = body.querySelector('nav'),
    bxMenu = body.querySelector('.bx-menu'), 
    menuSwitch = body.querySelector('.toggle-switch'); 

bxMenu.addEventListener('click', () => {
    sidebar.classList.toggle('close'); 
});

