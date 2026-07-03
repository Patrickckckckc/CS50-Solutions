document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email(originalEmail = null) {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';
  document.querySelector('#mail-view').style.display = 'none';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';

  // If called with an email, pre-fill fields
  if (originalEmail) {
    // Recipient
    document.querySelector('#compose-recipients').value = originalEmail.sender;

    // Subject
    let subject = originalEmail.subject.startsWith("Re:")
      ? originalEmail.subject
      : `Re: ${originalEmail.subject}`;
    document.querySelector('#compose-subject').value = subject;

    // Body
    document.querySelector('#compose-body').value =
      `On ${originalEmail.timestamp} ${originalEmail.sender} wrote:\n${originalEmail.body}\n\n`;
  }

   // Handle form submission
  document.querySelector('#compose-form').onsubmit = function(event) {
    event.preventDefault(); // stop default GET submission

    fetch('/emails', {
      method: 'POST',
      body: JSON.stringify({
        recipients: document.querySelector('#compose-recipients').value,
        subject: document.querySelector('#compose-subject').value,
        body: document.querySelector('#compose-body').value
      })
    })
    .then(response => response.json())
    .then(result => {
      console.log(result);
      load_mailbox('sent'); // Redirect to Sent mailbox after sending email
    })
    .catch(error => {
      console.error('Error:', error);
    });
  };
}

function load_mailbox(mailbox) {

  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector('#mail-view').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

  // Show the Mailbox
  fetch(`/emails/${mailbox}`)
    .then(response => response.json())
    .then(emails => {
      // Sort emails by timestamp (newest first)
      emails.sort((a, b) => new Date(b.timestamp) - new Date(a.timestamp));

      // Print emails
      console.log(emails);

      // Add each email into the HTML page
      for (let i = 0; i < emails.length; i++) {
        const container = document.getElementById('emails-view');

        // Create a new div for each email
        const emailDiv = document.createElement('div');
        emailDiv.className = 'email-item';

        // Fill the div
        emailDiv.innerHTML = `
          <strong>${emails[i].sender}</strong> - ${emails[i].subject}
          <span style="float:right;">${emails[i].timestamp}</span>
        `;

        // Background color depending on read status
        if (emails[i].read === true) {
          emailDiv.style.backgroundColor = 'lightgray';
        } else {
          emailDiv.style.backgroundColor = 'white';
        }

        // Add click event to load single email
        emailDiv.addEventListener('click', () => load_mail(emails[i].id));

        // Append in the page
        container.appendChild(emailDiv);
      }
    });
}


function load_mail(id)
{
  // Show the Mail and hide other views
  document.querySelector('#mail-view').style.display = 'block';
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'none';


  // GET request to the EMAIL
  fetch(`/emails/${id}`)
  .then(response => response.json())
  .then(email => {
    console.log(email)
    const container = document.getElementById('mail-view');
    container.innerHTML = "";

    const mailDiv = document.createElement('div');
    mailDiv.className = 'mail-item';

    const currentUserEmail = document.querySelector('#current-user').innerText;
    if (email.sender !== currentUserEmail)
    {
       // Create Archive / Unarchive button
        const archiveButton = document.createElement('button');
        archiveButton.innerText = email.archived ? "Unarchive" : "Archive";
        archiveButton.className = "btn btn-sm btn-outline-primary";

        // Add click event to toggle archive
       archiveButton.addEventListener('click', () => {
        fetch(`/emails/${id}`, {
          method: 'PUT',
          body: JSON.stringify({ archived: !email.archived})
          })
        .then(() => load_mailbox('inbox'));
        });

        mailDiv.appendChild(archiveButton);

        // Create Reply Button
        const replyButton = document.createElement('button');
        replyButton.innerText = "Reply";
        replyButton.className = "btn btn-sm btn-outline-primary";

        // Add Click Event
        replyButton.addEventListener('click', () => {compose_email(email);});
        mailDiv.appendChild(replyButton);

    }

    // Fill the Div with email details
    const details = document.createElement('div');
    details.innerHTML = `
      <p><strong>From:</strong> ${email.sender}</p>
      <p><strong>To:</strong> ${email.recipients.join(", ")}</p>
      <p><strong>Subject:</strong> ${email.subject}</p>
      <p><strong>Timestamp:</strong> ${email.timestamp}</p>
      <hr>
      <p>${email.body}</p>`;
    mailDiv.appendChild(details);


    // Append in the page
    container.appendChild(mailDiv);

  })

  // Update Email´s Read
  fetch(`/emails/${id}`, {
  method: 'PUT',
  body: JSON.stringify({
      read: true
  })
  })
}
