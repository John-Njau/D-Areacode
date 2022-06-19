$("#post-btn").click(function(event){
    event.preventDefault();
   
    $('.new-post').toggle();
    $('#newpost').trigger('click');
})