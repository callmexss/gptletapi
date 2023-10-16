# GPTletAPI

## Overview

GPTletAPI is a Django-based backend service that leverages the OpenAI GPT API to create small conversational applications. It includes a DRF-based API for easy integration with frontend services.

## Requirements

- Python 3.8+
- Django 3.2+
- Django Rest Framework

## Setup

1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```

2. Navigate to the project directory:
   ```bash
   cd gptletapi
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the server:
   ```bash
   python manage.py runserver
   ```

## Usage

The project exposes several API endpoints that can be used to interact with the GPT engine:

- `GET /api/v1/apps/`: Fetch all apps
- `POST /api/v1/openai/`: Make a request to the OpenAI API

For more details, refer to the API documentation.

## License

