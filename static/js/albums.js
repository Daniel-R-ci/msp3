/** Function to execute when document is fully loaded and DOM is in place */
$(document).ready(function(){
    
    //Hide create new album form
    $("#createAlbumContainer").hide();
    $("#ownAlbumsContainer").hide();

    //Create event handler to show form
    $("#showFormButton").click(function(){
        $("#createAlbumContainer").show();
        $("#memberButtons").hide();
        $("#ownAlbumsContainer").hide();
    });

    //Create event handler for Cancel button
    $("#cancelCreateButton").click(function(){
        $("#memberButtons").show();
        $("#id_name").val(" "); //Field won't close if it is empty

        $("#createAlbumContainer").hide();
    });

    //Create event handler for View your albums button
    $("#showOwnAlbumsButton").click(function(){
        $("#ownAlbumsContainer").toggle();
    });
     

});