
# URL Shortener App

## Introduction
This URL Shortener App is a simple tool to shorten URLs using the Bitly API. It also allows you to check the number of clicks on a Bitly link. This application can be run in a Docker container for easy setup and deployment.

## Prerequisites
Before you begin, ensure you have met the following requirements:
- Docker and Docker Compose installed on your system.
- A Bitly API token. You can obtain this by signing up at [Bitly](https://bitly.com/).

## Installation
1. **Clone the Repository**
   
   Clone this repository to your local machine using:
   ```
   git clone https://github.com/7uperior/URL-Shortener
   ```

2. **Environment Setup**

   Create a `.env` file in the root of the project with the following content:
   ```
   BITLY_API_TOKEN='YOUR_TOKEN'
   ```
   Replace `YOUR_TOKEN` with your actual Bitly API token.

3. **Build and Run with Docker**

   Run the following command to build and start the application using Docker:
   ```
   docker-compose up --build -d
   ```

## Usage
After starting the application:
1. Attach to the Docker container:
   ```
   docker attach url-shortener-app-1
   ```
2. Press "Enter" to start the application (this is a Docker-specific requirement).

3. The application will prompt you to enter a URL. Input the URL you wish to shorten or get click stats for.

## Features
- **URL Shortening**: Enter any URL to get a shortened version using Bitly.
- **Click Count**: For any Bitly link, the app can display the total number of clicks.

## main.py
The `main.py` file contains the core logic of the application, including API interactions with Bitly and functions for URL shortening and click count retrieval.
