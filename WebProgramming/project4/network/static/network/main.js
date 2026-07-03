document.addEventListener("DOMContentLoaded", () => {
    // Edit buttons
    document.querySelectorAll(".edit-button-class").forEach(button => {
        button.addEventListener("click", () => {
            const postId = button.dataset.postId;
            showForm(postId);
        });
    });

    // Cancel buttons
    document.querySelectorAll(".cancel-button-class").forEach(button => {
        button.addEventListener("click", () => {
            const postId = button.dataset.postId;
            hideForm(postId);
        });
    });

    // Save buttons (form submission)
    document.querySelectorAll(".save-button-class").forEach(button => {
        button.addEventListener("click", (event) => {
            event.preventDefault(); // prevent normal form submit
            const postId = button.dataset.postId;
            postForm(postId);
        });
    });
});

// Show form
function showForm(postId) {
    document.getElementById(`edit-form-${postId}`).classList.remove("d-none");
}

// Hide form
function hideForm(postId) {
    document.getElementById(`edit-form-${postId}`).classList.add("d-none");
}

// Submit form via fetch
function postForm(postId) {
    const form = document.getElementById(`edit-form-${postId}`);
    const formData = new FormData(form);

    fetch(form.action, {
        method: "POST",
        body: formData,
        headers: {
            "X-CSRFToken": form.querySelector("[name=csrfmiddlewaretoken]").value
        }
    })
    .then(response => response.json())
    .then(data => {
        console.log("Updated:", data);
        hideForm(postId);
        // Optionally update DOM with new content
    })
    .catch(error => console.error("Error:", error));
}
