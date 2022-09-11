#importing flask from framework and pets dictionary from helper.py file
from flask import Flask
from helper import pets

#creating Flask instance
app = Flask(__name__)

#creating index route
@app.route('/')
def index():
  return '''
  <h1> Adopt a Pet! </h1>
  <p> Browse through the links below to find your new furry friend: </p>
  <ul>
    <li> <a href="/animals/dogs"> Dogs </a> </li>
    <li> <a href="/animals/cats"> Cats </a> </li>
    <li> <a href="/animals/rabbits"> Rabbits </a> </li>
  </ul>
  '''

#creating animals route
@app.route('/animals/<pet_type>')
def animals(pet_type):
  html = f"<h1>List of {pet_type}"
  #creates a loop that will go through each pet and call their name and list the results
  html += "<ul>"
  #in order to get the index position, enumerate is used to simultaneously loop over indices
  #the syntax for enumerate is for idx, item in enumerate(iterable)
  for idx, item in enumerate(pets[pet_type]):
    html += "<li>" + f'<a href="/animals/{pet_type}/{idx}">' + item["name"] +"</a></li>"
  html += "</ul>"
  return f'''
    {html}
  '''

#creates pet id route
@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
  pet =  pets[pet_type][pet_id] #pulls pet id by calling the index from the dictionary
  return f'''
  <h1>My name is: {pet["name"]}</h1>
  <img src="{pet["url"]}"></img>
  <p>{pet["description"]}</p>
  <ul> 
    <li>Age - {pet["age"]}</li>
    <li>Breed - {pet["breed"]}</li>
  <ul>
  '''
