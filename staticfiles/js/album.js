/** Function to execute when document is fully loaded and DOM is in place */
$(document).ready(function(){

    // Get the delete modal
    const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));

    // Hide edit form
    $("#editAlbumContainer").hide();

    // Create event handler to show form
    $("#showFormButton").click(function(){
        $("#editAlbumContainer").show(); 
        $("#showFormButton").hide();
        $("#deleteAlbumButton").hide();
        albumName = document.getElementById("albumName").innerHTML
        albumDescription = document.getElementById("albumDescription").innerHTML
        $("#id_name").val(albumName);
        $("#id_description").val(albumDescription);
    })

    // Create event handler for Cancel button
    $("#cancelEditButton").click(function(){
        $("showFormButton").show();
        $("deleteAlbumButton").show();
        $("#editAlbumContainer").hide();
    })

    // Create event handler for delete button
    $("#deleteAlbumButton").click(function(){
        deleteModal.show();
    })

})