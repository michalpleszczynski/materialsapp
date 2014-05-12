function ajaxifyLinks(){
    // Capture all the links to push their url to the history stack and trigger the StateChange Event
    $('a').click(function(evt) {
        evt.preventDefault();
        History.pushState(null, $(this).text(), $(this).attr('href'));
    });
}

function setActiveLink(selector){
    $('#menu a').removeClass('active');
    if (selector){
        $(selector).addClass('active');
    }
}

$(window).scroll(function() {
    var position = $(window).height() - $(window).scrollTop();
    if(position > 0.75*$(document).height()) {
        $('#bottom_box').addClass('transparent');
    } else if (position <= 0.75*$(document).height()) {
        $('#bottom_box').removeClass('transparent');
    }
});