from tkinter import *
import requests
import json

root = Tk()
root.title('Weather App Tutorial') 
root.geometry("600x100")

def zipLookup():
    try:
        api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() + "&distance=5&API_KEY=B2B89E05-D510-49D2-9D08-F80EEA4308E2")
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

        root.configure(background=weather_color)
        myLabel = Label(root, text=city + "'s Air Quality is " + str(quality) + ". The Air Seems " + category + ".", font=("Helvetica", 15), background=weather_color)
        myLabel.grid(row=2, column=0)
    except Exception as e:
        api = "Error..."


zip = Entry(root)
zip.grid(row=0, column=0, stick=W+E+N+S)

zipButton = Button(root, text="Lookup Zipcode", command=zipLookup)
zipButton.grid(row=0, column=1, stick=W+E+N+S)

root.mainloop()
