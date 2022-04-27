<h1 align="center">Jobs-Website-Scraper</h1>
<p>
  <a href="LICENSE" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  </a>

</p>

> The project was made using Python, Beautiful Soup and Requests.</br>
> 
> This web scraper has the purpose of scraping job offers data from the website: [JobsCompany.com](https://timesjobs.com) and creates reports in the posts folder with the available job offers according to the filter that we apply.

![page_thumbnail](https://user-images.githubusercontent.com/90936639/154578340-d207f7f9-4248-4e1e-9ed0-ce00b1fc2596.png)

## Clone Repository

```
git clone https://github.com/Fer-Bar/Jobs-Website-Scraper.git
```
## The functionalities added:
- Show a nicer output of the results
- Option to filter out jobs that do not meet some skills that are required.
- Scraping the website every 60 minutes
- Writing the results to separated text files.

## How to use it
1. Go to the directory where you want to create the project and clone the repo
2. (Optional) Create a virtual environment `venv` and activate it:
Run the module `venv` as a script with the path to the folder:
```
python3 -m venv venv
``` 
Once the virtual environment is created, you can activate it:

#### Windows Users:
```
venv\Scripts\activate.bat
``` 
#### Unix or MacOS Users:
```
source tutorial-env/bin/activate
``` 
3. Install all dependencies using `pip install -r requirements.txt`
4. You can change the time to wait between each execution of the scraper in the `main.py` file. Just set the variable `time_wait` (minutes)
5. Run the `main.py` in your console and write your unfamiliar skills in the console (use spaces between every skill that you'll write) to get better results and the scraper will be able to filter the most recent job offers as a Python Developer.

![scraper_thumbnail](https://user-images.githubusercontent.com/90936639/154587102-4311b861-9b7e-4eb4-90fe-47a97b248bb1.png)

6. Now you can see the offers in the posts folder.

![posts](https://user-images.githubusercontent.com/90936639/165430651-226df06f-22e1-4c1a-9b53-0918adf6d060.png)

## Licence

Copyright © 2021 [Fernando](https://github.com/Fer-Bar).<br />
This project is [MIT](LICENSE) licensed.

***
