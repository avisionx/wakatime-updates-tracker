<p align="center">
  <img src="https://user-images.githubusercontent.com/32339251/94999375-8ce6ac80-05d6-11eb-8fa4-73b1559f6c75.png" alt="" width="160" height="160">
  <h3 align="center">WakaTime Updates Tracker</h3>
    
  <p align="center"><img src="https://img.shields.io/github/workflow/status/avisionx/wakatime-updates-tracker/Generate WakaData from Email?style=flat-square"> <img src="https://img.shields.io/badge/hacktoberfest-2020-ff69b4.svg?style=flat-square" /> <img src="https://img.shields.io/github/issues-raw/avisionx/wakatime-updates-tracker?style=flat-square"> <img src="https://hitcounter.pythonanywhere.com/count/tag.svg?url=https%3A%2F%2Fgithub.com%2Favisionx%2Fwakatime-updates-tracker" alt="Hits" /> <img src="https://img.shields.io/github/languages/count/avisionx/wakatime-updates-tracker?style=flat-square"> <img src="https://img.shields.io/github/languages/code-size/avisionx/wakatime-updates-tracker?style=flat-square"> <img src="https://img.shields.io/github/stars/avisionx/wakatime-updates-tracker?style=flat-square"> <img src="https://img.shields.io/github/contributors/avisionx/wakatime-updates-tracker?style=flat-square"> </p>

  <p align="center">
    This repository stores and compiles WakaTime Languages and Projects data from emails and saves the stats ✨
    </br>
    <a href="https://github.com/avisionx/wakatime-updates-tracker/#table-of-contents"><strong>Explore the docs »</strong></a><br/>
    <a href="https://github.com/avisionx/wakatime-updates-tracker/issues">Report Bug</a>
    .
    <a href="https://github.com/avisionx/wakatime-updates-tracker/issues">Request Feature</a>
  </p>
</p>  

<!-- TABLE OF CONTENTS -->
## Table of Contents
* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)

<!-- ABOUT THE PROJECT -->
## About The Project
There are a lot of WakaTime stats tracker for Github Readme available online, however, I didn't find one that uses email gist sent by WakaTime to commulate all the stats. 

Here's why:
* WakaTime stats for months, years...
* Free account supported :smile:

### Built With
This project was built with python3 and is powered by github actions for cron job tasks.

<!-- GETTING STARTED -->
## Getting Started
To get up and running with this project on your local machine follow these simple steps.

### Prerequisites
Here's a list of things you'll need to have prior to generating the stats
* Gmail account with all WakaTime report, refer to screenshot in [Installation Section](#installation)
* Label of `wakatime` added to all the report emails 
* Python v3+
> To download python3+ visit [https://www.python.org/downloads/](https://www.python.org/downloads/)

### Installation
1. Clone the repo
```sh
$ git clone https://github.com/avisionx/wakatime-updates-tracker.git
```
2. Install python packages
```sh
$ pip install -r requirements.txt
```
3. Setup an email id on gmail with all the wakatime update emails they look like as shown below, and add label of `wakatime` to all of them.
![WakaTimeEmailSS](https://user-images.githubusercontent.com/32339251/94999781-51011680-05d9-11eb-8ae2-126f2dbf7a29.png)
4. Create a .env file for local or Github Secrets
```sh
EMAIL_ID = your_gmail_email_id@gmail.com
EMAIL_PASSWORD = your_emails_password
```
5. Run the `main.py` file
```sh
$ python main.py
```

<!-- ROADMAP -->
## Roadmap
See the [open issues](https://github.com/avisionx/wakatime-updates-tracker/issues) for a list of proposed features (and known issues).

<!-- CONTRIBUTING -->
## Contributing
Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License
Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->
## Contact
Avi Garg - [https://avisionx.net/](https://avisionx.net/) - hello@avisionx.net

Project Link: [https://github.com/avisionx/wakatime-updates-tracker](https://github.com/avisionx/wakatime-updates-tracker)
