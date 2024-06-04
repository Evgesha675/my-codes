document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("banner").addEventListener("click", function() {
        // Перенаправление на другой HTML документ
        window.location.href = "index.html";
      });
    // Получаем все элементы с классом "slider" на странице
    let sliders = document.getElementsByClassName("slider");

    // Проходимся по каждому слайдеру
    Array.from(sliders).forEach(slider => {
        // Определяем переменные для текущего слайдера
        let slideIndex = 0;
        let slides = slider.querySelectorAll(".slides img");
        let intervalID; // Для хранения ID интервала

        // Функция для отображения конкретного слайда
        function showSlide(n) {
            if (n >= slides.length) { slideIndex = 0 }    
            if (n < 0) { slideIndex = slides.length - 1 }
            
            for (let i = 0; i < slides.length; i++) {
                slides[i].classList.remove('active');  
            }
            
            slides[slideIndex].classList.add('active');
        } 
        
        function plusSlide(n) {
            showSlide(slideIndex += n);
        } 

        // Функция для запуска автоматической смены слайдов
        function startSlideShow() {
            intervalID = setInterval(function() {
                plusSlide(1);
            }, 2000);
        }

        // Функция для остановки автоматической смены слайдов
        function stopSlideShow() {
            clearInterval(intervalID);
        }

        // Функция для обработки пересечения
        function handleIntersect(entries) {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    startSlideShow(); // Начинаем автоматическую смену слайдов
                } else {
                    stopSlideShow(); // Останавливаем автоматическую смену слайдов
                }
            });
        }

        // Создаем IntersectionObserver
        let observer = new IntersectionObserver(handleIntersect);

        // Устанавливаем первое изображение в качестве активного
        showSlide(0);

        // Наблюдаем за текущим слайдером
        observer.observe(slider);

        // Устанавливаем превью последнего активного изображения для неактивного слайдера
        let previewSlide = slider.querySelector(".preview img");
        if (previewSlide) {
            previewSlide.src = slides[slides.length - 1].src;
        }
    });
});
