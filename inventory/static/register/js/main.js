(function ($) {
	$(".toggle-password").click(function () {
		var input = $($(this).attr("toggle"));
		if (input.attr("type") == "password") {
        input.attr("type", "text");
        $(this).removeClass("zmdi-eye-off").addClass("zmdi-eye");
		} else {
        input.attr("type", "password");
        $(this).removeClass("zmdi-eye").addClass("zmdi-eye-off");
		}
	});
})(jQuery);
