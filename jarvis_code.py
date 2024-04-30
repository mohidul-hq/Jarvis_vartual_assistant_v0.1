import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import csv
import pyautogui
import time
import psutil


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Load contacts from CSV file
def load_contacts():
    contacts = {}
    with open(r'C:\\Users\\mohid\\OneDrive\\Desktop\\My all Codes\\Python Codes\\contacts.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) >= 2:
                contacts[row[0].lower()] = row[1]
    return contacts


contacts = load_contacts()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning sir!")
    elif 12 <= hour < 18:
        speak("Good Afternoon sir!")
    else:
        speak("Good Evening sir!")
    speak("Please tell me how may I help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\033[91m" + "Listening..." + "\033[0m")  # Red color for "Listening..."
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("\033[97m" + "Recognizing..." + "\033[0m")  # White color for "Recognizing..."
        query = r.recognize_google(audio, language='en-in')
        print("\033[32m" + f"User said: {query}\n" + "\033[0m")  # Green color for user input
        
        if 'close last window' in query:
            pyautogui.hotkey('alt', 'shift', 'tab')  # Switch to the second last window using Alt + Shift + Tab
            time.sleep(1)  # Pause for stability
            pyautogui.hotkey('alt', 'f4')  # Close the second last window using Alt + F4
            speak("Second last window closed successfully!")
            return "None"

        elif 'close all windows' in query:
            close_all_windows()
            speak("All windows except the active one have been closed.")
        
        elif 'activate sleep mode' in query:
            speak("Entering sleep mode.")
            return "sleep"

    except Exception as e:
        print("\033[93m" + "Say that again please..." + "\033[0m")  # Yellow color for "Say that again please..."
        return "None"

    return query.lower()


def close_all_windows():
    # Get the list of all running processes
    for proc in psutil.process_iter(['pid', 'name']):
        # Check if the process is a visible window
        if proc.info['name'] in ['explorer.exe', 'firefox.exe', 'chrome.exe', 'msedge.exe', 'opera.exe', 'iexplore.exe', 'safari.exe']:
            # Get the process ID
            pid = proc.info['pid']
            try:
                # Get the handle of the window
                hwnd = pyautogui.getWindowsWithTitle(proc.info['name'])[0].hwnd
                # Close the window if it's not the active one
                if hwnd != pyautogui.getActiveWindow().hwnd:
                    pyautogui.closeAllWindows(hwnd=hwnd)
            except:
                pass

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


def activate_whatsapp():
    # Replace this with the correct path to your WhatsApp executable
    whatsapp_path = r"C:\\Program Files\WindowsApps\\5319275A.51895FA4EA97F_2.2415.10.0_x64__cv1g1gvanyjgm\WhatsApp.exe" 

    os.startfile(whatsapp_path)
    # Wait for WhatsApp to load
    time.sleep(5)

def send_whatsapp_message(recipient, content):
    try:
        # Activate WhatsApp window
        activate_whatsapp()

        # Wait for WhatsApp to load
        time.sleep(5)

        # Search or start a new chat
        pyautogui.click(80, 140)  # Click on the search bar
        pyautogui.write(recipient, interval=0.25)  # Type recipient's name
        time.sleep(2)
        pyautogui.press('enter')  # Press enter to search or start a new chat

        # Type and send message
        pyautogui.click(240, 200)  # Click on the message box
        pyautogui.write(content, interval=0.2)  # Type the message
        pyautogui.press('enter')  # Press enter to send

        speak("WhatsApp message sent successfully!")
    except Exception as e:
        print(e)
        speak("Sorry, I am unable to send the WhatsApp message.")

def ask_recipient():
    speak("To whom should I send this message?")
    recipient = takeCommand()
    return recipient.lower()

def make_whatsapp_call(recipient_number):
    try:
        # Ask user whether they want to make a voice call or video call
        speak("Do you want to make a video call or voice call?")

        # Listen for user's choice
        choice = takeCommand()
        
        # Activate WhatsApp window
        activate_whatsapp()

        # Wait for WhatsApp to load
        time.sleep(5)

        # Click on the search bar
        pyautogui.click(80, 140)

        # Type recipient's number
        pyautogui.write(recipient_number, interval=0.25)

        # Press enter to search for the contact
        pyautogui.press('enter')

        # Wait for the contact to load
        time.sleep(2)

        # Click on the contact
        pyautogui.click(150, 240)  # Adjust the coordinates based on your screen

        # Wait for the contact options to load
        time.sleep(2)

        # Check if the user wants to make a voice call
        if 'voice' in choice:
            pyautogui.click(1800, 75)  # Adjust the coordinates for the voice call button
            speak("WhatsApp voice call initiated successfully!")
        # Check if the user wants to make a video call
        elif 'video' in choice:
            pyautogui.click(1700, 75)  # Adjust the coordinates for the video call button
            speak("WhatsApp video call initiated successfully!")
        else:
            speak("Invalid choice. Please try again.")
    except Exception as e:
        print(e)
        speak("Sorry, I am unable to make the WhatsApp call.")

def wake_up():
    speak("Yes, sir!")

if __name__ == "__main__":
    is_active = False
    while True:
        if not is_active:
            query = takeCommand()
            if 'jarvis' in query:
                is_active = True
                wishMe()

        else:
            query = takeCommand()

            if query == "sleep":
                is_active = False
                speak("Entering sleep mode.")
                continue

            if 'deactivate jarvis' in query:
                is_active = False
                speak("Deactivating Jarvis.")
                break

            if 'tell me about' in query:
                question = query.replace("tell me about",)
                question = query.replace("tell me about", "").strip()
                speak(f'Searching Wikipedia for {question}...')
                try:
                    results = wikipedia.summary(question, sentences=2)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)
                except wikipedia.DisambiguationError as e:
                    speak("There may be multiple interpretations for your question. Please be more specific.")
                except wikipedia.PageError as e:
                    speak("Sorry, I couldn't find any information about that.")

            elif 'open youtube' in query:
                webbrowser.open("https://www.youtube.com/")
                speak("Sure sir!")

            elif 'open google' in query:
                webbrowser.open("https://www.google.com/")
                speak("Sure sir!")


            elif 'open stackoverflow' in query:
                webbrowser.open("https://stackoverflow.com")
                speak("Sure sir!")


            elif 'play music' in query:
                webbrowser.open("https://www.youtube.com/watch?v=BYl7v0YsX9g&list=PPSV")
                speak("Sure sir!")


            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")
                print(f"Sir, the time is {strTime}")
                speak("Sure sir!")


            elif 'open code' in query:
                codePath = "C:\\Users\\mohid\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)
                speak("Welcome to Programming world!")
                speak("Sure sir!")


            elif 'who are you' in query:
                speak("I am jarvis virtual artificial intelligence, i am here to assists you variety of tasks best i can, 24 hours a day 7 days of week, importing all preferences hermit today's, Now systems are fully operational!")
                
            elif 'great job jarvis' in query:
                #print("Debug - Query:", query)
                speak("Thank you! Glad I could help.")


            elif 'oh nice' in query:
                #print("Debug - Query:", query)
                speak("Thanks sir!")



            elif 'well done' in query:
                #print("Debug - Query:", query)
                speak("Thanks sir!")

    


            elif 'email to user' in query:
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    to = "user@gmail.com"
                    sendEmail(to, content)
                    speak("Email has been sent!")
                    speak("Sure sir!")
                except Exception as e:
                    print(e)
                    speak("Sorry my friend, I am not able to send this email")
                    speak("Sorry sir!")

            elif 'send message' in query:
                try:
                    speak("What should I say in the message?")
                    content = takeCommand()
                    recipient = ask_recipient()
                    while recipient not in contacts:
                        speak("I apologize, but I couldn't find the contact. Could you please provide the recipient's name again?")
                        recipient = ask_recipient()
                    number = contacts[recipient]
                    send_whatsapp_message(number, content)
                except Exception as e:
                    print(e)
                    speak("Sorry, I am unable to send the WhatsApp message.")

            elif 'make call' in query:
                try:
                    speak("Whom should I call on WhatsApp?")
                    recipient = takeCommand()
                    while recipient not in contacts:
                        speak("I apologize, but I couldn't find the contact. Could you please provide the recipient's name again?")
                        recipient = takeCommand()
                    make_whatsapp_call(contacts[recipient])
                except Exception as e:
                    print(e)
                    speak("Sorry, I am unable to make the WhatsApp call.")
