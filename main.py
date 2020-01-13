from flask import Flask, request, render_template, send_from_directory
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Setup Firebase service account
cred = credentials.Certificate("REMOVED KEY DUE TO SECURITY")
firebase_admin.initialize_app(cred)

db = firestore.client()

#Explaining Imports: Flask - Html support | requests - used to take text area | render_template - opening html files |

app = Flask(__name__)

#===Dummy Data===#
first_name = ''
last_name = ''
return_text = ''


@app.route('/') #creates a new webpage
@app.route('/home') #stacked so multiurl links to same place
def home():
    return render_template('home.html') #render_templates renders html file in /templates


@app.route('/css/<path>')
def send_style(path):
    return send_from_directory('css', path)

@app.route('/home', methods=['POST']) 
def submit():
    first_name = '{}'.format(request.form['textInput']) #grab text from textarea in html
    last_name = '{}'.format(request.form['textInpu  t2'])

    # send to firebase
    doc_ref = db.collection(u'users').document(first_name[0] + last_name)
    doc_ref.set({
        u'first': first_name,
        u'last': last_name,
    })

    first_name = first_name.upper() #processing could happen here
    last_name = last_name.upper()

    print(first_name)
    print(last_name)
    return render_template('home.html', return_text=first_name + ' ' + last_name) #this loads first_name into the html file. neat.

@app.route('/box')
def box():
  return render_template('box.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0', port = 8080)

#debug mode does not work with repl.it
  

