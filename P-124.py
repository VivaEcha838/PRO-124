from flask import Flask, jsonify, request

app = Flask(__name__)
list = [
    {
        "id": 1,
        "name": "Waleed",
        "Contact": "8764839376",

    }, 
    {
        "id": 2,
        "name": "Saurav",
        "Contact": "9384763546",

    }

]

@app.route("/add-contact", methods = ['POST'])
def add_contact():
    if not request.json:
        return jsonify({
            "Status": "Error",
            "Error": "Please provide proper format"
        })
    contact = {
        "id": list[-1]['id']+1,
        "name": request.json['name'],
        "Contact": request.json.get('Contact'),
    }
    list.append(contact)
    return jsonify({
            "Status": "Success",
            "Msg": "Added Successfully"
        })
@app.route('/get-contact')
def get_contact():
    return jsonify({
        'data': list
    })
if(__name__ == "__main__"):
    app.run(debug=True)
    
