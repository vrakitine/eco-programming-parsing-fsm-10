import json
from flask import Flask, request, Response
from flask import render_template, flash, redirect

app = Flask(__name__)

import sys
sys.path.append('/home/evaclickparsingfsm/classes')

import fsmclasses
import dbclasses


@app.route('/', methods=['GET', 'POST'])
def index():
    real_number = str("")
    integer_part = str("")
    decimal_part = str("")
    current_state = str("s_00")
    previous_state = str("s_00")
    event = str("unknown")
    error = str("")
    tracks = []

    sql = dbclasses.SQLighter()
    fsm = fsmclasses.Fsm()
    fsm.setStateLogTable(sql)
    state_matrix = fsm.getStateMatrix()

    if 'real_number' in request.form :
        real_number = request.form['real_number']

        # define event code
        i = 0
        while i < len(real_number) + 1:
            event = "v_50"
            symbol = "unknown"

            if i < len(real_number):
                if real_number[i] in ["+","-"]:
                    event = "v_10"
                    symbol = real_number[i]

                if real_number[i] in ["0","1","2","3","4","5","6","7","8","9"]:
                    event = "v_20"
                    symbol = real_number[i]

                if real_number[i] in ["."]:
                    event = "v_30"
                    symbol = real_number[i]

            if i == len(real_number):
                event = "v_40"
                symbol = "CR"

            # define new state
            sql = dbclasses.SQLighter()
            state = fsm.getNextState(sql, current_state, event, symbol)
            previous_state = current_state
            current_state = state

            if i < len(real_number):
                tracks.append("\ni:[" + str(i) +"] | event:[" + event + "] | real_number[i]:[" + real_number[i] + "] | previous_state:[" + previous_state + "] | current_state:[" + current_state + "] ")

            if current_state in state_matrix:
                if current_state == "s_20":
                    integer_part += real_number[i]
                if current_state == "s_40":
                    decimal_part += real_number[i]
                i += 1
                continue
            break

        if current_state.find("END") != 0:
            error = 'Error state[' + current_state + ']'
            integer_part = str("")
            decimal_part = str("")


    return render_template('index.html', title='p01_case_00 - branch', real_number=real_number, integer_part=integer_part, decimal_part=decimal_part, error=error, tracks=tracks)