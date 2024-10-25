let currentSlide = 0;
const slides = document.querySelector('.slides');

function moveSlide(direction) {
  const totalSlides = document.querySelectorAll('.slide').length;

  currentSlide += direction;

  if (currentSlide >= totalSlides) {
    currentSlide = 0; // Go back to the first slide
  } else if (currentSlide < 0) {
    currentSlide = totalSlides - 1; // Go to the last slide
  }

  const slideWidth = slides.querySelector('.slide').clientWidth;
  slides.style.transform = `translateX(-${currentSlide * slideWidth}px)`;
}
