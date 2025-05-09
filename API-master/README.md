# Robot-Eye Flask API
This API is for connect mobile app with rasbperry pi

## Local
Clone the repository in a folder:
```
git clone git@github.com:Project-Eye-Robot/API.git
```
Create a venv (outside project) and source:
```
python3 -m venv venv
source venv/bin/activate
```
Install Flask:
```
pip install Flask
```
run python script (the default port is 80 but I change it locally with 1234):
```
cd API/
python app.py
```
### Routes:
- localhost:1234
- localhost:1234/testGet
- localhost:1234/testPost (need json body)

## Rasbperry
Inside rasbperry run the python script
```
cd /API
source venv/bin/activate
cd /api-app
sudo python app.py
```
### Routes (access remotly):
- https://pentastyle-gull-3744.dataplicity.io
- https://pentastyle-gull-3744.dataplicity.io/testGet
- https://pentastyle-gull-3744.dataplicity.io/testPost (need json body)