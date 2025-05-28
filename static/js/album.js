/** Function to execute when document is fully loaded and DOM is in place */
$(document).ready(function(){

    // Get the delete modal
    const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));

    // Hide forms form
    $("#addPhotoContainer").hide();
    $("#editAlbumContainer").hide();
 
    // Create event handler to show add photo form
    $("#showAddPhotoButton").click(function(){
        $("#addPhotoContainer").show(); 
        $("#memberButtons").hide();
    });

    // Create event handler to show edit album form
    $("#showEditButton").click(function(){
        $("#memberButtons").hide();
        $("#editAlbumContainer").show(); 
    });

 // Create event handler for Cancel button for add photo
    $("#cancelAddPhotoButton").click(function(event){
        $("#memberButtons").show();
        $("#addPhotoContainer").hide();
    });

    // Create event handler for Cancel button for edit form
    $("#cancelEditAlbumButton").click(function(event){
        $("#memberButtons").show();
        $("#editAlbumContainer").hide();
    });

    // Create event handler for delete button
    $("#deleteAlbumButton").click(function(){
        deleteModal.show();
    });

})