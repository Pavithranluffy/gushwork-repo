// Selectors
const mainImage =getElementById("mainImage");
const zoomLens = document.getElementById("mainImageContainer");
const zoomResult = document.getElementById("zoomResult");

document.addEventListener("DOMContentLoaded", function() {
    const mainImage = document.getElementById('mainImage');
    const zoomContainer = document.getElementById('mainImageContainer');
    const lens = document.getElementById('zoomLens');
    const result = document.getElementById('zoomResult');

    if (mainImage && zoomContainer && lens && result) {
        // Prepare zoom result background
        result.style.backgroundImage = `url(${mainImage.src})`;
        // Default box size for zoom
        result.style.backgroundSize = `${mainImage.width * 2}px ${mainImage.height * 2}px`;

        zoomContainer.addEventListener("mousemove", moveLens);
        zoomContainer.addEventListener("mouseenter", showLens);
        zoomContainer.addEventListener("mouseleave", hideLens);

        function moveLens(e) {
            e.preventDefault();
            
            // Get position of image
            const { left, top, width, height } = mainImage.getBoundingClientRect();
            
            // Adjust zoom result size
            result.style.backgroundSize = `${width * 2.5}px ${height * 2.5}px`;

            // Calculate cursor X and Y
            let x = e.clientX - left - lens.offsetWidth / 2;
            let y = e.clientY - top - lens.offsetHeight / 2;
            
            // Prevent going out of bounds
            if (x > width - lens.offsetWidth) {
                x = width - lens.offsetWidth;
            } else if (x < 0) {
                x = 0;
            }
            if (y > height - lens.offsetHeight) {
                y = height - lens.offsetHeight;
            } else if (y < 0) {
                y = 0;
            }
            
            // Move lens
            lens.style.left = x + "px";
            lens.style.top = y + "px";
            
            // Move background in result
            let backgroundX = (x / width) * 100;
            let backgroundY = (y / height) * 100;
            
            result.style.backgroundPosition = `${backgroundX}% ${backgroundY}%`;
        }
        
        function showLens() {
            if(window.innerWidth > 1024) {
                lens.style.display = 'block';
                result.style.display = 'block';
                result.style.backgroundImage = `url(${mainImage.src})`; // Fix image
            }
        }
        
        function hideLens() {
            lens.style.display = 'none';
            result.style.display = 'none';
        }
    }

    // FAQ Accordion
    const faqItems = document.querySelectorAll('.faq-item');
    faqItems.forEach(item => {
        item.querySelector('.faq-question').addEventListener('click', () => {
            const isActive = item.classList.contains('active');
            faqItems.forEach(i => {
                i.classList.remove('active');
                i.querySelector('.icon').textContent = '⌄';
            });
            if (!isActive) {
                item.classList.add('active');
                item.querySelector('.icon').textContent = '⌃';
            }
        });
    });

    // Sticky Header Logic
    const stickyHeader = document.getElementById('stickyHeader');
    window.addEventListener('scroll', () => {
        // Show after first fold (assumed around 800px or full screen height)
        if (window.scrollY > 600) {
            stickyHeader.classList.add('show');
        } else {
            stickyHeader.classList.remove('show');
        }
    });

    // Applications carousel swipe/buttons
    const appCarousel = document.getElementById('appCarousel');
    const scrollAmount = 300;
    
    document.querySelector('.prev-app').addEventListener('click', () => {
        appCarousel.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
    });
    document.querySelector('.next-app').addEventListener('click', () => {
        appCarousel.scrollBy({ left: scrollAmount, behavior: 'smooth' });
    });
});

// Gallery Thumbnails
const images = [
    "https://images.unsplash.com/photo-1544551763-46a0121087dd?auto=format&fit=crop&q=80&w=800",
    "https://images.unsplash.com/photo-1504917595217-d4dc5ebe6122?auto=format&fit=crop&q=80&w=800",
    "https://images.unsplash.com/photo-1531265726475-52ad60219627?auto=format&fit=crop&q=80&w=800",
    "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&q=80&w=800",
    "https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&q=80&w=800"
];
let currentImageIndex = 0;

function setImage(index) {
    currentImageIndex = index;
    const mainImgNode = document.getElementById('mainImage');
    mainImgNode.src = images[index];
    
    document.querySelectorAll('.thumb').forEach((thumb, i) => {
        thumb.classList.toggle('active', i === index);
    });
}

function prevImage() {
    let newIndex = currentImageIndex - 1;
    if (newIndex < 0) newIndex = images.length - 1;
    setImage(newIndex);
}

function nextImage() {
    let newIndex = currentImageIndex + 1;
    if (newIndex >= images.length) newIndex = 0;
    setImage(newIndex);
}

// Modal Logic
function openModal(id) {
    document.getElementById(id).style.display = 'flex';
}

function closeModal(id) {
    document.getElementById(id).style.display = 'none';
}

// Close modal on outside click
window.onclick = function(event) {
    if (event.target.classList.contains('modal-overlay')) {
        event.target.style.display = "none";
    }
}
