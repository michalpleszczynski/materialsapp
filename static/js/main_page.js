function set_active_link(selector){
    $('#menu a').removeClass('active');
    $(selector).addClass('active');
}

$(window).scroll(function() {
    if($(window).scrollTop() + $(window).height() > 0.75*$(document).height()) {
        $('#bottom_box').removeClass('transparent');
    } else if ($(window).scrollTop() + $(window).height() <= 0.75*$(document).height()) {
        $('#bottom_box').addClass('transparent');
    }
});