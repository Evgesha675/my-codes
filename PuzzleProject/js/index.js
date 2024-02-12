/*Область с ячейками*/
let mainWindowPuzzle = document.querySelector(`#main-puzzle`);
let mainWindowPicture = document.querySelector(`#main-picture`);

/*Область с кнопками для выбора лвл*/
let headerBtn = document.querySelector(`.header-btn`);

/*Подсказка*/
let btnHelp = document.querySelector(`#btn-help`);
let windowHelp = document.querySelector(`#window-help`);

/*Область с пазлами*/
let placePuzzle = document.querySelector(`#place-puzzle`);

/*Размеры для сбора сетки*/
let wTile = 9;
let hTile = 6;

/*Площадь изображения*/
let S = hTile * wTile;

/*Размеры для сбора пазлов*/
wPuz = 14;
hPuz = 4;

/*Элементы строк и столбцов сетки*/
let tileS = `<div class="d-flex main-puzzle">`;
let tileE = `</div>`;

let puzS = `<div class="d-flex place-puzzle">`;
let puzE = `</div>`;

/*Сборка сетки из ячеек*/
function selectLvl(evt) {

    /*Куда мы нажали*/
    let btn = evt.target;

    /*Проверка, что нажали на кнопку*/
    if (btn.classList.contains(`btn`)) {

        /*Сюда собираются пазлы*/
        let tile = ``;
        let puz = ``;

        /*Значние для пазлов (путь к картинкам)*/
        let counter = 0;
        let val = 0;

        /*Всё стираем для дальнейшего заполнения*/
        mainWindowPuzzle.innerHTML = ``;
        mainWindowPicture.innerHTML = ``;

        /*Получаем значение нажатой кнопки*/
        val = Number(btn.value);

        /*Сборка сетки*/
        for (let i = 0; i < hTile; i++) {
            tile += tileS;
            for (let j = 0; j < wTile; j++) {
                tile += `<div class="item-tile"></div>`;
            }
            tile += tileE;
        }

        /*Сборка пазлов*/
        let arr = gerRandomNum(S);
        for (let i = 0; i < hPuz; i++) {
            puz += puzS;
            for (let j = 0; j < wPuz; j++) {
                puz += `<div class="item-puz"><img src="assets/pic${val}/${arr[counter]}.png" alt="" width="50px" height="50px"></div>`;
                counter++;
                if (counter >= S) {
                    break;
                }
            }
            puz += puzE;
        }

        /*Вставляем картинку, которую надо собрать*/
        mainWindowPicture.innerHTML = `<div class="main-picture"><img src="assets/pic${val}/picture${val}.png" alt="" width="420px" height="270px"></div>`;

        /*Вставляем сетку для пазлов*/
        mainWindowPuzzle.innerHTML = tile;

        /*Удаляем класс закрывающий кнопку "Подсказка"*/
        btnHelp.classList.remove(`d-none`);

        /*Вставляем пазлы*/
        placePuzzle.innerHTML = puz;
    }
}

/*Генерация рандомных и уникальных чисел от 1 до 54 с выводом массива*/
function gerRandomNum(max) {
    let min = 1;
    let i = min;
    let arrRandomNum = [];
    let randomNum;

    while(i <= max) {
        randomNum = Math.floor(Math.random() * (max - min + 1)) + min;
        if (!arrRandomNum.includes(randomNum)) {
            arrRandomNum.push(randomNum);
            i++;
        } else {
            continue;
        }
    }
    return arrRandomNum;
}

/*Обработчики для кнопок выбора лвл*/
headerBtn.addEventListener(`click`, selectLvl);

/*Обработчики для выбора пазла*/
placePuzzle.addEventListener(``,);

btnHelp.addEventListener(`click`, function() {
    mainWindowPicture.classList.toggle(`d-none`);
});
