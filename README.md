# COMP 1531 Group Project, 19T1

### Aims:

The aim of this group project is to enable students to consolidate their knowledge in the fundamental principles of Software Engineering and apply the theoretical concepts to a “hands-on” software engineering problem. The project will enable students to:

-   Develop problem-solving skills to solve ‘real-world’ software engineering problems; analyse the problem domain, design and develop a solution to the problem

-   Learn to work effectively as part of a team by managing your project, planning, and allocation of responsibilities among the members of your team

-   Gain experience in collaborating through the use of a source control

-   Apply appropriate design practices and methodologies in the development of their solution


### Due Dates:

- Milestone 1: 11:59 pm Sunday 11th March, Week 3  
     (Feedback: Week 4 Lab Session)

- Milestone 2: 11:59 pm Sunday 7th April, Week 6
    ( Demo to tutors and tutor feedback: Week 7 Lab)

- Milestone 3: 11:59 pm Sunday 21st April, Week 9
  (Presentation to class: Week 10 Lab)

- Project Report and Moodle Peer assessment: 11:59PM Sunday 29 April, Week 10

### Value: 25%

# Background

Your consultancy firm has been called in to Australia’s largest burger food chain GourmetBurgers for a new software project.   The client is interested in developing an online self-service ordering application.    The client feels that such a system would provide faster delivery of meals to customers, enable customers to build their own gourmet creations which would result in improving the revenue at the different franchises of the food chain.

# Preliminary Requirements

The online application offers three types of services:

 1. Customers - Place Online Orders
 2. Staff - Service Online Orders
 3. Staff  - Maintain Inventory

### 1. Customer - Online Orders

**Mains**
At any GourmetBurger outlet, a customer can create two types of mains, a burger or a wrap and order their gourmet creation.  For each selected main, a customer can choose:

1. type and number of buns (e.g., 3 sesame buns for a double burger or 2 muffin buns for a standard single burger) - the number of buns cannot exceed the maximum allowable     limit (e.g., if only single, double and triple burgers are permitted, then the customer cannot choose more than 4 buns)
3. type and number of patties (e.g., 2 chicken patties, vegetarian, beef). here again, customers are restricted to the maximum allowable patties
 4. other ingredients of their choice such as tomato, lettuce, tomato sauce, cheddar cheese, swiss cheese etc.
Each of the mains (burger or wrap) has a base price, and each ingredient carries an additional price, so once a customer has completed their gourmet creation, the net price of their created main will be calculated based on the chosen ingredients and displayed to the customer.

**Sides and Drinks**
Besides the main, a customer can (optionally) order sides (e.g., a 6 pack nuggets, 3 pack nuggets, fries (small, medium, large)) and drink(s) of their choice.

Once, a customer has completed their selection (main, side and drink), they can checkout to complete their order. At this point, they will be issued with an order-id.  At any point in time, the customer should be able to check if their order is ready to be collected using their order-id.  The customer can check the status of their order at any point to see if their order is completed.

### 2. Staff - Service Orders

The staff can view the current orders at any point in time.  Once a customer's order has been cooked, they will update the status of the order to indicate that the order is available for pickup by the customer.  The customer should be able to see this change in status at their end when they refresh their page. This order will now disappear from staff orders menu.

### 3. Staff - Maintain Inventory
Staff will also be responsible for maintaining the inventory of their various ingredients.   Periodically, they will refill their stock.  As a customer places an order (e.g. a double burger with 2 chicken patties and cheddar cheese) will result in the inventory levels being decremented accordingly.  At any point in time, if a particular ingredient is not available, the customer will not be able to select the particular item to their order.
Burgers, wraps, nuggets are all stocked in whole quantities.
Bottled drinks are stocked in either cans (375 ml) or bottles (600 ml) and drinks such as orange juice will be served in varying sizes (e.g., a small = 250 ml, a medium = 450 ml etc).
Sides such as fries will need to be stocked by weight (in gms). For example, a small fries = 75g, a medium fries = 125 g and if a customer orders a medium fries, this would reduce the inventory levels by 125g.

# Group Project Requirements

## Team Registration

For this project, you will need to organise yourself into teams of 3 (no more than 3), and all the team members must be from the same lab session. You will do this under the guidance of your tutor in the week 2 lab. While they will try to accommodate your preferences for teammates, they may have to make adjustments to ensure teams have 3 members.

Once your team has been formed one member from the team will need to register it:

1.  Go to  [https://cgi.cse.unsw.edu.au/~cs1531/github/run.cgi/login](https://cgi.cse.unsw.edu.au/~cs1531/github/run.cgi/login)  and sign in
2.  Click on the  **Teams**  button. This will show you a form that you must fill out
3.  Select your tutorial from the left drop-down menu and think of a team name (do NOT use any emojis or similar special characters)
4.  Click  **Create**
5.  Follow the link in the notification to add your other team members. This will create a team within the cs1531 GitHub organisation.

Please ensure that your team is registered by end of week 2.

## Creation of Team Repository

Each team will need to create a repository to collaborate on their group project. One member from the team...

-   Go to  [https://cgi.cse.unsw.edu.au/~cs1531/github/run.cgi/login](https://cgi.cse.unsw.edu.au/~cs1531/github/run.cgi/login)  and sign in

-   Click on the ‘Group Project’ button.

-   Select your tutorial group (on the left drop-down menu) and your team (on the right drop-down menu)

-   Click on Import

This will create a private repository under your team with a file `readme.md` and a default `.gitignore` file to enable you to list files and folders that can be ignored and never committed to the repository, for example your python virtual environment.

## Implementation Guidelines

-   Keeping mind that an Agile Software Development style has been chosen for this project, your team will be required to build and deliver the project in iterations. Each iteration will deliver a part of the requirements of the project during which the team members are expected to carry out all the SDLC activities, namely analysis, design, coding and testing. At the end of the iteration, you (as a team) will demonstrate to your lab class the functionality implemented during that iteration cycle. Your team must bear in mind that project requirements may be subject to change and enhancements to functionalities may be made at the end of the iteration. You will need to carefully design the solution for your current iteration, such that the solution is extensible to accommodate these changes. Deliverable for each iteration will be outlined at the start of each iteration cycle.

-   For this project, no sophisticated authentication is required to be implemented. When the URL of the online app  is specified, e.g.,  [http://localhost:8080/],  this should launch a dashboard that prompts the user to order a mains, side or drink

-   Any kind of persistence mechanism may be used (e.g., Python’s  **pickle**) to store the inventory items

-   This project must be designed using  **object-oriented design**  principles and implemented using  **Python/Flask/Jinja2**. It is recommended that students build their front-end using HTML and CSS only. No other CSS frameworks (e.g. Material CSS, Bootstrap, etc.) to be used for building the UI of the application.

-   What has been provided to you is a problem statement; a set of high-level requirements from the customer. Your team must analyse the problem statement and go through a process of eliciting more formal requirements to develop the final set of user-stories and acceptance tests.   You will need to have a visioning exercise with your customer, to determine the complete range of burgers/wraps and ingredients available for selection to the customer along with any additional constraints to orders.This must be elicited as part of your requirements analysis.

-   The model solution demonstrated in the lectures was only a guide to demonstrate “one” possible way of implementing the customer’s requirements. You are required to design your solution and present in week 10.

-   At the end of each deliverable (weeks 4, 7, & 10) tutors will check the team’s GitHub repositories to ensure that all members of the team have contributed equally to the project and appropriate branches are created by each team member.  There will additionally be an anonymous peer assessment among team members at the week end, where each team member has the opportunity to rate other team members for their contribution to the group project.


## Log Book

You are required to maintain a log book through the entire project that records:

-   date of regular, stand-up meetings

-   summary of decisions made in stand-up meetings, requirements elicited and key design decisions (hand-written user-stories, CRC cards etc.)

-   responsibilities allocated to each team member and tasks to be accomplished for the next meeting

-   progress of tasks using a velocity chart (a hand-drawing will suffice, no sophisticated tool needed), summary of decisions made in stand-up meetings

-   milestones achieved

-   reflection if assigned tasks (decided from last meeting) have been achieved

-   any obstacles


Marks will be awarded for the log book ( in weeks 7 and 10 )

**Assessment**

You will be assessed on your ability to apply what you have learnt in this course as well as your ability to work in a team and produce a significant piece of software. In cases where the client has not been explicit in their requirements, you will need to make your own design decisions with your
team. It is important that you communicate regularly with your team members as well as document your design to avoid confusion about the choices you have made. You will keep a list of assumptions you have made and submit them as part of your final submission in your log book. You will also be asked to justify these decisions when you demonstrate in week 10.

You are expected to use git appropriately by committing consistently and using **feature branches** to manage significant changes. It is an important part of this project for you (as a team) to manage your own time. You need to start early and work consistently: do not be overly optimistic about what you can achieve (remember you are all doing other courses with other assignments). It is essential for you as a team to monitor your own progress and it is often necessary to revise the plan as you progress.

While it is up to you how to divide the work between you, all members must take on the developer role and work consistently throughout the project.   (each team member must work equally on front-end and back-end functionality and testing).

_**Each team member generally receives the same mark, but if the peer assessment tool or the logs of your GitHub repository indicate an imbalance in the amount of work done, the total mark may be scaled to match actual contribution.**_

## Group Project Scheduled Deliverables

The planned dates for the different stages of the project deliverables are outlined below.

-   Week 4 Lab Session: User Stories Submission (10%)
-   Week 7 Lab Session: Demonstration of iteration 1 (40%)
-   Week 10 Lab Session: Final Group Project Demonstration (50%)

### Week 4 Lab Session:  Milestone 1 (10 %)

Prior to your lab session, your team must schedule collaboration sessions, to have initial high-level visioning discussions during which you will brainstorm to identify epic stories from the customer requirements and their key features, break-down high-level user stories to smaller user-stories and detail each user story to identify key conditions of satisfaction, error-conditions etc. Based on the requirements analysisYour team is expected to produce a **product backlog** which contains:

 1.   High Level  **Epic Stories**  from the problem statement
 2.   Each epic story broken into  **user stories**  – Each user-story must define:
       -   a unique story identifier (e.g., UC1)
       -   a short description of the feature based on the Role-Goal-Benefit template (Refer to the RGB model described in the lectures)
       - an estimate for the implementation of the user story in user story points (e.g., UC1 = 2 User story points, where each point = 2.5 hours)
        -   priority of implementation
        -   acceptance criteria for each user story (Refer to the 3 C’s model described in the lectures)

**Please note, the above artifacts will need to be submitted using GIVE by week 4, Monday 8:59 am.**  The submission guidelines for for this milestone and a user-story template will be uploaded to webcms3.

***Note: All members of the team must attend the lab to present their user-stories in order to receive a mark for this milestone.  Any student who is unable to make the lab session due to unavoidable circumstance must notify me prior to the presentation with supporting documentation.***

### Week 7 Lab Session: Milestone 2 ( 40% )

During this lab session, you will demonstrate the first iteration of your working software.  For this iteration, you are required to implement only the **`back-end functionality`** of all the user-stories related to first two services, namely **`customers placing online orders`** and **`staff servicing orders`**.

The task for your team is to  **select the necessary user-stories from the backlog of user-stories developed in week 4**  and implement them to meet the customer’s goals. You will demonstrate the working of your back-end software through running test-cases for each user-story.  For this iteration, you are required to produce the following deliverable.
-   **`Source Code:`** The code you wish to submit for this milestone should be in a branch named  `release`. Use the `master` branch as you would normally and `release` for when your application is stable. Avoid having commits in `release` that are not also in `master` (i.e. you should merge from `master` into `release`, not commit to it directly).
-   **`UML class diagram`**
-   **`Log Book`**

More details about each of the above deliverable will be outlined later.

### Week 10 Lab Session: Milestone 3 ( 50% )
For this iteration, you will need to **update your product backlog** based on **changes made to the requirements** by the customer (customer feedback and changes will be available following milestone 2) and complete all the user-stories in the updated product backlog.  For this milestone, you will also be required to implement a front-end based on HTML/Flask/Jinja for your application.  You will demonstrate your application to your tut group in Week 10.  Details of necessary deliverable for this iteration will be outlined later.

### Peer assessment

To ensure fair allocation of marks, you are required to complete a form on Moodle where you specify how much each team member contributed to the project and any comments you have about them. Information on how you can access this form will be released closer to Week 12.
