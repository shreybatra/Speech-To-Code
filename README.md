# Speech-To-Code
Speech to Code service, built for Microsoft AI Hackathon

## Inspiration
The inspiration for this project was "my laziness". It is a wild fantasy for almost every developer to speak to their machine and the machine automatically types the code for you. The challenge to use Azure AI to achieve this couldn't have been more accurate. _Imagine travelling in an Uber and side by side writing your code by speaking to your phone and by the time you reach to your office, it automatically exports the .py file to your system._

## What it does
Our service, Speech to Code showcases the ability to write code, by speaking to the machine. A demo has been given in the video which showcases a simple website to speak commands and it automatically writes your code.

Our system identifies the type of command given and accordingly extracts important information such as keywords and entities to build the line of code. **Currently it supports the code syntax of Python.** The following commands are ready to test for you - 
1. Create an integer.
2. Create a string.
3. Create a list.
4. Create a For Loop.
5. Print/Display any variable
6. Delete a line.
7. Delete everything.
8. Add indents (to add \t to write in blocks inside for loops.)
9. Remove indents.

## Testing
There are two ways to test your code. Both ways need an Azure Speech To Text API subscription key.
1. Open this [link](https://speechtocodeui.z22.web.core.windows.net/). Wait for it to load the SDK, the warning will hide on its own. Add your Azure Speech to Text subscription key and region of service and enjoy giving commands to it.
2. Manual Testing - Clone the repository mentioned, create a **.env** file with sample contents given in **test.env** file. Create a python3 virtual env and pip install the requirements file. Run main.py and open index.html in your browser.

## How I built it
As I came to know about this project too late, I had just about a day or two to come up with an MVP for the same. The tech stack includes - 
1. Basic Testing UI to send voice commands to. This could later be integrated in some Voice controlled device such as Echo, Google Home, and similar. _This UI takes the speech and converts it to text using Azure Speech to Text APIs._
2. Backend - Made by a simple flask API, it internally calls 2 types of service.
  a) LUIS - Language Understanding by Azure, which tells us which type of command has been given to the service.
  b) Azure Text Analytics API - To extract out important informations such as variable names, integer or string values, list definitions, loop limits, etc.

## Services Used
1. Azure Language Understanding - LUIS.
2. Azure Text Analytics - Language Cognitive Services.
3. Azure Speech to Text Service.
4. Azure App Service (to deploy the code.)
5. Azure Storage (for static website hosting).

## Challenges I ran into
1. The biggest challenge was the time frame, as I came to know about this just 2 days before the deadline and with busy office hours, it was difficult to add in complex commands. They will be continuously added and published, now that it has started.
2. To deploy the backend code APIs on Azure App Service, as I myself had little experience to deploy the same.
3. To structure the coding language (spoken) in such a way that the system understands the natural language and takes into account the variable names and values with efficient accuracy.

## Accomplishments that I'm proud of
1. I am proud of to create a sample app which actually demonstrates how we can use speech to write code itself, making the life of a developer a little bit easier.
2. I also am proud I could complete this sample in whatever time frame I had and to deploy the whole system onto Azure App Service, i have a working tester for the world to test and give me feedback.

## What I learned
1. I learned to use Azure's much accurate AI APIs, mostly speech and language, which makes the use of NLP in our system too easy.
2. I learned how to deploy your application to Azure Cloud, using App Services and plans.
3. I even learned using CSS a bit, as I am myself not a big fan of UI Development.

## What's next for Speech To Code
1. The next, for sure, is to expand the possibilities of commands for this service, such as creating complex mathematical expressions, while loops, condition checking (both variable to variable and with different data types).
2. It would be to incorporate this service to a proper Voice Assistant Tool, which the developers can use it in their own simple ways, such as through their mobile or earphones.
