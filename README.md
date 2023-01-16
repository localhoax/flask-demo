### Installation

Make sure you have Python 3.10 installed and configured correctly in the system path
Setup a Python 3.10 virtual environment by following the steps below

`pip install virtualenv`
`virtualenv venv`
`source venv/bin/activate` (for Powershell, run `./venv/Scripts/activate.ps1`)

To install project dependencies, run the following

> `pip install -r requirements.txt`

### Commands

To start the development server, run the following

> `python main.py`

### Read more

-   [HTTP Request Methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)
-   [HTTP Response Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
-   [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)
-   [Decorators in Python](https://www.geeksforgeeks.org/decorators-in-python/)

### Helpful links

-   Install [Postman](https://www.postman.com/downloads/) to test and document your APIs
-   To test out your API across devices install [ngrok](https://ngrok.com/download)
    After installation, run the following command to start a tunnel to your hosted application at port 3000
    > `ngrok http 3000`