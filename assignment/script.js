// Selectors
document.addEventListener("DOMContentLoaded", function () {
    const mainImage = document.getElementById('mainImage');
    const zoomContainer = document.getElementById('mainImageContainer');
    const result = document.getElementById('zoomResult');
    const lens = document.getElementById('zoomLens');
    let isZoomed = false;

    if (mainImage && zoomContainer && result && lens) {
        // Create zoom effect on hover
        zoomContainer.addEventListener("mouseenter", function () {
            lens.style.display = 'flex'; // Centering the SVG inside
        });

        // Click to toggle zoom pane
        zoomContainer.addEventListener("click", function (e) {
            if (e.target.closest('.carousel-arrow')) return;
            isZoomed = !isZoomed;
            if (isZoomed) {
                result.style.backgroundImage = `url(${mainImage.src})`;
                result.style.display = 'block';
                moveZoom(e); // Initialize position
            } else {
                result.style.display = 'none';
            }
        });

        zoomContainer.addEventListener("mousemove", function (e) {
            moveLensOnly(e);
            if (isZoomed) {
                moveZoom(e);
            }
        });

        zoomContainer.addEventListener("mouseleave", function () {
            result.style.display = 'none';
            lens.style.display = 'none';
            isZoomed = false;
        });

        function moveLensOnly(e) {
            const { left, top, width, height } = mainImage.getBoundingClientRect();
            let x = e.clientX - left;
            let y = e.clientY - top;
            let lensX = x - (lens.offsetWidth / 2);
            let lensY = y - (lens.offsetHeight / 2);

            if (lensX < 0) lensX = 0;
            if (lensY < 0) lensY = 0;
            if (lensX > width - lens.offsetWidth) lensX = width - lens.offsetWidth;
            if (lensY > height - lens.offsetHeight) lensY = height - lens.offsetHeight;

            lens.style.left = `${lensX}px`;
            lens.style.top = `${lensY}px`;
        }

        function moveZoom(e) {
            e.preventDefault();

            const { left, top, width, height } = mainImage.getBoundingClientRect();

            // Scaling ratios
            const cx = result.offsetWidth / lens.offsetWidth;
            const cy = result.offsetHeight / lens.offsetHeight;

            // Adjust result background size
            result.style.backgroundSize = `${width * cx}px ${height * cy}px`;

            // Calculate cursor relative X and Y inside the image
            let x = e.clientX - left;
            let y = e.clientY - top;

            // Ensure lens doesn't go out of bounds
            let lensX = x - (lens.offsetWidth / 2);
            let lensY = y - (lens.offsetHeight / 2);

            if (lensX < 0) lensX = 0;
            if (lensY < 0) lensY = 0;
            if (lensX > width - lens.offsetWidth) lensX = width - lens.offsetWidth;
            if (lensY > height - lens.offsetHeight) lensY = height - lens.offsetHeight;

            // Position the lens
            lens.style.left = `${lensX}px`;
            lens.style.top = `${lensY}px`;

            // Position the background result
            result.style.backgroundPosition = `-${lensX * cx}px -${lensY * cy}px`;
        }
    }

    // FAQ Accordion
    const faqItems = document.querySelectorAll('.faq-item');
    faqItems.forEach(item => {
        item.querySelector('.faq-question').addEventListener('click', () => {
            const isActive = item.classList.contains('active');
            faqItems.forEach(i => {
                i.classList.remove('active');
            });
            if (!isActive) {
                item.classList.add('active');
            }
        });
    });

    // Applications carousel swipe/buttons
    const appCarousel = document.getElementById('appCarousel');
    const scrollAmount = 300;

    const prevApp = document.querySelector('.prev-app');
    const nextApp = document.querySelector('.next-app');

    if (prevApp && nextApp && appCarousel) {
        prevApp.addEventListener('click', () => {
            appCarousel.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
        });
        nextApp.addEventListener('click', () => {
            appCarousel.scrollBy({ left: scrollAmount, behavior: 'smooth' });
        });
    }
});

// Gallery Thumbnails
const images = [
    "https://images.unsplash.com/photo-1544551763-46a0121087dd?auto=format&fit=crop&q=80&w=800",
    "https://images.unsplash.com/photo-1504917595217-d4dc5ebe6122?auto=format&fit=crop&q=80&w=800",
    "https://images.unsplash.com/photo-1531265726475-52ad60219627?auto=format&fit=crop&q=80&w=800",
    "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&q=80&w=800",
    "https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&q=80&w=800",
    "https://images.unsplash.com/photo-1504917595217-d4dc5ebe6122?auto=format&fit=crop&q=80&w=800"
];
let currentImageIndex = 0;

function setImage(index) {
    currentImageIndex = index;
    const mainImgNode = document.getElementById('mainImage');
    if (mainImgNode) mainImgNode.src = images[index];

    const result = document.getElementById('zoomResult');
    if (result) result.style.backgroundImage = `url(${images[index]})`;

    document.querySelectorAll('.thumb').forEach((thumb, i) => {
        thumb.classList.toggle('active', i === index);
    });
}

function prevImage(e) {
    if (e) e.stopPropagation();
    let newIndex = currentImageIndex - 1;
    if (newIndex < 0) newIndex = images.length - 1;
    setImage(newIndex);
}

function nextImage(e) {
    if (e) e.stopPropagation();
    let newIndex = currentImageIndex + 1;
    if (newIndex >= images.length) newIndex = 0;
    setImage(newIndex);
}

// Modal Logic
function openModal(id) {
    const modal = document.getElementById(id);
    if (modal) modal.style.display = 'flex';
}

function closeModal(id) {
    const modal = document.getElementById(id);
    if (modal) modal.style.display = 'none';
}

// Close modal on outside click
window.onclick = function (event) {
    if (event.target.classList.contains('modal-overlay')) {
        event.target.style.display = "none";
    }
}
