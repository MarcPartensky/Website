function dontReloadOnFormSubmit() {
	const forms = document.forms;
	const url = `/notified-mail-form`
	console.log(forms)
	for (let form of forms) {
		console.log(form)

		$(form).submit(function(event) {
			console.log('Sending:')
			console.log($(form))
			console.log(url)
			const data = $(form).serialize()
			console.log(data)
			$.ajax({
				type: "POST",
				url: url,
				data: data,
				// success: function(ev) {
				// 	$('#main-modal').modal('toggle')
				// },
				// error: function(ev) {
				// 	$('#main-modal').modal('toggle')
				// }
				statusCode: {
					200: function(value) {
						$('#main-modal').modal('toggle')
						$('.modal-content').addClass('alert')
						$('.modal-content').addClass('alert-success')
						$('#main-modal-title').first()[0].firstChild.data = "Success!"
						$('#main-modal-body').first()[0].firstChild.data = value.responseText
						console.log(value)
					},
					403: function(value) {
						$('#main-modal').modal('toggle')
						$('.modal-content').addClass('alert')
						$('.modal-content').addClass('alert-danger')
						$('#main-modal-title').first()[0].firstChild.data = "Forbidden!"
						$('#main-modal-body').first()[0].firstChild.data = value.responseText
						console.log(value)
					},
					500: function(value) {
						$('#main-modal').modal('toggle')
						$('.modal-content').addClass('alert')
						$('.modal-content').addClass('alert-danger')
						$('#main-modal-title').first()[0].firstChild.data = "Error"
						$('#main-modal-body').first()[0].firstChild.data = value.responseText
						console.log(value)
					}
				}
			})
			return false
		}.bind(form, url))
	}
}

// toggle the theme
function toggleTheme() {
	var el = document.getElementById("theme");
	console.log('theme:', el)
	if (el.href.match(CSS_THEME_LIGHT)) {
		el.href = CSS_THEME_DARK;
	} else {
		el.href = CSS_THEME_LIGHT;
	}
}

function main() {
	dontReloadOnFormSubmit()

	VANTA.NET({
		el: "#footer",
		mouseControls: true,
		touchControls: true,
		gyroControls: false,
		minHeight: 200.00,
		minWidth: 200.00,
		scale: 1.00,
		scaleMobile: 1.00,
		color: 0x770000,
		backgroundColor: 0x0,
		points: 10.00
	})
}

$(document).ready(main)
