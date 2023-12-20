// Display search bar when the search icon is clicked
jQuery(document).ready(function () {
    jQuery("#searchIcon").click(function () {
        jQuery("#searchIconForm").toggleClass("d-none");
        jQuery("#searchInput").focus();
    });
    jQuery("#searchInput").click(function (event) {
        event.stopPropagation();
    });
});


// Function to handle toggle in faq page
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

// function products
$('.btt-link').click(function (e) {
    window.scrollTo(0, 0);
});

$('#sort-selector').change(function () {
    var selector = $(this);
    var currentUrl = new URL(window.location);

    var selectedVal = selector.val();
    if (selectedVal != "reset") {
        var sort = selectedVal.split("_")[0];
        var direction = selectedVal.split("_")[1];

        currentUrl.searchParams.set("sort", sort);
        currentUrl.searchParams.set("direction", direction);

        window.location.replace(currentUrl);
    } else {
        currentUrl.searchParams.delete("sort");
        currentUrl.searchParams.delete("direction");

        window.location.replace(currentUrl);
    }
});
