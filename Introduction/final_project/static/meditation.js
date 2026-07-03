document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("comment-form");
  const list = document.getElementById("comment-list");

  // Profile lists
  const myCommentsList = document.querySelector("#user_comments ul");
  const likedCommentsList = document.querySelector("#user_comments_liked ul");

  // Handle new comment submission (index only)
  if (form) {
    form.addEventListener("submit", async (e) => {
      e.preventDefault();
      const submitBtn = form.querySelector("button[type='submit']");
      submitBtn.disabled = true;

      const formData = new FormData(form);
      const response = await fetch("/add_comment", { method: "POST", body: formData });
      const data = await response.json();

      if (data.success) {
        const li = document.createElement("li");
        li.innerHTML = `
          <strong>${data.username}</strong>: ${data.content}
          <small>${data.created_at}</small>
          <div class="reactions">
            <button class="like-btn ${data.user_reaction === 'like' ? 'active-like' : ''}" data-id="${data.id}">👍 ${data.likes}</button>
            <button class="dislike-btn ${data.user_reaction === 'dislike' ? 'active-dislike' : ''}" data-id="${data.id}">👎 ${data.dislikes}</button>
            ${data.owned ? `<button class="delete-btn" data-id="${data.id}">🗑 Delete</button>` : ""}
          </div>
        `;
        list.insertBefore(li, list.firstChild);
        form.reset();
      } else {
        alert(data.error || "Error posting comment");
      }

      submitBtn.disabled = false;
    });
  }

  // Reusable handler for delete + like/dislike
  function attachReactions(container) {
    if (!container) return;

    container.addEventListener("click", async (e) => {
      // Delete
      if (e.target.classList.contains("delete-btn")) {
        const commentId = e.target.dataset.id;
        if (!confirm("Are you sure you want to delete this comment?")) return;

        const response = await fetch("/delete_comment", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ comment_id: commentId })
        });
        const data = await response.json();
        if (data.success) {
          e.target.closest("li").remove();
        } else {
          alert(data.error || "Error deleting comment");
        }
      }

      // Like/Dislike
      if (e.target.classList.contains("like-btn") || e.target.classList.contains("dislike-btn")) {
        const commentId = e.target.dataset.id;
        const action = e.target.classList.contains("like-btn") ? "like" : "dislike";

        const response = await fetch("/react_comment", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ comment_id: commentId, action })
        });
        const data = await response.json();

        if (data.success) {
          const li = e.target.closest("li");
          const likeBtn = li.querySelector(".like-btn");
          const dislikeBtn = li.querySelector(".dislike-btn");

          likeBtn.textContent = `👍 ${data.likes}`;
          dislikeBtn.textContent = `👎 ${data.dislikes}`;

          likeBtn.classList.remove("active-like");
          dislikeBtn.classList.remove("active-dislike");

          if (data.user_reaction === "like") {
            likeBtn.classList.add("active-like");
          } else if (data.user_reaction === "dislike") {
            dislikeBtn.classList.add("active-dislike");
          }
        } else {
          alert(data.error || "Error reacting to comment");
        }
      }
    });
  }

  // Attach to all lists
  attachReactions(list);              // index page
  attachReactions(myCommentsList);    // profile: my comments
  attachReactions(likedCommentsList); // profile: liked comments
});
