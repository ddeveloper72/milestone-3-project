# Guidelines

Use the following guidelines when developing your project:

- The project's logic must be written in Python. HTML, CSS, and JavaScript can be used to enhance the look and feel of the game.
- Whenever possible, strive to use semantic HTML5 elements to structure your HTML code better.
- We recommended taking a TDD approach to building the game.
  
  *   Create a section in your README.md titled 'Testing.' In this section, summarise your approach to testing and provide pseudocode you have written to develop your tests
  *   Write and run automated tests to ensure that your website’s functionality works well
  *   If you run any manual tests be sure to document those tests in the 'Testing' section of your README
  *   If there are any tests that are not running as expected or are failing, provide a summary in the 'Testing' section of your README of what your expected output was and any reasons as to why the test(s) may be failing.
  
-   Use flask, a micro-framework, to structure your project's back-end. Provide instructions on how to deploy your project in your README.
-   Make sure your site is as responsive as possible. You can test this by checking the site on different screen sizes and browsers.
-   We advise that you write down user stories and create wireframes/mockups before embarking on full-blown development.
-   The site can also make use of CSS frameworks such as Bootstrap, just make sure you maintain a clear separation between the library code and your code.
-   Write a README.md file for your project that explains what the project does and the need that it fulfills. It should also describe the functionality of the project, as well as the technologies used. If some of the work was based on other code, explain what was kept and how it was changed to fit your need. A project submitted without a README.md file will FAIL.
-   Use Git & GitHub for version control. Each new piece of functionality should be in a separate commit.
-   Deploy the final version of your code to a hosting platform such as Heroku.

Non-requirements for this project:

*   Secure user authentication (e.g. via passwords) is not required for this particular project. Having each user just choose a username is sufficient. Secure authentication will be introduced in the Django module.
*   Persisting data by writing it in files is not required in this project, and indeed is problematic on Heroku due to its ephemeral filesystem. Instead, prefer to keep all of the data you need in memory (in variables) and/or in Flask sessions. Storing data effectively in a database will be the focus of the next module
*   Your project is not expected to support real-time interaction between users on different browsers. There are ways to achieve this with clever use of js polling or websockets, but it's not a requirement for this project. It's perfectly fine if new data is only retrieved from the backend whenever a user loads a new page.

## PLAGIARISM
It is each student’s responsibility to ensure that when they include (directly or indirectly) the work of others that this contribution is fully and adequately acknowledged and documented.

You are encouraged to ask your mentor/tutor for advice about your project work, but note that your project code should not include any code written by others unless it is explicitly credited to them with a comment above. Any such code provided by your mentor/tutor would not contribute to your assessment. Failure to attribute credit to code that isn’t yours will be considered as plagiarism and will result in a failing grade.

*Document source: The Code Institute - Project Guidelines*