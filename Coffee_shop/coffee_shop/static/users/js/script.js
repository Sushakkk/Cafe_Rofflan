// const signUpButton = document.getElementById('signUp');
// const signInButton = document.getElementById('signIn');
// const container = document.getElementById('container');

// signUpButton.addEventListener('click', () =>
// container.classList.add('right-panel-active'));

// signInButton.addEventListener('click', () =>
// container.classList.remove('right-panel-active'));

document.addEventListener("DOMContentLoaded", () => { //Ждем загрузки всей HTML-разметки перед выполнением кода.
    const signUpButton = document.getElementById('signUp');//Инициализация элементов
    const signInButton = document.getElementById('signIn');
    const container = document.getElementById('container');

    // Проверка состояния при загрузке страницы
    if (localStorage.getItem('rightPanelActive') === 'true') { //Если значение в localStorage равно 'true',
                                                              // добавляем класс right-panel-active к контейнеру.
        container.classList.add('right-panel-active');
    }

    signUpButton.addEventListener('click', () => {
        container.classList.add('right-panel-active');//При клике на кнопку "Sign Up" добавляем класс 
        localStorage.setItem('rightPanelActive', 'true');//right-panel-active к контейнеру и сохраняем это состояние в localStorage.
    });

    signInButton.addEventListener('click', () => {
        container.classList.remove('right-panel-active'); // При клике на кнопку "Sign In" удаляем класс right-panel-active                                             
        localStorage.setItem('rightPanelActive', 'false'); // с контейнеру и сохраняем это состояние в localStorage.
    });
});
