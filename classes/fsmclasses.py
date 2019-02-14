import json

class Fsm:

    def __init__(self):
        self.state_log_table_name = 'state_log'
        self.state_matrix_file_full_path = '/home/evaclickparsingfsm/data/fsm_matrices/fsm_matrix_p01_case_00.json'

    def getStateMatrix(self):
        with open(self.state_matrix_file_full_path, 'r') as f:
            self.state_matrix = json.load(f)

        return self.state_matrix

    def setStateLogTable(self, sql):
        sql.createStateLogTable(self.state_log_table_name)

    def getNextState(self, sql, state_current, event_code):
        state_next = self.state_matrix[state_current][event_code]
        self.appendStateLogTable(sql, state_current, event_code, state_next)

        return state_next

    def appendStateLogTable(self, sql, state_current, event_code, state_next):
        sql.insert("INSERT INTO `" + self.state_log_table_name + "` (`SL_PREVIOUS_STATE_CODE`, `SL_EVENT_CODE`, `SL_CURRENT_STATE_CODE`) VALUES ('" + state_current + "', '" + event_code + "', '" + state_next + "')")
