Todo
---

* <s>Submit: Change what it says</s>
* <s>Make a JS File and link it in the header.</s>
* <s>Capture the submit event of the login form. </s>
  * <s>Send the username to the server via ajax POST (you will get an error bc it is a non existent pg)</s>
* <s>Login should be hidden before the js loads then the JS will showit</s>
* <s>Make a login page handler (tornado)</s>
  * <s>response: {success: true, message: LOGGED IN}</s>
  * <s>response should be in json </s>
  * <s>response should have correct mime type aka right "content type"</s>
* <s>Form for chat message text box</s>
* <s>After login *success* hide login form and show "chat message textbox form"</s>
* <s>Attach a submit handler to "chat message textbox"</s>
* <s>Bundle up the message and send to a new fictional page of your choosing</s>
  * <s>Send the username and send the message</s>
* <s>Create "message handler" on the server</s>
* <s>Make logout form
  * Logout should be next to submit button for the chat box
  * Logout should be its own form
  * Make logout handler
    * Send to fictional page of your own choosing
    * Bundle username and send it back </s>
* <s>Server (login page) delays for 5 seconds before it responds
  * Use asyncio
    * HINT: Instead of a regular get/post make a tornado coroutine get/post
    * HINT: make new func that should be an asyncio coroutine
    * HINT: Figure out how to call a single asyncio coroutine inside a tornado coroutine
    * HINT: Do the sleep inside the asyncio coroutine using the asyncio sleep </s>
* Use a global dict that will store all the currently logged in usernames
  * Make sure when the user logs out it removes it from the dict
* Login with same username responds with a failure message (to the ajax ie from server)
* Handle response in ajax and check if success is true and use alert() if False
* Server side: check if username is valid, send a response msg with why it has failed
  * Criteria:
    * more than three characters
    * no special characters except (a,z,A,Z,1,9)
    * Not more than 20 characters
  * Make it on the client side using the same criteria as above:
    * When you test on the server make sure the client side is commented out







































