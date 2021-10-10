(function ($) {
    /*--/ Star Counter /--*/

    // Begin jQuery
    $(function () {
      
        // DOM ready
        // If a link has a dropdown, add sub menu toggle.
        $("nav ul li").hover(function (e) {
            var isHovered = $(this).is(":hover");
            if (isHovered) {
                $(this).children("ul").stop().slideDown(300);
            } else {
                $(this).children("ul").stop().slideUp(300);
            }
            e.stopPropagation();
        });
        // Clicking away from dropdown will remove the dropdown class
        $("html").click(function () {
            $(".nav-dropdown").hide();
        });
        // Toggle open and close nav styles on click
        $("#nav-toggle").click(function () {
            $("nav ul").slideToggle();
        });

        $("nav ul li > a").on("click", function () {
            $(this).parent().find("ul").first().toggle(300);

            $(this).parent().siblings().find("ul").hide(200);

            //Hide menu when clicked outside
        });

        // Hamburger to X toggle
        $("#nav-toggle").on("click", function () {
            this.classList.toggle("active");
        });
    }); // end DOM ready
})(jQuery); // end jQuery
