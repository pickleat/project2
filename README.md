# Project 2

## Suggested Milestones
- [ ] Research: [Socket.IO](#Socket)
- [ ] Better understand [Client-ide JavaScript](#Client-Side-JS)
- [ ] Research [Local Storage](#Local-Storage)
- [ ] Make a wireframe for the app that gives a style to shoot for. 
- [ ] Complete the Display Name, Channel Creation, and Channel List steps.
- [ ] Complete the Messages View and Sending Messages steps.
- [ ] Complete the Remembering the Channel and Personal Touch steps.

## ToDos
**Display Name:**
- [ ] something

**Channel Creation:**
- [ ] something

**Channel List:**
- [ ] something

**Messages View:**
- [ ] something

**Sending Messages:**
- [ ] something

**Remembering the Channel:**
- [ ] something

**Personal Touch:**
- [ ] something

**README.md writeup:**
- [ ] something

**requirements.txt**
- [ ] Add all other packages to the requirements.txt file

## Project Specs:
**Display Name:**
>When a user visits your web application for the first time, they should be prompted to type in a display name that will eventually be associated with every message the user sends. If a user closes the page and returns to your app later, the display name should still be remembered.
**Channel Creation:**
>Any user should be able to create a new channel, so long as its name doesn’t conflict with the name of an existing channel.
**Channel List:**
>Users should be able to see a list of all current channels, and selecting one should allow the user to view the channel. We leave it to you to decide how to display such a list.
**Messages View:**
>Once a channel is selected, the user should see any messages that have already been sent in that channel, up to a maximum of 100 messages. Your app should only store the 100 most recent messages per channel in server-side memory.
**Sending Messages:**
>Once in a channel, users should be able to send text messages to others the channel. When a user sends a message, their display name and the timestamp of the message should be associated with the message. All users in the channel should then see the new message (with display name and timestamp) appear on their channel page. Sending and receiving messages should NOT require reloading the page.
**Remembering the Channel:**
>If a user is on a channel page, closes the web browser window, and goes back to your web application, your application should remember what channel the user was on previously and take the user back to that channel.
**Personal Touch:**
>Add at least one additional feature to your chat application of your choosing! Feel free to be creative, but if you’re looking for ideas, possibilities include: supporting deleting one’s own messages, supporting use attachments (file uploads) as messages, or supporting private messaging between two users.
**README.md writeup:**
>Include a short writeup describing your project, what’s contained in each file, and (optionally) any other additional information the staff should know about your project. Also, include a description of your personal touch and what you chose to add to the project.
**requirements.txt**
>If you’ve added any Python packages that need to be installed in order to run your web application, be sure to add them to requirements.txt!

**Hints**
>You shouldn’t need to use a database for this assignment. However, you should feel free to store any data you need in memory in your Flask application, as via using one or more global variables defined in application.py.
>You will likely find that [local storage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage) will prove helpful for storing data client-side that will be saved across browser sessions.

## Research

### Socket
[Socket.io Documentation](https://socket.io/docs/)
[Flask/Socket Documentation](https://flask-socketio.readthedocs.io/en/latest/)

- Gives instructions for:
    - Initialization
    - Recieving/Sending Messages
    - Broadcasting
    - Rooms
    - Connection Events
    - Other Functions
    - Error Handling

### Client-Side-JS
Research Goes here: 

### Local-Storage
[Local Storage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage)