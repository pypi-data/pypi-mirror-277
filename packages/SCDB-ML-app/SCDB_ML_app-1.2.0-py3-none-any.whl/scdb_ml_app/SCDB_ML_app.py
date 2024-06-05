'''
SCDB-ML-app is a deployed app to analyze the U.S. Supreme Court Database
Copyright (C) 2024  HERMES A. V. URQUIJO

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
from flask import Flask,redirect,url_for,render_template,request,jsonify,send_file # type: ignore
#to use relative paths the main program must be initiated from the parent folder as a module
from .mine_decision_tree import mine_decision_tree as mine_tree_class
from .predict_decision_tree import predict_decision_tree as predict_tree_class
from .train_decision_tree import train_decision_tree as train_tree_class
from .mining_temporal_series import miningTemporalSeries as miningTS
from .decomposing_temporal_series import decomposingTemporalSeries as decomposingTS
import time
from os import remove, getcwd
from os.path import exists,join
from numpy import savetxt, loadtxt
from pandas import DataFrame
from pathlib import Path

app = Flask(__name__)
current_directory = getcwd()
#This function basically writes the html page
@app.route("/")#url for routing
def homePage():
    #This value at the return should be changed by a html document separately created
    return render_template("index.html")

@app.route("/<some_url>")
def notFound(some_url):
    match some_url:
        case "admin":
            return redirect(url_for("admin"))
        case _:
            return render_template("notFound.html")

@app.route("/admin")
def admin():
    return "<h1>Admin page</h1>"

#Decision Treee Classifier
@app.route("/predict_tree", methods=["POST","GET"])
def predict_tree():
    if exists(Path(join(current_directory,"scdb_ml_app\\models\\accuracy_tree.txt"))):
        accuracy = loadtxt(Path(join(current_directory,"scdb_ml_app\\models\\accuracy_tree.txt")))
        visible=True
    else:
        visible=False
        accuracy=0
    if request.method == "POST":
        voteId = float(request.form["voteID"])
        issueArea = float(request.form["issueArea"])
        petitionerState = float(request.form["petitionerState"])
        respondentState = float(request.form["respondentState"])
        jurisdiction = float(request.form["jurisdiction"])
        caseOriginState = float(request.form["caseOriginState"])
        caseSourceState = float(request.form["caseSourceState"])
        certReason = float(request.form["certReason"])
        lcDisposition = float(request.form["lcDisposition"])
        try:
            predict_tree_ = predict_tree_class()  
            predict_tree_.set_predictors([voteId,issueArea,petitionerState,respondentState,jurisdiction,caseOriginState,caseSourceState,certReason,lcDisposition])      
            decisionDirection=predict_tree_.predict_self()
            return jsonify({'status':'success',
                            'redirect': url_for("predicted_tree",
                                        accuracy_visible="p_shown", 
                                        accuracy_var=f"{accuracy*100:.1f}"+"%",
                                        decisionDirection=decisionDirection,#url_for() posts a float with 1 decimal place, don't know why
                                        voteId = voteId,
                                        issueArea = issueArea,
                                        petitionerState = petitionerState,
                                        respondentState = respondentState,
                                        jurisdiction = jurisdiction,
                                        caseOriginState = caseOriginState,
                                        caseSourceState = caseSourceState,
                                        certReason = certReason,
                                        lcDisposition = lcDisposition
                                )})
        except FileNotFoundError:
            return jsonify({'status':'fileNotFound',
                            'message':'Model not found, you must train the machine first!',
                            'redirect':url_for('train_tree')
                            })
    if visible:
        return render_template("predict_tree.html",accuracy_visible="p_shown", accuracy_var=f"{accuracy*100:.1f}"+"%",decisionDirection="= Not calculated yet")
    else:
        return render_template("predict_tree.html",accuracy_visible="p_hidden", accuracy_var="0.0"+"%",decisionDirection="= Not calculated yet")

@app.route("/predicted_tree", methods=["GET","POST"])
def predicted_tree():
    remove_cache_filecsv()
    values = request.args.to_dict()
    accuracy_visible = values.get('accuracy_visible', '')
    accuracy_var = values.get('accuracy_var', '')
    voteId = float(values.get("voteId", ''))
    issueArea = float(values.get("issueArea", ''))
    petitionerState = float(values.get("petitionerState", ''))
    respondentState = float(values.get("respondentState", ''))
    jurisdiction = float(values.get("jurisdiction", ''))
    caseOriginState = float(values.get("caseOriginState", ''))
    caseSourceState = float(values.get("caseSourceState", ''))
    certReason = float(values.get("certReason", ''))
    lcDisposition = float(values.get("lcDisposition", ''))
    decisionDirection = float(values.get("decisionDirection", ''))
    if request.method=="POST":
        values_ = request.values.to_dict()
        values = {key:value for key, value in values_.items() if key!='accuracy_visible' and key!='decisionDirection'}
        values['decisionDirection']=values_['decisionDirection']
        df = DataFrame([values])  # Wrap new_values in a list to create a DataFrame with one row
        filename = Path(join(current_directory,"scdb_ml_app\\models\\predicted_decisionDirection_DTreeC.csv"))
        try:
            df.to_csv(filename, sep=';', index=False)
        except Exception as e:
            print(f"Error saving data: {e}")
        #return send_from_directory(myPath,filename,as_attachment=True)
        return send_file(filename,as_attachment=True)

    return render_template("predicted_tree.html",
                           accuracy_visible=accuracy_visible,
                           accuracy_var=accuracy_var,
                           decisionDirection=decisionDirection,
                           voteId=voteId,
                           issueArea=issueArea,
                           petitionerState=petitionerState,
                           respondentState=respondentState,
                           jurisdiction=jurisdiction,
                           caseOriginState=caseOriginState,
                           caseSourceState=caseSourceState,
                           certReason=certReason,
                           lcDisposition=lcDisposition)

@app.route("/mine_tree", methods=["POST","GET"])
def mine_tree():
    mine_tree_=mine_tree_class()
    if request.method == "POST":
        res = mine_tree_.download_file()
        mine_tree_.load_base()
        mine_tree_.preprocess()
        miningTS_ = miningTS()
        res = res and miningTS_.mine_now()
        if not res:
            print("Error de mineração")
            return jsonify({'status': 'fail', 'message':'Error while mining!', 'redirect': url_for('/')})
        return jsonify({'status': 'success', 'message':'Data mined succesfully!', 'redirect': url_for('train_tree')})
    return render_template("mine_tree.html")

@app.route("/train_tree", methods=["POST","GET"])
def train_tree():
    if request.method == "POST":
        mine_tree_=mine_tree_class()
        if not mine_tree_.verify_preprocessed():
            return jsonify({'status': 'fail', 'message':'File not found, download the file of data first', 'redirect': url_for('mine_tree')})
        max_depth = int(request.form["max_depth"])
        test_size = int(request.form["test_size"])
        random_states = int(request.form["random_states"])
        train_tree_=train_tree_class()
        accuracy = train_tree_.train(max_depth=max_depth,test_size=test_size/100.0,random_state=random_states)
        savetxt(Path(join(current_directory,"models\\accuracy_tree.txt")),[accuracy])
        # Simulate a long-running process
        time.sleep(2)
        #passos para ver se o arquivo foi baixado 
        return jsonify({'status': 'success', 'message':'Machine trained succesfully!', 'redirect': url_for('predict_tree',show_accuracy="true",accuracy_visible="p_shown",accuracy_var=f"{accuracy*100:.1f}"+"%")})
    return render_template("train_tree.html")

def remove_cache_filecsv():
    if exists(Path(join(current_directory,'scdb_ml_app\\models\\predicted_decisionDirection_DTreeC.csv'))):
        remove(Path(join(current_directory,'scdb_ml_app\\models\\predicted_decisionDirection_DTreeC.csv')))
        return True
    return False
#End Decision Tree Classifier

#Temporal series
@app.route("/temporal_series",methods=["GET","POST"])
def temporal_series():
    checkbox_status30 = False
    checkbox_status90 = False
    checkbox_status365 = False
    checkbox_status182 = True
    decomposingTS_ = decomposingTS()
    res = decomposingTS_.decompose(timePeriod=182)
    if not res:
        print("Error de no modelo")
        return render_template('temporal_series.html')
    if request.method=="POST":
        checkbox_status182=False
        decomposingTS_ = decomposingTS()
        checkBoxValue = request.form.get('timePeriod')
        match checkBoxValue:
            case "30":
                res = decomposingTS_.decompose(timePeriod=30)
                checkbox_status30 = True
            case "90":
                res = decomposingTS_.decompose(timePeriod=90)
                checkbox_status90 = True
            case "182":
                res = decomposingTS_.decompose(timePeriod=182)
                checkbox_status182 = True
            case "365":
                res = decomposingTS_.decompose(timePeriod=365)
                checkbox_status365 = True

    return render_template('temporal_series.html',
                            checkbox_status30=checkbox_status30,
                            checkbox_status90=checkbox_status90, 
                            checkbox_status182=checkbox_status182, 
                            checkbox_status365=checkbox_status365)



#End Temporal series

#Naive bayes
#End Naive bayes

#Deep Learning
#End deep learning

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
