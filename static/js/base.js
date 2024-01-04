/*global jQuery, window, document, URL, $, event */

jQuery(document).ready(function () {
    jQuery("#searchIcon").click(function () {
        jQuery("#searchIconForm").toggleClass("d-none");
        jQuery("#searchInput").focus();
    });
    jQuery("#searchInput").click(function (e) {
        e.stopPropagation();
    });
});

function toggleAnswer(faqId, e) {
    var answer = document.getElementById(faqId);
    var icon = e.target; // Targeting the 'i' element directly

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
    var faqItems = document.querySelectorAll(".faq-item");
    var shownFAQs = Array.from(faqItems).filter(function (faq) {
        return faq.style.display !== "none";
    }).length;

    if (shownFAQs <= 4) {
        faqItems.forEach(function (faq) {
            faq.style.display = "block";
        });
        document.getElementById("viewMoreBtn").innerText = "VIEW LESS";
    } else {
        Array.from(faqItems).slice(4).forEach(function (faq) {
            faq.style.display = "none";
        });
        document.getElementById("viewMoreBtn").innerText = "VIEW MORE";
    }
}

