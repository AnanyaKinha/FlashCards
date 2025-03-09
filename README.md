# **Flashcard Web App for Learning System Design, Java, and OOP**

## **Overview**
This is a web-based flashcard application designed to help users learn and practice concepts related to **System Design**, **Java**, and **Object-Oriented Programming (OOP)**. The application presents questions in a flashcard format, allowing users to type their answers and verify them.  

The app is built using **React.js** for the frontend and uses **Appwrite** for backend services, including database and authentication. It also features a dynamically updatable question bank to keep content relevant.  



## **Features**
### Flashcard Learning
- Users can select a topic (System Design, Java, or OOP).
- A flashcard with a question is presented, allowing the user to type their answer.
- After submission, the correct answer is revealed.

### Dynamic Question Bank
- Questions and answers are stored in **Appwrite's database**, allowing easy updates without code changes.
- Supports multiple topics with their own set of questions.

### User Progress Tracking
- Tracks the user's progress on each topic.
- Users can revisit questions to reinforce learning.

### Responsive Design
- Fully responsive and mobile-friendly UI.




## **Tech Stack**
| Technology     | Purpose                                                                 |
|----------------|-------------------------------------------------------------------------|
| **React.js**    | Frontend development                                                    |
| **Appwrite**    | Backend services, including database and authentication                |
| **Tailwind CSS**| Styling and UI components                                              |
| **Vite**        | Build tool for faster development and optimized production build       |



## **System Architecture**
![System Architecture Diagram](https://github.com/AnanyaKinha/FlashCards/blob/main/images/SysArch.png?raw=true)

The application follows a client-server architecture with the following flow:
1. **User** interacts with the web app through a browser.
2. The **frontend** (React.js) sends requests to the **Appwrite API** for fetching questions and updating progress.
3. The **Appwrite API** handles the requests and retrieves data from the **Appwrite Database**.
4. The database stores all flashcard questions, answers, and user progress.
5. The frontend renders the flashcards and tracks user interactions.

