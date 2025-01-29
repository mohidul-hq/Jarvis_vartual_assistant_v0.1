# Jarvis AI Assistant

## Overview

Jarvis is a voice-controlled AI assistant designed to assist users with a wide variety of tasks, including searching Wikipedia, opening websites, playing music, managing windows, sending emails, and sending WhatsApp messages or making WhatsApp calls.

## Features

- **Voice Commands**: Hands-free interaction using speech recognition.
- **Wikipedia Integration**: Search for information and hear summaries.
- **Web Navigation**: Quickly access popular websites like YouTube, Google, and Stack Overflow.
- **Music Player**: Open YouTube playlists and control playback.
- **Time Query**: Ask Jarvis to tell the current time.
- **Application Launch**: Open applications such as Visual Studio Code.
- **Email Functionality**: Send emails with voice instructions.
- **WhatsApp Messaging**: Send messages or make voice/video calls via WhatsApp.
- **Window Management**: Close specific or all application windows.

## Prerequisites

Ensure you have the following software installed and configured:

- Python 3.x
- Required Python Libraries:
  - `pyttsx3`
  - `speech_recognition`
  - `wikipedia`
  - `webbrowser`
  - `smtplib`
  - `psutil`
  - `pyautogui`
  - `csv`
- A contacts file (`contacts.csv`) in the specified directory for WhatsApp communication.

## Installation

1. Clone or download the project.
2. Install the required libraries using:

   ```bash
   pip install pyttsx3 speechrecognition wikipedia psutil pyautogui
