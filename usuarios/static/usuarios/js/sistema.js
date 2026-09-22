const botaoMenu = document.querySelector('#botao-menu');
const sidebar = document.querySelector('.sidebar');
const fecharMenu = document.querySelector('#fechar-menu');

const sidebarRecolhida = localStorage.getItem('sidebarRecolhida');

if (sidebarRecolhida === 'true') {
    sidebar.classList.add('recolhida');
}

botaoMenu.addEventListener('click', function () {

    if (window.matchMedia('(max-width: 768px)').matches) {
        sidebar.classList.toggle('aberta');
        return;
    }

    sidebar.classList.toggle('recolhida');

    localStorage.setItem(
        'sidebarRecolhida',
        sidebar.classList.contains('recolhida')
    );
});

fecharMenu.addEventListener('click', function () {
    sidebar.classList.remove('aberta');
});