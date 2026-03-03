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

// Manufacturing Process Dynamic Steps
const processSteps = [
    {
        pill: "Step 1/8: Raw Material",
        title: "High-Grade Raw Material Selection",
        desc: "Vacuum sizing tanks ensure precise outer diameter while internal pressure maintains perfect roundness and wall thickness uniformity.",
        features: [
            "PE100 grade material",
            "Optimal molecular weight distribution"
        ],
        images: [
            "https://images.unsplash.com/photo-1544551763-46a0121087dd?auto=format&fit=crop&q=80&w=600",
            "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?auto=format&fit=crop&q=80&w=600"
        ]
    },
    {
        pill: "Step 2/8: Extrusion",
        title: "Precision Extrusion Technology",
        desc: "State-of-the-art extruders melt and homogenize the HDPE resin. Advanced screw design ensures optimal melt temperature and pressure control.",
        features: [
            "Computer-controlled heating zones",
            "Continuous melt filtration"
        ],
        images: [
            "https://images.unsplash.com/photo-1544551763-46a0121087dd?auto=format&fit=crop&q=80&w=600"
        ]
    },
    {
        pill: "Step 3/8: Cooling",
        title: "Controlled Cooling Systems",
        desc: "Multi-stage water cooling baths utilize precise temperature gradients to ensure uniform cooling, preventing internal stresses and material deformation.",
        features: [
            "Multi-zone temperature regulation",
            "High-efficiency heat exchange"
        ],
        images: [
            "https://images.unsplash.com/photo-1544551763-46a0121087dd?auto=format&fit=crop&q=80&w=600"
        ]
    },
    {
        pill: "Step 4/8: Sizing",
        title: "Accurate Sizing & Calibration",
        desc: "Automated vacuum calibration sleeves strictly control the outer dimensions of the pipe, ensuring compliance with international standard tolerances.",
        features: [
            "Laser diameter measurement",
            "Real-time ultrasonic wall thickness scanning"
        ],
        images: [
            "https://images.unsplash.com/photo-1544551763-46a0121087dd?auto=format&fit=crop&q=80&w=600"
        ]
    },
    {
        pill: "Step 5/8: Quality Control",
        title: "Rigorous Quality Control",
        desc: "Every batch undergoes hydrostatic pressure testing, tensile strength evaluation, and melt flow index verification in our certified laboratory.",
        features: [
            "ISO 4427 compliance testing",
            "Continuous inline monitoring"
        ],
        images: [
            "https://images.unsplash.com/photo-1544551763-46a0121087dd?auto=format&fit=crop&q=80&w=600"
        ]
    },
    {
        pill: "Step 6/8: Marking",
        title: "Laser Precision Marking",
        desc: "Automated inline printing applies permanent, high-contrast identification markings including standards, pressure ratings, and traceability codes.",
        features: [
            "Non-fading inkjet & thermal printing",
            "Meter-by-meter length marking"
        ],
        images: [
            "https://images.unsplash.com/photo-1544551763-46a0121087dd?auto=format&fit=crop&q=80&w=600"
        ]
    },
    {
        pill: "Step 7/8: Cutting",
        title: "Automated Clean Cutting",
        desc: "Planetary cutting saws seamlessly separate the continuous pipe into exact lengths without creating chips or rough edges, preparing the pipe for insertion.",
        features: [
            "Dust-free swarfless cutting",
            "Programmable length accuracy"
        ],
        images: [
            "https://images.unsplash.com/photo-1544551763-46a0121087dd?auto=format&fit=crop&q=80&w=600"
        ]
    },
    {
        pill: "Step 8/8: Packaging",
        title: "Secure Packaging & Logistics",
        desc: "Straight pipes are bundled with timber supports while smaller diameters are tightly coiled and strapped, ready for secure container shipment globally.",
        features: [
            "UV-protective wrapping options",
            "Custom coil lengths available"
        ],
        images: [
            "https://images.unsplash.com/photo-1544551763-46a0121087dd?auto=format&fit=crop&q=80&w=600"
        ]
    }
];

let currentProcessStep = 0;
let currentInnerImageIndex = 0;

function updateProcessDOM() {
    console.log("Updating Process DOM for step:", currentProcessStep);
    const data = processSteps[currentProcessStep];
    if (!data) return;

    // Update Title and Desc
    const titleEl = document.getElementById('processTitle');
    const descEl = document.getElementById('processDesc');
    if (titleEl) titleEl.textContent = data.title;
    if (descEl) descEl.textContent = data.desc;

    // Update Features List
    const featureList = document.getElementById('processFeatures');
    if (featureList) {
        featureList.innerHTML = '';
        data.features.forEach(feat => {
            featureList.innerHTML += `
                <li>
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" stroke="none"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/></svg>
                    ${feat}
                </li>
            `;
        });
    }

    // Update Image with transition
    const imgEl = document.getElementById('processImg');
    if (imgEl) {
        imgEl.style.opacity = 0;
        setTimeout(() => {
            imgEl.src = data.images[currentInnerImageIndex % data.images.length];
            imgEl.style.opacity = 1;
        }, 150);
    }

    // Update Desktop Tabs highlighting
    const tabs = document.querySelectorAll('.process-tab');
    tabs.forEach((tab, index) => {
        if (index === currentProcessStep) {
            tab.classList.add('active');
        } else {
            tab.classList.remove('active');
        }
    });

    // Update Mobile pill text
    const mobileIndicator = document.getElementById('mobileStepText');
    if (mobileIndicator) {
        mobileIndicator.textContent = data.pill;
    }
}

function changeProcessStep(direction) {
    currentProcessStep += direction;
    if (currentProcessStep < 0) currentProcessStep = processSteps.length - 1;
    if (currentProcessStep >= processSteps.length) currentProcessStep = 0;
    currentInnerImageIndex = 0; // Reset image index on step change
    updateProcessDOM();
}

function setProcessStep(index) {
    if (currentProcessStep === index) return;
    currentProcessStep = index;
    currentInnerImageIndex = 0;
    updateProcessDOM();
}

// Support for inner carousel image switching
function changeInnerProcessImage(direction, event) {
    if (event) event.stopPropagation();
    const data = processSteps[currentProcessStep];
    currentInnerImageIndex += direction;
    if (currentInnerImageIndex < 0) currentInnerImageIndex = data.images.length - 1;
    if (currentInnerImageIndex >= data.images.length) currentInnerImageIndex = 0;

    const imgEl = document.getElementById('processImg');
    if (imgEl) {
        imgEl.style.opacity = 0.5;
        setTimeout(() => {
            imgEl.src = data.images[currentInnerImageIndex];
            imgEl.style.opacity = 1;
        }, 100);
    }
}

// Initial setup after load
window.addEventListener('load', () => {
    // Add event listeners for the tabs as a fallback for the onclick attribute
    const tabs = document.querySelectorAll('.process-tab');
    tabs.forEach((tab, index) => {
        tab.addEventListener('click', () => {
            setProcessStep(index);
        });
    });

    // Ensure image has transition
    const imgEl = document.getElementById('processImg');
    if (imgEl) {
        imgEl.style.transition = 'opacity 0.2s ease';
    }
});
