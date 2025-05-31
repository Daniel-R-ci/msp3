$(document).ready(function () {

    const editButtons = document.getElementsByClassName("btn-edit");
    const commentText = document.getElementById("id_comment");
    const commentForm = document.getElementById("commentForm");
    const submitButton = document.getElementById("submitButton");

    const deleteButtons = document.getElementsByClassName("btn-delete");
    const deleteCommentConfirm = document.getElementById("deleteCommentConfirm");
    const deletePhotoConfirm = document.getElementById("deletePhotoConfirm");

    const deleteCommentModal = new bootstrap.Modal(document.getElementById("deleteCommentModal"));
    const deletePhotoModal = new bootstrap.Modal(document.getElementById("deletePhotoModal"));
    
    /**
    * Initializes edit functionality for the provided edit buttons.
    * Code taken from Code Institute I think terefore I blog code along project
    * Modified to suit 
    */
    for (let button of editButtons) {
        button.addEventListener("click", (e) => {
            let commentId = e.target.getAttribute("data-comment_id");
            let photoId = e.target.getAttribute("data-photo_id");
            let commentContent = document.getElementById(`comment${commentId}`).innerText;

            commentText.value = commentContent;
            submitButton.innerText = "Update";

            commentForm.setAttribute("action", `${photoId}/edit_comment/${commentId}`);
        });
    }

    /**
    * Initializes deletion functionality for the provided delete buttons.
    * Code taken from Code Institute I think terefore I blog code along project
    * Modified to suit 
    */
    for (let button of deleteButtons) {
        button.addEventListener("click", (e) => {
            let commentId = e.target.getAttribute("data-comment_id");
            let photoId = e.target.getAttribute("data-photo_id");
            document.getElementById("submitButton").getAttribute("data-photo_id");
            deleteCommentConfirm.href = `${photoId}/delete_comment/${commentId}`;
            deleteCommentModal.show();
        });
    }

    //Hide edit form
    $("#editPhotoContainer").hide();

    //Create event handler for edit button
    $("#showEditButton").click(function(){
        $("#memberButtons").hide();
        $("#editPhotoContainer").show();
    });

    //Create event handler for cancel button
    $("#cancelEditPhotoButton").click(function (){
        $("#editPhotoContainer").hide();
        $("#memberButtons").show();
    });

    // Create event handler for delete button
    $("#deletePhotoButton").click(function(){
        deletePhotoModal.show();
    });

});