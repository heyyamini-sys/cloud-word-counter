Cloud-Word-Counter

A serverless, full-stack web application that dynamically counts words and characters, securely saving the analytics to a cloud database.

Architecture:
* **Frontend:** HTML, CSS, and JavaScript.
* **API Routing:** AWS API Gateway (with Lambda Proxy Integration).
* **Compute:** AWS Lambda (Python).
* **Database:** MongoDB Atlas (NoSQL).

How It Works:
1. The user inputs text into the browser interface.
2. JavaScript sends a `POST` request to the AWS API Gateway endpoint.
3. API Gateway triggers the AWS Lambda function.
4. The Python Lambda function calculates the word and character counts.
5. The analytics and a timestamp are securely saved into a MongoDB Atlas cluster.
6. A success response is sent back to update the webpage dynamically.

Key Learnings:
* Configuring **CORS** and Preflight requests in AWS API Gateway.
* Managing API deployment stages and Lambda Proxy settings.
* Securely connecting to MongoDB using environmental variables to protect database credentials.
* Troubleshooting backend issues using browser developer tools (F12) and AWS CloudWatch logs.
