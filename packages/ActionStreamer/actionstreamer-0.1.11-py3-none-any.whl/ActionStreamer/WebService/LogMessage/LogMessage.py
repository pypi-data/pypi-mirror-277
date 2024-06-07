import CommonFunctions
import datetime
import json
from ActionStreamer import DateTimeEncoder

def CreateLogMessage(logConfig, strMessage, bLogToConsole=True):

    try:
        if (bLogToConsole):
            CommonFunctions.Log(strMessage, logConfig.agentName)

        utc_now = datetime.datetime.now(datetime.timezone.utc)
        jsonPostData = {"deviceSerial":logConfig.deviceSerial, "agentType":logConfig.agentType, "agentVersion":logConfig.agentVersion, "agentIndex":logConfig.agentIndex, "processID":logConfig.processID, "message":strMessage, "logDate": utc_now}

        method = "POST"
        path = 'v1/logmessage'
        url = logConfig.wsConfig.base_url + path
        headers = {"Content-Type": "application/json"}
        parameters = ''
        #body = json.dumps(jsonPostData)
        body = json.dumps(jsonPostData, indent=4, cls=DateTimeEncoder)

        intResponseCode, strResponse = CommonFunctions.send_signed_request(logConfig.wsConfig, method, url, path, headers, parameters, body)

    except Exception as ex:
        
        filename, line_number = CommonFunctions.get_exception_info()
        if filename is not None and line_number is not None:
            print(f"Exception occurred at line {line_number} in {filename}")
        print(ex)

        intResponseCode = -1
        strResponse = "Exception in CreateLogMessage"

    return intResponseCode, strResponse