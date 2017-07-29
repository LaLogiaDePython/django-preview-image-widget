$(document).on('mouseenter', '#preview', function(e) {
    $(this).find('a').fadeIn();
});

$(document).on('mouseleave', '#preview', function(e) {
    $(this).find('a').fadeOut();
});

$(document).on('click', '#file-select', function(e) {
    e.preventDefault();
    $("[preview_image_widget]").click();
});

$(document).on('change', '[preview_image_widget]', function(e) {
    var file = (this.files[0].name).toString();
    var reader = new FileReader();
    
    $('#file-info').text('');
    $('#file-info').text(file);
    
     reader.onload = function (e) {
         $('#preview img').attr('src', e.target.result);
     };
     
     reader.readAsDataURL(this.files[0]);
});

$(document).ready(function(){
    var $ImageWidget = $("[preview_image_widget]");
    var preview = $ImageWidget.attr("data-preview");
    if(typeof preview != "undefined"){
        var img = preview;
    } else {
        var img = "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNzEiIGhlaWdodD0iMTgwIj48cmVjdCB3aWR0aD0iMTcxIiBoZWlnaHQ9IjE4MCIgZmlsbD0iI2VlZSI+PC9yZWN0Pjx0ZXh0IHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9Ijg1LjUiIHk9IjkwIiBzdHlsZT0iZmlsbDojYWFhO2ZvbnQtd2VpZ2h0OmJvbGQ7Zm9udC1zaXplOjEycHg7Zm9udC1mYW1pbHk6QXJpYWwsSGVsdmV0aWNhLHNhbnMtc2VyaWY7ZG9taW5hbnQtYmFzZWxpbmU6Y2VudHJhbCI+MTcxeDE4MDwvdGV4dD48L3N2Zz4=";
    }
    var html = '<div id="preview" class="thumbnail"><a href="#" id="file-select" class="btn btn-raised btn-primary">Elegir imagen</a>'+
        '<img src="'+ img +'"/>';
    $ImageWidget.before(html);
});
