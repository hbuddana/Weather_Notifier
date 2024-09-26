# Weather_Notifier

![Weather_Notifier](https://github.com/user-attachments/assets/1759dcff-b298-46f2-9df0-ad3ad41af3b8)

Sometimes, inspiration comes from the most unexpected conversations! Recently, one of my neighbors, a 7th grader, asked me about what I do as a data engineer. After explaining how I work with data—extracting, cleaning, and loading it—he became fascinated with the process and asked, “Can we build something like that?”

Together, we embarked on a journey to create a simple yet functional project: a Weather Notifier. The goal? To fetch weather data and send it as email updates.

While the concepts of APIs and email systems (SMTP) are usually considered advanced, we broke them down into bite-sized, understandable steps. Here’s how we did it:

His excitement grew the moment he realized he could access live weather data! I introduced him to the idea of using a weather API. Despite it being a new concept, we focused on how it allows us to communicate with external data sources, making it feel like we were “talking” to the internet.

💡 Simplifying the Project: Instead of overwhelming him with all the technical jargon, we approached it step by step:

Extract: We used the OpenWeatherMap API to fetch weather details based on city names. The API was the key source of data, but we treated it like a simple function that just gives us the weather when we ask for it.
Transform: We learned how to clean and structure the data by focusing on just the relevant pieces—the temperature and weather description.
Load: Finally, we connected Python to Gmail’s SMTP server to send emails with weather updates. Though SMTP is a complex protocol, I explained it as a way to “send a message” from one computer to another.
✨ Building Together: We even added a basic UI using Tkinter where he could input multiple cities and email addresses. The look on his face when he saw real-time weather data sent to his inbox was priceless! This project was more than just code; it was about showing him how abstract concepts can come to life when applied practically.

💼 ** Key Takeaways **: This experience wasn’t about teaching every single technical detail but rather about sparking curiosity. By focusing on what we wanted to achieve and why each step mattered, we built something real and functional while keeping things fun and engaging.

👨‍💻 Tech Stack:

Python (requests, tkinter, pyodbc)
OpenWeatherMap API
SMTP (for email notifications)
SQL Server for logging emails
