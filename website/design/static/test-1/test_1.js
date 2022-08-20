const $backTop = $(".back-to-top");
const isHidden = "is-hidden";

AOS.init({
  offset: 200,
  delay: 50,
  once: true
});

/*$('a[data-toggle="pill"]').on("shown.bs.tab", e => {
  AOS.refresh();
});*/

$(window).on("scroll", function() {
  const $this = $(this);
  if ($this.scrollTop() + $this.height() == $(document).height()) {
    $backTop.removeClass(isHidden);
  } else {
    $backTop.addClass(isHidden);
  }
});

$backTop.on("click", () => {
  $("html, body").animate({ scrollTop: 0 }, "slow");
  return false;
});
