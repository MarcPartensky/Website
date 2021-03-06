/**
* Template Name: Knight - v2.1.0
* Template URL: https://bootstrapmade.com/knight-free-bootstrap-theme/
* Author: BootstrapMade.com
* License: https://bootstrapmade.com/license/
*/

// Init AOS
function aos_init() {
	AOS.init({
		duration: 600,
		once: true
	});
}

function main($) {
	"use strict";

	console.log('start main.js');

	// Smooth scroll for the navigation menu and links with .scrollto classes
	var scrolltoOffset = $('#header').outerHeight() - 1;
	$(document).on('click', '.nav-menu a, .mobile-nav a, .scrollto', function(e) {
		if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
			var target = $(this.hash);
			if (target.length) {
				e.preventDefault();

				var scrollto = target.offset().top - scrolltoOffset;

				if ($(this).attr("href") == '#header') {
					scrollto = 0;
				}

				$('html, body').animate({
					scrollTop: scrollto
				}, 1500, 'easeInOutExpo');

				if ($(this).parents('.nav-menu, .mobile-nav').length) {
					$('.nav-menu .active, .mobile-nav .active').removeClass('active');
					$(this).closest('li').addClass('active');
				}

				if ($('body').hasClass('mobile-nav-active')) {
					$('body').removeClass('mobile-nav-active');
					$('.mobile-nav-toggle i').toggleClass('icofont-navigation-menu icofont-close');
					$('.mobile-nav-overly').fadeOut();
				}
				return false;
			}
		}
	});

	// Activate smooth scroll on page load with hash links in the url
	$(document).ready(function() {
		if (window.location.hash) {
			var initial_nav = window.location.hash;
			if ($(initial_nav).length) {
				var scrollto = $(initial_nav).offset().top - scrolltoOffset;
				$('html, body').animate({
					scrollTop: scrollto
				}, 1500, 'easeInOutExpo');
			}
		}
	});


	// Mobile Navigation
	if ($('.nav-menu').length) {
		var $mobile_nav = $('.nav-menu').clone().prop({
			class: 'mobile-nav d-lg-none'
		});
		$('body').append($mobile_nav);
		$('.mobile-nav .nav-logo').remove();
		$('body').prepend('<button type="button" class="mobile-nav-toggle d-lg-none"><i class="icofont-navigation-menu"></i></button>');
		$('body').append('<div class="mobile-nav-overly"></div>');

		$(document).on('click', '.mobile-nav-toggle', function(e) {
			$('body').toggleClass('mobile-nav-active');
			$('.mobile-nav-toggle i').toggleClass('icofont-navigation-menu icofont-close');
			$('.mobile-nav-overly').toggle();
		});

		$(document).on('click', '.mobile-nav .drop-down > a', function(e) {
			e.preventDefault();
			$(this).next().slideToggle(300);
			$(this).parent().toggleClass('active');
		});

		$(document).click(function(e) {
			var container = $(".mobile-nav, .mobile-nav-toggle");
			if (!container.is(e.target) && container.has(e.target).length === 0) {
				if ($('body').hasClass('mobile-nav-active')) {
					$('body').removeClass('mobile-nav-active');
					$('.mobile-nav-toggle i').toggleClass('icofont-navigation-menu icofont-close');
					$('.mobile-nav-overly').fadeOut();
				}
			}
		});
	} else if ($(".mobile-nav, .mobile-nav-toggle").length) {
		$(".mobile-nav, .mobile-nav-toggle").hide();
	}

	// Navigation active state on scroll
	var nav_sections = $('section');
	var main_nav = $('.nav-menu, .mobile-nav');

	$(window).on('scroll', function() {
		var cur_pos = $(this).scrollTop() + 200;

		nav_sections.each(function() {
			var top = $(this).offset().top,
				bottom = top + $(this).outerHeight();

			if (cur_pos >= top && cur_pos <= bottom) {
				if (cur_pos <= bottom) {
					main_nav.find('li').removeClass('active');
				}
				main_nav.find('a[href="#' + $(this).attr('id') + '"]').parent('li').addClass('active');
			}
			if (cur_pos < 300) {
				$(".nav-menu ul:first li:first").addClass('active');
			}
		});
	});

	// Stick the header at top on scroll
	$("#header").sticky({
		topSpacing: 0,
		zIndex: '50'
	});

	// Back to top button
	$(window).scroll(function() {
		if ($(this).scrollTop() > 100) {
			$('.back-to-top').fadeIn('slow');
		} else {
			$('.back-to-top').fadeOut('slow');
		}
	});

	$('.back-to-top').click(function() {
		$('html, body').animate({
			scrollTop: 0
		}, 1500, 'easeInOutExpo');
		return false;
	});

	// Porfolio isotope and filter
	$(window).on('load', function() {
		var portfolioIsotope = $('.portfolio-container').isotope({
			itemSelector: '.portfolio-item',
			layoutMode: 'fitRows'
		});

		$('#portfolio-flters li').on('click', function() {
			$("#portfolio-flters li").removeClass('filter-active');
			$(this).addClass('filter-active');

			portfolioIsotope.isotope({
				filter: $(this).data('filter')
			});
			aos_init();
		});

		// Initiate venobox (lightbox feature used in portofilo)
		$(document).ready(function() {
			$('.venobox').venobox();
		});
	});

	// Testimonials carousel (uses the Owl Carousel library)
	$(".testimonials-carousel").owlCarousel({
		autoplay: true,
		dots: true,
		loop: true,
		items: 1
	});

	// Portfolio details carousel
	$(".portfolio-details-carousel").owlCarousel({
		autoplay: true,
		dots: true,
		loop: true,
		items: 1
	});

	// jQuery counterUp
	// $('[data-toggle="counter-up"]').counterUp({
	//   delay: 10,
	//   time: 1000
	// });

	 $('.counter').counterUp({
				delay: 10,
				time: 1000,
				offset: 70,
				beginAt: 100,
				formatter: function (n) {
					return n.replace(/,/g, '.');
				 }
	 })

	// typed class
  if ($('.typed').length) {
    var typed_strings = $(".typed").data('typed-items');
    typed_strings = typed_strings.split(',')
    new Typed('.typed', {
      strings: typed_strings,
      loop: true,
      typeSpeed: 100,
      backSpeed: 50,
      backDelay: 2000
    });
  }


	// const hero = document.getElementById('hero')


	// $(window).load(function() {
	//   var f = document.createElement('iframe');
	//   f.src = url;
	//   f.width = 1000;
	//   f.height = 500;
	//   $('body').append(f);
	// });
//
		// window.onload = function(){
		//   const calendar = document.getElementById('open-web-calendar')
		//   calendar.src = 'https://open-web-calendar.herokuapp.com/calendar.html?url=https%3A%2F%2Fcalendar.google.com%2Fcalendar%2Fical%2Fmarc.partensky%2540gmail.com%2Fpublic%2Fbasic.ics&amp;language=fr'
		//   calendar.style = 'center center no-repeat'
		//   calendar.sandbox = 'allow-scripts allow-same-origin allow-top-navigation'
		//   calendar.allowTransparency = 'true'
		//   calendar.scrolling = 'no'
		//   calendar.frameborder = '0'
		//   calendar.height = '600px'
		//   calendar.width = '100%'
		// };

};

$(document).ready(function() {
/*	$(window).load(function () {
		console.log('load');
	});
	*/
	console.log('ready event');
	main($);
	aos_init();
});
