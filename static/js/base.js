function toggleAnswer(faqId) {
    let answer = document.getElementById(faqId);
    let icon = event.target; // Targeting the 'i' element directly

    if (answer.style.display === "none") {
        answer.style.display = "block";
        icon.classList.remove("fa-plus");
        icon.classList.add("fa-minus");
    } else {
        answer.style.display = "none";
        icon.classList.remove("fa-minus");
        icon.classList.add("fa-plus");
    }
}



function toggleFAQs() {
    let faqItems = document.querySelectorAll('.faq-item');
    let shownFAQs = Array.from(faqItems).filter(faq => faq.style.display !== 'none').length;

    if (shownFAQs <= 4) {
        faqItems.forEach(faq => {
            faq.style.display = 'block';
        });
        document.getElementById('viewMoreBtn').innerText = 'VIEW LESS';
    } else {
        for (let i = 4; i < faqItems.length; i++) {
            faqItems[i].style.display = 'none';
        }
        document.getElementById('viewMoreBtn').innerText = 'VIEW MORE';
    }
}
