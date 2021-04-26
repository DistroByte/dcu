function debounce(func, wait = 10, immediate = true) {
  var timeout;
  return function () {
    var context = this, args = arguments;
    var later = function () {
      timeout = null;
      if (!immediate) func.apply(context, args);
    };
    var callNow = immediate && !timeout;
    clearTimeout(timeout);
    timeout = setTimeout(later, wait);
    if (callNow) func.apply(context, args);
  };
};


function checkAnimate() {
  const elements = document.querySelectorAll('.animate');
  elements.forEach(element => {
    // half way through the element
    const activateAt = (window.scrollY + window.innerHeight) - element.clientHeight / 2;
    // bottom of the element
    const elementBottom = element.offsetTop + element.clientHeight;
    // checks if element is on screen
    const isHalfShown = activateAt > element.offsetTop;
    const isNotScrolledPast = window.scrollY < elementBottom;
    // activates animation
    if (isHalfShown && isNotScrolledPast) {
      element.classList.add('active');
    }
  });
}

window.addEventListener('scroll', debounce(checkAnimate));