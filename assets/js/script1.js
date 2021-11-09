const sliderPrev = document.querySelector('.slider__prev'),
    sliderNext = document.querySelector('.slider__next'),
    sliderItems = document.querySelectorAll('.slider__item');

document.querySelectorAll('.slider__image').forEach(image => image.addEventListener('mousedown', e => e.preventDefault()))

let active;

sliderItems.forEach((el, i) => {
    if (el.classList.contains('active')) active = i
})

sliderNext.addEventListener('click', () => sliderMove(sliderNext))
sliderPrev.addEventListener('click', () => sliderMove(sliderPrev))

const sliderMove = button => {
    sliderItems.forEach(el => el.classList.remove('active'))
    if (button === sliderNext) {
        active++
        active = active >= sliderItems.length ? 0 : active
    } else {
        active--
        active = active < 0 ? sliderItems.length - 1 : active
    }
    sliderItems[active].classList.add('active')
}
let stopIterval = setInterval(() => {
    sliderMove(sliderNext)
}, 3000);

const slider = document.querySelector('.slider');
slider.addEventListener('mouseover', () => {
    clearInterval(stopIterval)
})
slider.addEventListener('mouseout', () => {
    stopIterval = setInterval(() => {
        sliderMove(sliderNext)
    }, 3000);
})

addEventListener('keydown', e => {
    if (e.code === 'ArrowDown') sliderMove(sliderNext)
    else if (e.code === 'ArrowUp') sliderMove(sliderPrev)
})