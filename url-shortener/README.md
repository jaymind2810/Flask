<div align="center">

[//]: # (<img width="30%" src="https://user-images.githubusercontent.com/fav.PNG">)

# URl Shortener
</div>

### Cloning the repository

--> Clone the repository using the command below :
```bash
git clone https://github.com/jaymind2810/url-shortener.git
```

--> Move into the directory where we have the project files : 
```bash
cd url-shortener
```

--> Create a virtual environment :
```bash
# Let's install virtualenv first
sudo apt install python3-venv

# Then we create our virtual environment
python3 -m venv venv
```

--> Activate the virtual environment :
```bash
source venv/bin/activate
```

--> Install the requirements :
```bash
pip install -r requirements.txt
```

#

### Running the App
    
--> To run the App, we use :
```bash
export FLASK_APP=urlshortner.py
export FLASK_ENV=development
flask run
```

- Then, the development server will be started at http://127.0.0.1:5000/

