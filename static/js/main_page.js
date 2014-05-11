function setActiveLink(selector){
    $('#menu a').removeClass('active');
    $(selector).addClass('active');
}

$(window).scroll(function() {
    var position = $(window).height() - $(window).scrollTop();
    if(position > 0.75*$(document).height()) {
        $('#bottom_box').addClass('transparent');
    } else if (position <= 0.75*$(document).height()) {
        $('#bottom_box').removeClass('transparent');
    }
});