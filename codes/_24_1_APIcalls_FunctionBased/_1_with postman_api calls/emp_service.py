

from emp_dao import create_erecord, check_eid

def save_data(edata):
    print("SERVICE: Get Data : ", edata)
    # 1. Business Logic Implementation
    '''
        1. Check empid exists or not 
        2. Add datetimestamp, Country, State, location
    '''
    resp = check_eid(edata['emp_id'])
    if resp:
        edata['datetime'] = '10thJuly2023MON'
        edata['Country'] = "India"
        edata['State'] = 'Karnataka'
        edata['location'] = 'AECS Layout'
        # 2. Pass to DAO Layer
        resp = create_erecord(edata)
        return resp
    else:
        return "Employee already exists"