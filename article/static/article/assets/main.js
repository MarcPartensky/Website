$(".sidebar-header-1 a, .nav-list a").on("click", function (e) {
    e.preventDefault();
    const href = $(this).attr("href").replace('#', '');
    const element = document.getElementById(href)
    const margin = 20;
    $("html, body").animate({ scrollTop: $(element).offset().top-margin }, 1500);
});

