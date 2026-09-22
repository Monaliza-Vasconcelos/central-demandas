const botaoMenu = document.querySelector('#botao-menu');
const sidebar = document.querySelector('.sidebar');

const sidebarRecolhida = localStorage.getItem('sidebarRecolhida');

if (sidebarRecolhida === 'true') {
    sidebar.classList.add('recolhida');
}

botaoMenu.addEventListener('click', function () {
    sidebar.classList.toggle('recolhida');

    localStorage.setItem(
        'sidebarRecolhida',
        sidebar.classList.contains('recolhida')
    );
});