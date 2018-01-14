from flask import (Flask, render_template, redirect,
                   url_for, request, make_response)
from file_management import getImagesLabellingList, writeNewRow
from options import GROUP_1
from options_race import RACE_Dict
from options_att import ATTRACTIVENESS_dict
import time
import outfit_management as om
import outfit_management_race as omr
import outfit_management_att as oma
import random
app = Flask(__name__)

group_1_count = 0
race_count = 0
attractiveness_count = 0
#image folder path
Group_1PATH = 'static/Pics/' 


imageList = list()

@app.route('/')
def index():
    return render_template('home.html')
@app.route('/complete')
def complete():
    random_number = random.randint(10000000, 99999999)
    return render_template('complete.html',random_number=random_number)

@app.route('/save_Group_1', methods=['POST'])
def save_Group_1():
    global group_1_count
    group_1_count += 48
    if group_1_count==len(imageList):
        group_1_count=0
        response = make_response(redirect(url_for('complete')))
        return response
    response = make_response(redirect(url_for('group_1')))
    #Saves labels to CSV file
    labelledDict = dict(request.form.items()) #request the POST-ed info
    print(labelledDict)
    om.writeNewRow(dict(request.form.items()), 'Group_1')
    return response

@app.route('/save_RACE', methods=['POST'])
def save_RACE():
    global race_count
    race_count += 48
    if race_count==len(imageList):
        race_count=0
        response = make_response(redirect(url_for('complete')))
        return response
    response = make_response(redirect(url_for('RACE')))
    #Saves labels to CSV file
    labelledDict = dict(request.form.items()) #request the POST-ed info
    print(labelledDict)
    omr.writeNewRow(dict(request.form.items()), 'Race')
    
    return response

@app.route('/save_ATTRACTIVENESS', methods=['POST'])
def save_ATTRACTIVENESS():
    global attractiveness_count
    attractiveness_count += 48
    if attractiveness_count==len(imageList):
        attractiveness_count=0
        response = make_response(redirect(url_for('complete')))
        return response
    response = make_response(redirect(url_for('ATTRACTIVENESS')))
    #Saves labels to CSV file
    labelledDict = dict(request.form.items()) #request the POST-ed info
    print(labelledDict)
    oma.writeNewRow(dict(request.form.items()), 'Attractiveness')
    
    return response
#TODO: Write new images into top.csv bottom.csv and shoes.csv as well


@app.route('/RACE')
def RACE():
    global imageList
    if len(imageList) == 0:
        imageList = om.getImagesLabellingList()
    else:
        print("Images Left:", len(imageList)-race_count)

    return render_template('race.html',
        imageDict=imageList[race_count],
        imageDict2=imageList[race_count+1],
        imageDict3=imageList[race_count+2],
        imageDict4=imageList[race_count+3],
        imageDict5=imageList[race_count+4],
        imageDict6=imageList[race_count+5],
        imageDict7=imageList[race_count+6],
        imageDict8=imageList[race_count+7],
        imageDict9=imageList[race_count+8],
        imageDict10=imageList[race_count+9],
        imageDict11=imageList[race_count+10],
        imageDict12=imageList[race_count+11],
        imageDict13=imageList[race_count+12],
        imageDict14=imageList[race_count+13],
        imageDict15=imageList[race_count+14],
        imageDict16=imageList[race_count+15],
        imageDict17=imageList[race_count+16],
        imageDict18=imageList[race_count+17],
        imageDict19=imageList[race_count+18],
        imageDict20=imageList[race_count+19],
        imageDict21=imageList[race_count+20],
        imageDict22=imageList[race_count+21],
        imageDict23=imageList[race_count+22],
        imageDict24=imageList[race_count+23],
        imageDict25=imageList[race_count+24],
        imageDict26=imageList[race_count+25],
        imageDict27=imageList[race_count+26],
        imageDict28=imageList[race_count+27],
        imageDict29=imageList[race_count+28],
        imageDict30=imageList[race_count+29],
        imageDict31=imageList[race_count+30],
        imageDict32=imageList[race_count+31],
        imageDict33=imageList[race_count+32],
        imageDict34=imageList[race_count+33],
        imageDict35=imageList[race_count+34],
        imageDict36=imageList[race_count+35],
        imageDict37=imageList[race_count+36],
        imageDict38=imageList[race_count+37],
        imageDict39=imageList[race_count+38],
        imageDict40=imageList[race_count+39],
        imageDict41=imageList[race_count+40],
        imageDict42=imageList[race_count+41],
        imageDict43=imageList[race_count+42],
        imageDict44=imageList[race_count+43],
        imageDict45=imageList[race_count+44],
        imageDict46=imageList[race_count+45],
        imageDict47=imageList[race_count+46],
        imageDict48=imageList[race_count+47],
        options=RACE_Dict)

@app.route('/ATTRACTIVENESS')
def ATTRACTIVENESS():
    global imageList
    if len(imageList) == 0:
        imageList = om.getImagesLabellingList()
    else:
        print("Images Left:", len(imageList)-attractiveness_count)

    return render_template('attractiveness.html',
        imageDict=imageList[attractiveness_count],
        imageDict2=imageList[attractiveness_count+1],
        imageDict3=imageList[attractiveness_count+2],
        imageDict4=imageList[attractiveness_count+3],
        imageDict5=imageList[attractiveness_count+4],
        imageDict6=imageList[attractiveness_count+5],
        imageDict7=imageList[attractiveness_count+6],
        imageDict8=imageList[attractiveness_count+7],
        imageDict9=imageList[attractiveness_count+8],
        imageDict10=imageList[attractiveness_count+9],
        imageDict11=imageList[attractiveness_count+10],
        imageDict12=imageList[attractiveness_count+11],
        imageDict13=imageList[attractiveness_count+12],
        imageDict14=imageList[attractiveness_count+13],
        imageDict15=imageList[attractiveness_count+14],
        imageDict16=imageList[attractiveness_count+15],
        imageDict17=imageList[attractiveness_count+16],
        imageDict18=imageList[attractiveness_count+17],
        imageDict19=imageList[attractiveness_count+18],
        imageDict20=imageList[attractiveness_count+19],
        imageDict21=imageList[attractiveness_count+20],
        imageDict22=imageList[attractiveness_count+21],
        imageDict23=imageList[attractiveness_count+22],
        imageDict24=imageList[attractiveness_count+23],
        imageDict25=imageList[attractiveness_count+24],
        imageDict26=imageList[attractiveness_count+25],
        imageDict27=imageList[attractiveness_count+26],
        imageDict28=imageList[attractiveness_count+27],
        imageDict29=imageList[attractiveness_count+28],
        imageDict30=imageList[attractiveness_count+29],
        imageDict31=imageList[attractiveness_count+30],
        imageDict32=imageList[attractiveness_count+31],
        imageDict33=imageList[attractiveness_count+32],
        imageDict34=imageList[attractiveness_count+33],
        imageDict35=imageList[attractiveness_count+34],
        imageDict36=imageList[attractiveness_count+35],
        imageDict37=imageList[attractiveness_count+36],
        imageDict38=imageList[attractiveness_count+37],
        imageDict39=imageList[attractiveness_count+38],
        imageDict40=imageList[attractiveness_count+39],
        imageDict41=imageList[attractiveness_count+40],
        imageDict42=imageList[attractiveness_count+41],
        imageDict43=imageList[attractiveness_count+42],
        imageDict44=imageList[attractiveness_count+43],
        imageDict45=imageList[attractiveness_count+44],
        imageDict46=imageList[attractiveness_count+45],
        imageDict47=imageList[attractiveness_count+46],
        imageDict48=imageList[attractiveness_count+47],
        options=ATTRACTIVENESS_dict)

@app.route('/group_1')
def group_1():
    global imageList
    if len(imageList) == 0:
        imageList = om.getImagesLabellingList()
    else:
        print("Images Left:", len(imageList)-group_1_count)

    return render_template('group_1.html',
        imageDict=imageList[group_1_count],
        imageDict2=imageList[group_1_count+1],
        imageDict3=imageList[group_1_count+2],
        imageDict4=imageList[group_1_count+3],
        imageDict5=imageList[group_1_count+4],
        imageDict6=imageList[group_1_count+5],
        imageDict7=imageList[group_1_count+6],
        imageDict8=imageList[group_1_count+7],
        imageDict9=imageList[group_1_count+8],
        imageDict10=imageList[group_1_count+9],
        imageDict11=imageList[group_1_count+10],
        imageDict12=imageList[group_1_count+11],
        imageDict13=imageList[group_1_count+12],
        imageDict14=imageList[group_1_count+13],
        imageDict15=imageList[group_1_count+14],
        imageDict16=imageList[group_1_count+15],
        imageDict17=imageList[group_1_count+16],
        imageDict18=imageList[group_1_count+17],
        imageDict19=imageList[group_1_count+18],
        imageDict20=imageList[group_1_count+19],
        imageDict21=imageList[group_1_count+20],
        imageDict22=imageList[group_1_count+21],
        imageDict23=imageList[group_1_count+22],
        imageDict24=imageList[group_1_count+23],
        imageDict25=imageList[group_1_count+24],
        imageDict26=imageList[group_1_count+25],
        imageDict27=imageList[group_1_count+26],
        imageDict28=imageList[group_1_count+27],
        imageDict29=imageList[group_1_count+28],
        imageDict30=imageList[group_1_count+29],
        imageDict31=imageList[group_1_count+30],
        imageDict32=imageList[group_1_count+31],
        imageDict33=imageList[group_1_count+32],
        imageDict34=imageList[group_1_count+33],
        imageDict35=imageList[group_1_count+34],
        imageDict36=imageList[group_1_count+35],
        imageDict37=imageList[group_1_count+36],
        imageDict38=imageList[group_1_count+37],
        imageDict39=imageList[group_1_count+38],
        imageDict40=imageList[group_1_count+39],
        imageDict41=imageList[group_1_count+40],
        imageDict42=imageList[group_1_count+41],
        imageDict43=imageList[group_1_count+42],
        imageDict44=imageList[group_1_count+43],
        imageDict45=imageList[group_1_count+44],
        imageDict46=imageList[group_1_count+45],
        imageDict47=imageList[group_1_count+46],
        imageDict48=imageList[group_1_count+47],
        options=GROUP_1)
app.run(debug=True, port=3000, host='0.0.0.0')
