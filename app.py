from flask import Flask, render_template
import json

app= Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
	data = { 
		"summary":{
			"under40":0.6,
      		"exactly40":0.2,
      		"over40":0.2
   			}
		}
	
	return render_template('home.html', datas=data)



if __name__ == '__main__':
	app.run(debug=True)