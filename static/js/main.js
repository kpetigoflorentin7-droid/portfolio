// Menu mobile
const burger = document.getElementById('burger');
const navLinks = document.querySelector('.nav-links');
if (burger) {
    burger.addEventListener('click', () => {
        navLinks.classList.toggle('open');
        burger.classList.toggle('active');
    });
    document.querySelectorAll('.nav-links a').forEach(link => {
        link.addEventListener('click', () => {
            navLinks.classList.remove('open');
            burger.classList.remove('active');
        });
    });
}

// Navbar au scroll
const navbar = document.getElementById('navbar');
const scrollTop = document.getElementById('scrollTop');
window.addEventListener('scroll', () => {
    if (window.scrollY > 40) {
        navbar.classList.add('scrolled');
        scrollTop.classList.add('visible');
    } else {
        navbar.classList.remove('scrolled');
        scrollTop.classList.remove('visible');
    }
});

// Animations au scroll (reveal)
const revealEls = document.querySelectorAll('.reveal');
const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            revealObserver.unobserve(entry.target);
        }
    });
}, { threshold: 0.15 });
revealEls.forEach(el => revealObserver.observe(el));

// Barres de compétences animées
const skillBars = document.querySelectorAll('.skill-fill');
const skillObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const el = entry.target;
            el.style.width = el.dataset.width + '%';
            skillObserver.unobserve(el);
        }
    });
}, { threshold: 0.3 });
skillBars.forEach(el => skillObserver.observe(el));

// Effet machine à écrire sur le titre du hero
const typedEl = document.querySelector('.typed');
if (typedEl) {
    const text = typedEl.dataset.text;
    let i = 0;
    typedEl.textContent = '';
    function typeWriter() {
        if (i < text.length) {
            typedEl.textContent += text.charAt(i);
            i++;
            setTimeout(typeWriter, 40);
        }
    }
    setTimeout(typeWriter, 600);
}

// Glow qui suit la souris dans le hero (subtil, desktop uniquement)
const glow = document.getElementById('cursorGlow');
if (glow && window.matchMedia('(pointer: fine)').matches) {
    document.addEventListener('mousemove', (e) => {
        glow.style.transform = `translate(${e.clientX - 150}px, ${e.clientY - 150}px)`;
    });
}