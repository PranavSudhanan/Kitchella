$(document).ready(function() {
    var dialogAbout = $('<div></div>')
        .html("<p><b>Welcome to our eCommerce Project for INFSCI-2710!</b><br><br>We're going to insert some sort of generic introduction blurb here for people loading the site for the first time! Maybe, I actually don't know!</p>")
        .dialog({
            modal: true,
            title: 'eCommerce Intro',
            width: 500,
			create: function(event, ui) {
				$(event.target).parent().find('.ui-dialog-titlebar-close').addClass('btn-danger').addClass('btn').addClass('pt-1');
			}
        });
});