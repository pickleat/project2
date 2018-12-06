# Project 2

## Suggested Milestones
- [x] Research: [Socket.IO](#Socket)
- [x] Better understand [Client-side JavaScript](#Client-Side-JS). Put an x, but mostly because there weren't many resources. 
- [x] Research [Local Storage](#Local-Storage). Set aside a few links for later reference.
- [x] Make a [wireframe](#wireframe) for the app that gives a style to shoot for.
- [ ] Complete the Display Name, Channel Creation, and Channel List steps.
- [ ] Complete the Messages View and Sending Messages steps.
- [ ] Complete the Remembering the Channel and Personal Touch steps.

## ToDos
**Template Implementation**
-[ ] Channel Name
-[ ] Left Bar
-[ ] Text Area
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
        - if adding you need to add ```import join_room, leave_room```
    - Connection Events
    - Other Functions
    - Error Handling
- This will be a great reference.
- From this documentation, it feels like this will be a one-page site, with lots of different forms with values(or something else?) that trigger the ```@socketio.on('something')``` events.

Seems like socket heavily relies on Flask, which is great since the last project was made on flask!

### Client-Side-JS
Doesn't seem to be an easy guide or tutorial for client-side JS specifically. But here's what I did find: 
[MDN-Client-Side-APIs](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs)
[MDN-Client-Side-Storage](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Client-side_storage)
[Document-Object-Model-MDN](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction)

- Lots of good info here, explaining how the DOM works and what the pieces are called.
    - ```Document``` an object referring to the page being loaded (?)
    - ```element``` refers to an element or node returned by the DOM AP

### Local-Storage
[Local-Storage-MDN](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage)
>The read-only localStorage property allows you to access a Storage object for the Document's origin; the stored data is saved across browser sessions. localStorage is similar to sessionStorage, except that while data stored in localStorage has no expiration time, data stored in sessionStorage gets cleared when the page session ends — that is, when the page is closed.
[Web-Storage-API-MDN](https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API/Using_the_Web_Storage_API)

### Wireframe
![Basic-WireFrame](https://raw.githubusercontent.com/pickleat/project2/master/Flack.png)
