import webbrowser
import schedule
import time

# Defining the websites to open
websites = ["https://roymustang-dev-ml-dataset-explorer-app-app-ldxvnr.streamlit.app/",
            "https://roymustang-dev-course-recommendation-system-app-eptgsa.streamlit.app/",
            "https://adi-portfolio.streamlit.app/"]

# Function to open websites
def open_websites():
    for website in websites:
        webbrowser.open(website)


# Scheduling the function to run at 10:00 AM everyday
schedule.every().day.at("01:15").do(open_websites)

# Keep the program running in a loop
while True:
    schedule.run_pending()
    time.sleep(1)