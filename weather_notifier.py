import tkinter as tk
from tkinter import messagebox
from weather import get_weather
from notifier import send_email
import config
import pyodbc
from datetime import datetime

# Function to log emails into the SQL Server database with city name
def log_email(sender_email, receiver_email, temp, desc, city):
    conn = pyodbc.connect(
        f'DRIVER={config.SQL_SERVER["DRIVER"]};'
        f'SERVER={config.SQL_SERVER["SERVER"]};'
        f'DATABASE={config.SQL_SERVER["DATABASE"]};'
        'Trusted_Connection=yes;'
    )
    cursor = conn.cursor()

    sent_datetime = datetime.now()
    cursor.execute(
        "INSERT INTO EmailLog (SentDateTime, SenderEmail, ReceiverEmail, CityName, Temperature, WeatherDescription) VALUES (?, ?, ?, ?, ?, ?)",
        sent_datetime, sender_email, receiver_email, city, temp, desc
    )
    conn.commit()

    cursor.close()
    conn.close()

# Function to send weather updates for multiple cities and log each one
def send_weather_updates():
    emails = email_entry.get()
    cities = city_entry.get()
    
    receivers = [email.strip() for email in emails.split(',') if email.strip()]
    city_list = [city.strip() for city in cities.split(',') if city.strip()]

    if not receivers:
        messagebox.showerror("Input Error", "Please enter at least one email.")
        return
    if not city_list:
        messagebox.showerror("Input Error", "Please enter at least one city.")
        return

    for city in city_list:
        temp, desc = get_weather(config.API_KEY, city)
        if temp and desc:
            subject = f"Weather Update for {city}"
            body = f"City: {city}\nTemperature: {temp}°C\nWeather: {desc}.Harsha Buddana"

            for receiver in receivers:
                send_email(config.SENDER_EMAIL, config.SENDER_PASSWORD, receiver, subject, body)
                # Log the email to the database with the city
                log_email(config.SENDER_EMAIL, receiver, temp, desc, city)

        else:
            messagebox.showerror("Error", f"Failed to fetch weather data for {city}!")

    messagebox.showinfo("Success", "Weather updates sent and logged successfully!")

# UI Setup
root = tk.Tk()
root.title("Weather Notifier")

tk.Label(root, text="Enter email addresses (comma-separated):").pack(pady=5)
email_entry = tk.Entry(root, width=50)
email_entry.pack(pady=5)

tk.Label(root, text="Enter city names (comma-separated):").pack(pady=5)
city_entry = tk.Entry(root, width=50)
city_entry.pack(pady=5)

send_button = tk.Button(root, text="Send Weather Updates", command=send_weather_updates)
send_button.pack(pady=20)

root.mainloop()
