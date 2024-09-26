# Weather_Notifier

![Weather_Notifier](https://github.com/user-attachments/assets/1759dcff-b298-46f2-9df0-ad3ad41af3b8)

Sometimes, inspiration comes from the most unexpected conversations! Recently, one of my neighbors, a 7th grader, asked me about what I do as a data engineer. After explaining how I work with data—extracting, cleaning, and loading it—he became fascinated with the process and asked, “Can we build something like that?”

Together, we embarked on a journey to create a simple yet functional project: a Weather Notifier. The goal? To fetch weather data and send it as email updates.

While the concepts of APIs and email systems (SMTP) are usually considered advanced, we broke them down into bite-sized, understandable steps. Here’s how we did it:

His excitement grew the moment he realized he could access live weather data! I introduced him to the idea of using a weather API. Despite it being a new concept, we focused on how it allows us to communicate with external data sources, making it feel like we were “talking” to the internet.

💡 Simplifying the Project: Instead of overwhelming him with all the technical jargon, we approached it step by step:

- Extract: We used the OpenWeatherMap API to fetch weather details based on city names. The API was the key source of data, but we treated it like a simple function that just gives us the weather when we ask for it.
  
- Transform: We learned how to clean and structure the data by focusing on just the relevant pieces—the temperature and weather description.
  
- Load: Finally, we connected Python to Gmail’s SMTP server to send emails with weather updates. Though SMTP is a complex protocol, I explained it as a way to “send a message” from one computer to another.
  
✨ Building Together: We even added a basic UI using Tkinter where he could input multiple cities and email addresses. The look on his face when he saw real-time weather data sent to his inbox was priceless! This project was more than just code; it was about showing him how abstract concepts can come to life when applied practically.

💼 **Key Takeaways**: This experience wasn’t about teaching every single technical detail but rather about sparking curiosity. By focusing on what we wanted to achieve and why each step mattered, we built something real and functional while keeping things fun and engaging.

👨‍💻 **Tech Stack**:

- Python (requests, tkinter, pyodbc)
- OpenWeatherMap API
- SMTP (for email notifications)
- SQL Server for logging emails

## Architecture Flow:
1. User Interface (UI):

- The user interacts with a basic UI created with Tkinter.
- They input multiple email addresses and city names into the input fields.
- Upon clicking the "Send Weather Updates" button, the system initiates the flow.

2. Weather Data Fetching (OpenWeatherMap API):

- The entered cities are passed to the weather.py script.
- The script uses the OpenWeatherMap API to fetch weather details (temperature, description) for each city.
- The API response is parsed and returned to the main application.

3.Email Sending (SMTP):

- The parsed weather data is sent to the notifier.py script.
- The notifier.py script sends weather update emails using Gmail's SMTP server to the email addresses entered by the user.
- Multiple emails are sent, one for each recipient, containing weather details of each city.

4. Data Logging (SQL Server):

- Once an email is sent, the event is logged into a SQL Server database using the log_email function.
- The logged data includes the date/time, sender and recipient email addresses, city, temperature, and weather description.

![1](https://github.com/user-attachments/assets/1b48c0c1-8fb0-4a84-a0d5-e0fab51121a9)

![2](https://github.com/user-attachments/assets/eb0361ae-7043-4d3f-8b2a-ee86bcd5bc6a)

![3](https://github.com/user-attachments/assets/d5665957-675d-427e-8b1e-ea6a0f67c08f)
