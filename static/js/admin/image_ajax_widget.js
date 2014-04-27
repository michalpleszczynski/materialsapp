function get_image(id){
    Dajaxice.core.get_image(Dajax.process, {'id':id});
}

// dismissAddAnotherPopup is a function from Django's RelatedObjectLookups.js
// this wraps this function, executes it and after triggers change event on a select element
dismissAddAnotherPopup = (function() {
    var func = dismissAddAnotherPopup;

    return function() {
        // execute wrapped function
        func.apply(this, arguments);
        // find the select element
        var name = windowname_to_id(arguments[0].name);
        var elem = document.getElementById(name);
        // trigger change event
        elem.onchange();
    };
}());