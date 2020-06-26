from tkinter import *
import requests
import json

root = Tk()
root.title('Weather App Tutorial') 
root.geometry("400x24")

try:
    api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=95843&distance=5&API_KEY=B2B89E05-D510-49D2-9D08-F80EEA4308E2")
    api = json.loads(api_request.content)
    city = myLabel = api[0]['ReportingArea']
    quality = myLabel = api[0]['AQI']
    category = myLabel = api[0]['Category']['Name']

    if category == "Good":
        weather_color = "#0C0"
    elif category == "Moderate":
        weather_color = "#FFFF00"
    elif category == "Unhealthy for Sensitive Groups":
        weather_color = "#ff9900"
    elif category == "Unhealthy":
        weather_color = "#FF0000"
    elif category == "Very Unhealthy":
        weather_color = "#990066"
    elif category == "Hazardous":
        weather_color = "#660000" 
except Exception as e:
    api = "Error..."

root.configure(background=weather_color)
string_quality = str(quality) 
myLabel = Label(root, text=city + "'s Air Quality is " + str(quality) + ". The Air Seems " + category + ".", font=("Helvetica", 13), background=weather_color)
myLabel.pack()

root.mainloop()
