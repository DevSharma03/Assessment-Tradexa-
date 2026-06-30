# AI Usage Report

## 1. AI Tool(s) Used

- ChatGPT (OpenAI GPT-5.5)

---

## 2. Prompts Used

The following are the major prompts and discussions used during the development of this assignment:

- Reviewed the assignment requirements and submission expectations.
- Discussed the overall project architecture for a lightweight Django backend.
- Designed a simple and maintainable folder structure.
- Planned the API request and response format.
- Designed the complete request flow from receiving an order to recommending the best shipping box.
- Discussed whether to use a database or a JSON file for storing box information.
- Designed the separation of responsibilities between Views, Services, Validators, and Utility functions.
- Generated the project skeleton and Django boilerplate.
- Reviewed multiple approaches for implementing the box recommendation algorithm.
- Discussed edge cases and testing scenarios.

---

## 3. AI Output Accepted

The following AI-generated suggestions were accepted and used in the project:

- Overall project architecture.
- Folder structure.
- Django application structure.
- API endpoint design.
- Request and response schema.
- Separation of business logic into a dedicated service layer.
- Validation layer for incoming requests.
- Utility/helper function organization.
- JSON-based storage for available shipping boxes.
- Django boilerplate for views and URL routing.
- High-level recommendation workflow.
- Test case suggestions.

---

## 4. AI Output Rejected or Modified

Some AI suggestions were intentionally modified or rejected during implementation:

- Rejected using a database, as the assignment only required a backend system and did not require persistent storage.
- Rejected unnecessary enterprise-level design patterns such as Repository Pattern, Factory Pattern, Dependency Injection, and Singleton Pattern.
- Rejected authentication, admin panel, Docker, and deployment-related suggestions as they were outside the assignment scope.
- Modified the folder structure slightly to better fit the project's simplicity.
- Implemented the recommendation algorithm manually instead of directly copying AI-generated business logic.
- Reviewed and adjusted all generated code before integrating it into the project.

---

## 5. Mistakes or Limitations in AI Output

During development, the following limitations were identified:

- Some initial architectural suggestions introduced unnecessary complexity for a small assignment.
- The assignment did not define how products should be packed inside a box, so AI could only suggest possible approaches rather than a definitive solution.
- Boilerplate code required manual refinement to match the final project structure.
- Some helper methods required modification based on the final implementation.

---

## 6. Verification Process

All AI-generated content was manually reviewed before being used.

The final implementation was verified by:

- Comparing the implementation against the assignment requirements.
- Reviewing the project architecture before coding.
- Manually reviewing every generated code snippet.
- Testing the API endpoints using Postman.
- Writing and executing unit tests.
- Testing common edge cases, including:
  - Empty orders
  - Invalid request payloads
  - Orders exceeding weight capacity
  - Orders exceeding box dimensions
  - Multiple valid box options
  - No suitable box available

Only the reviewed, tested, and verified code was included in the final submission.
