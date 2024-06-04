import logging, time, datetime, sys, socket, random, tzlocal, glob, fnmatch
import platform
from collections import deque
from datetime import datetime
from cpppo.server.enip import address, client
import os
import configparser
import requests
import json

VERSION = "2.9"

# config
CONFIG_SERVER_ADDRESS = ""
CONFIG_USERNAME = ""
CONFIG_PASSWORD = ""

TAGS_DEFINITION_FILE_NAME = "TagsDefinition.txt"
GET_TAGS_FROM_SERVER_MIN_RATE_SECONDS = 10
GET_CLOUD_VERSION_FROM_SERVER_MIN_RATE_SECONDS = 10
VERIFY_SSL = False  # True = do not allow un verified connection , False = Allow

SUGGESTED_UPDATE_VERSION = ""
CONFIG_FILE = "config.ini"
SCAN_RATE_LAST_READ = {}
CURRENT_TOKEN = ""
CONNECTOR_TYPE_NAME = ""
LAST_GET_TAGS_FROM_SERVER = None
LAST_GET_CLOUD_VERSION_FROM_SERVER = None

def enum(**enums):
    return type("Enum", (), enums)

TagStatus = enum(Invalid=10, Valid=20)

# Retrieve the logger instance
logger = logging.getLogger(__name__)


# ============================
def read_last_rows_from_log(max_number_of_rows=10):
    log_file_path = "CloudConnectorService.log"
    if os.path.exists(log_file_path):
        with open(log_file_path, "r") as file:
            last_rows = deque(file, maxlen=max_number_of_rows)

        return list(map(str.rstrip, last_rows))
    return None

# ============================
def setLogLevel(lvl):
    try:
        if str(lvl) in ["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG", "NOTSET"]:
            lvl = logging.getLevelName(str(lvl))

    except Exception as inst:
        print("Error in setLogLevel", inst)


# ============================
def ci_print(msg, level=""):
    try:

        if level == "DEBUG":
            logger.debug(msg)
        elif level == "INFO":
            logger.info(msg)
        elif level == "ERROR":
            logger.error(msg)
        elif level == "WARNING":
            logger.warning(msg)
        else:
            logger.info(msg)

    except Exception as e:
        logger.warning(f"An error occurred while logging: {e}")


# ============================
def SendLogToServer(log):
    try:
        addCloudConnectorLog(log, datetime.now())
        return
    except Exception as e:
        return



# ============================
def handleError(message, err):
    try:

        err_desc = str(err)
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.basename(exc_tb.tb_frame.f_code.co_filename)
        srtMsg = (
            f"{message} , {err_desc} , {exc_type} , {fname} , {exc_tb.tb_lineno}"
        )
        ci_print(srtMsg, "ERROR")
    except Exception as inner_err:
        ci_print(f"Error in handleError: {inner_err}", "ERROR")


# ============================
def getAliveFile():
    ret = None
    try:
        file_path = "lc_pid.txt"
        with open(file_path, "r") as file:
            ret = json.load(file)
    except Exception as e:
        handleError("Error reading alive file: %s", e)
    return ret


# ============================

def initialize_config(overwrite=False):

    global CONFIG_SERVER_ADDRESS
    global CONFIG_USERNAME
    global CONFIG_PASSWORD


    try:
        file_path = f"{CONFIG_FILE}"

        if os.path.exists(file_path) and not overwrite:
            config = configparser.ConfigParser()
            config.read(file_path)

            CONFIG_SERVER_ADDRESS = config.get("Server", "Address")
            CONFIG_USERNAME = config.get("Server", "username")
            CONFIG_PASSWORD = config.get("Server", "password")


            ci_print(f"Server Address: {CONFIG_SERVER_ADDRESS}", "INFO")
            ci_print(f"Username: {CONFIG_USERNAME}", "INFO")
            ci_print(f"Password: {CONFIG_PASSWORD}", "INFO")
            ci_print(f"VERSION: {getLocalVersion()}")

        else:
            ci_print(f"Config not found or overwrite is True, creating new one in {file_path}", "INFO")
            config = configparser.ConfigParser()
            config.add_section("Server")
            config.add_section("Logging")

            def get_input(prompt, current_value):
                value = input(prompt + f" (Currently: {current_value}): ")
                return value if value else current_value

            CONFIG_SERVER_ADDRESS = get_input("Enter Server Address (e.g., https://localhost:63483)", CONFIG_SERVER_ADDRESS)
            CONFIG_USERNAME = get_input("Enter new user name", CONFIG_USERNAME)
            CONFIG_PASSWORD = get_input("Enter password", CONFIG_PASSWORD)

            config.set("Server", "Address", CONFIG_SERVER_ADDRESS)
            config.set("Server", "username", CONFIG_USERNAME)
            config.set("Server", "password", CONFIG_PASSWORD)


            with open(file_path, "w") as configfile:
                config.write(configfile)

            initialize_config()  # Reload the config after updating

    except Exception as inst:
        handleError("Error in initialize_config", inst)


# ============================
def reboot():

    try:
        if platform.system() == "Windows":
            ci_print("Reboot not supported on Windows.", "INFO")
            #subprocess.run(["shutdown", "/r", "/t", "0"], check=True)
        else:
            ci_print("Reboot not supported on !Windows.", "INFO")
            #os.system("sudo reboot")
    except Exception as ex:
        handleError("Error in reboot", ex)



# Cloud Functions
# ============================

CONFIG_SERVER_ADDRESS = "your_server_address"
VERIFY_SSL = True
CURRENT_TOKEN = ""
CONFIG_USERNAME = "your_username"
CONFIG_PASSWORD = "your_password"


def get_cloud_token():

    global CONFIG_SERVER_ADDRESS
    global VERIFY_SSL
    global CURRENT_TOKEN

    if CURRENT_TOKEN:
        return CURRENT_TOKEN

    url = f"{CONFIG_SERVER_ADDRESS}/api/CloudConnector/Token"

    try:
        response = requests.post(
            url,
            data={
                "grant_type": "password",
                "username": CONFIG_USERNAME,
                "password": CONFIG_PASSWORD,
            },
            headers={
                "User-Agent": "python",
                "Content-Type": "application/x-www-form-urlencoded",
            },
            verify=VERIFY_SSL,
        )

        response.raise_for_status()  # Raises an HTTPError for bad responses
        data = response.text

        jsonData = json.loads(data)
        token = jsonData.get("access_token", "")

        if token:
            CURRENT_TOKEN = token

    except requests.exceptions.RequestException as e:
        handleError("Error getting Token", e)
        token = ""
    except json.JSONDecodeError as e:
        handleError("Error decoding token response", e)
        token = ""
    except KeyError as e:
        handleError("Token not found in response", e)
        token = ""

    return token


# ============================
# make http request to cloud if fails set CURRENT_TOKEN='' so it will be initialized next time
# ============================
def ciRequest(url, data, method="get", action="", token=""):

    result = {"isOK": False}
    global CURRENT_TOKEN

    if not token:
        ci_print(f"Skipping {action} - no Token")
        return result

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "text/plain"
    }

    if method.lower() == "post":
        headers["Content-Type"] = "application/json"

    try:
        if method.lower() == "post":
            ci_print(f"{datetime.now()}, ciRequest url: {url} action: {action}, data: {data}")
            response = requests.post(url, data=data, headers=headers, verify=VERIFY_SSL)
        else:
            ci_print(f"{datetime.now()}, ciRequest url: {url} action: {action}")
            response = requests.get(url, headers=headers, verify=VERIFY_SSL)

        if response.status_code == 403:
            CURRENT_TOKEN = ""

        result["isOK"] = response.status_code == 200
        result["response"] = response

    except Exception as err:
        handleError(f"Error in ci_request {action}", err)
        CURRENT_TOKEN = ""

    return result


# ============================
def get_cloud_version():

    global GET_CLOUD_VERSION_FROM_SERVER_MIN_RATE_SECONDS
    global LAST_GET_CLOUD_VERSION_FROM_SERVER
    global CURRENT_TOKEN
    global VERSION
    global SUGGESTED_UPDATE_VERSION

    if CURRENT_TOKEN == "":
        CURRENT_TOKEN = get_cloud_token()

    token = CURRENT_TOKEN

    tags = None

    try:
        now = datetime.now()
        getVersionTimePass = 0

        if LAST_GET_CLOUD_VERSION_FROM_SERVER:
            getVersionTimePass = (now - LAST_GET_CLOUD_VERSION_FROM_SERVER).total_seconds()

        if getVersionTimePass == 0 or getVersionTimePass > GET_CLOUD_VERSION_FROM_SERVER_MIN_RATE_SECONDS:

            handleNewRequests()

            LAST_GET_CLOUD_VERSION_FROM_SERVER = datetime.now()
            ip_address = socket.gethostbyname(socket.gethostname())
            url = f"{CONFIG_SERVER_ADDRESS}/api/CloudConnector/GetVersion/?version={VERSION}&IpAddress={ip_address}"

            ret = ciRequest(url, None, "get", "getCloudVersion", token)
            response = ret["response"]

            if not ret["isOK"]:
                return ""

            ans = json.loads(response.text)
            update_to_version = ans[0]

            SUGGESTED_UPDATE_VERSION = update_to_version

            if bool(update_to_version) != "" and bool(update_to_version != VERSION):
                ci_print(f"Local Version: {VERSION} but Server suggests Other Version: {update_to_version}", "INFO")

    except Exception as err:
        print(str(err))
        handleError("Error getting Version from cloud", err)
        SUGGESTED_UPDATE_VERSION = ""

    return SUGGESTED_UPDATE_VERSION


# ============================
def get_cloud_tags(token=""):

    global LAST_GET_TAGS_FROM_SERVER
    global GET_TAGS_FROM_SERVER_MIN_RATE_SECONDS

    try:
        url = f"{CONFIG_SERVER_ADDRESS}/api/CloudConnector/GetTags/"

        tags = None

        now = datetime.now()
        getTagsTimePass = 0

        if LAST_GET_TAGS_FROM_SERVER:
            getTagsTimePass = (now - LAST_GET_TAGS_FROM_SERVER).total_seconds()

        if getTagsTimePass == 0 or getTagsTimePass > GET_TAGS_FROM_SERVER_MIN_RATE_SECONDS:
            ret = ciRequest(url, None, "get", "getCloudTags", token)
            if ret and ret["isOK"] == True:
                response = ret["response"]
                LAST_GET_TAGS_FROM_SERVER = datetime.now()
                ans = json.loads(response.text)
                arranged_tags = arrange_tags_by_scan_time(ans["Tags"])
                tags = {"Tags": arranged_tags}

                with open(TAGS_DEFINITION_FILE_NAME, "w") as f:
                    json.dump(tags, f)

            else:
                ci_print("Failed to retrieve Tags from Cloud server", "WARNING")
    except Exception as inst:
        print(str(inst))
        handleError("Error getting tags from cloud", inst)
        tags = None

    if tags == None:
        tags = get_tags_definition_from_file()

    return tags


# ============================
def arrange_tags_by_scan_time(tags):
    ans = {}

    try:
        for index in range(len(tags)):
            scan_rate = tags[index]["ScanRate"]

            if scan_rate in ans:
                tagsListPerScanRate = ans[scan_rate]
            else:
                ans[scan_rate] = []

            ans[scan_rate].append(tags[index])
    except Exception as err:
        handleError("Error arranging tags by scan time", err)
    return ans


# ============================
def printTags(tags):
    try:
        ci_print(str(tags))

        for tag in tags:
            tag_id = tag.get("TagId", "")
            tag_name = tag.get("TagName", "")
            tag_address = tag.get("TagAddress", "")
            scan_rate = tag.get("ScanRate", "")

            msg = f"Tag Id: {tag_id}, TagName: {tag_name}, TagAddress: {tag_address}, ScanRate: {scan_rate}"
            ci_print(msg, "INFO")

    except Exception as inst:
        handleError("Error in printTags", inst)


# ============================
def set_cloud_tags(tag_values, token=""):
    global TagStatus
    updated_successfully = False

    try:
        url = f"{CONFIG_SERVER_ADDRESS}/api/CloudConnector/SetCounterHistory/"
        payload = []

        for tag in tag_values:
            tag_id = tag.get("TagId")
            timestamp = str(tag.get("time"))
            value = tag.get("value")
            status = TagStatus.Valid if str(tag.get("status")) == "20" else TagStatus.Invalid

            tag_val = {
                "TagId": tag_id,
                "TimeStmp": timestamp,
                "StatusCE": status,
                "Value": value,
            }
            payload.append(tag_val)

        ret = ciRequest(url, json.dumps(payload), "post", "setCloudTags", token)
        response = ret["response"]

        updated_successfully = response.status_code == 200

    except Exception as inst:
        handleError("Error setting tags in cloud", inst)
        return False

    return updated_successfully


# ============================
def sendLogFileToCloud(numberOfRows=10, timestamp="", requestId=""):

    try:
        requestId = str(requestId)
        lines = read_last_rows_from_log(numberOfRows)
        for line in lines:
            addCloudConnectorLog(line, timestamp, str(requestId))
    except Exception as inst:
        handleError("sendLogFileToCloud: Error setting tags in cloud", inst)
        return False


# ============================
def addCloudConnectorLog(log, timestamp="", request_id=""):

    global CURRENT_TOKEN
    if timestamp == "":
        timestamp = datetime.now()

    token = CURRENT_TOKEN
    if token == "":
        return


    try:
        url = CONFIG_SERVER_ADDRESS + "/api/CloudConnector/SetCounterLog/"

        payload = []
        payload = [{"Log": log, "TimeStamp": str(timestamp), "RequestId": request_id}]
        ret = ciRequest(url, json.dumps(payload), "post", "SetConnectorLog", token)
        response = ret["response"]

        return response.status_code == 200

    except Exception as inst:
        handleError("Exception in addCloudConnectorLog", inst)
        return False


# ============================
def getCloudConnectorRequests():

    global CURRENT_TOKEN
    token = CURRENT_TOKEN


    ans = None
    try:
        url = CONFIG_SERVER_ADDRESS + "/api/CloudConnector/GetCloudConnectorRequests/"
        ret = ciRequest(url, None, "get", "GetCloudConnectorRequests", token)

        response = ret["response"]
        if ret["isOK"] == True:
            ans = json.loads(response.text)
    except Exception as inst:
        handleError("Error getting requests from cloud", inst)
        ans = None

    return ans


# ============================
def updateCloudConnectorRequests(requestId, status):

    global CURRENT_TOKEN
    updatedSuccessfully = False

    token = CURRENT_TOKEN
    if token == "":
        ci_print("no token skip updateCloudConnectorRequests", "WARNING")
        return
    try:
        url = (
            CONFIG_SERVER_ADDRESS
            + "/api/CloudConnector/SetCounterRequestStatus/?requestId="
            + str(requestId)
            + "&status="
            + str(status)
        )

        ret = ciRequest(url, "", "post", "SetCounterRequestStatus", token)
        response = ret["response"]

        updatedSuccessfully = response.status_code == 200

    except Exception as inst:
        handleError("Exception in addCloudConnectorLog", inst)
        return False

    return updatedSuccessfully


# get requests from cloud and handle it
# ============================
def handleNewRequests():

    try:
        requests = getCloudConnectorRequests()
        if requests:

            for request in requests:
                try:
                    if request["Type"] == 1:  # send logs
                        requestData = json.loads(request["Data"])
                        rownCount = requestData["Rows"]
                        ret = updateCloudConnectorRequests(request["Id"], 2)  # in process
                        requestData = json.loads(request["Data"])
                        sendLogFileToCloud(rownCount, "", request["Id"])
                        ret = updateCloudConnectorRequests(request["Id"], 3)  # Done
                    if request["Type"] == 2:  # change logs level
                        ci_print(
                            "Handling change log level request " + str(request), "INFO"
                        )
                        requestData = json.loads(request["Data"])
                        newLogLevel = requestData["Level"]
                        ret = updateCloudConnectorRequests(request["Id"], 2)  # in process
                        setLogLevel(newLogLevel)
                        ret = updateCloudConnectorRequests(request["Id"], 3)  # Done
                    if request["Type"] == 3:  # reboot
                        ci_print("Handling reboot request " + str(request), "INFO")
                        ret = updateCloudConnectorRequests(request["Id"], 3)  # Done
                        reboot()
                except Exception as innerinst:
                    print("error handling request ") + str(innerinst)
                    handleError("Error setting tags in inner handleNewRequests", innerinst)
    except Exception as inst:
        handleError("Error in handleNewRequests", inst)
        return False


# ============================
# PLC Functions
# ============================
def fill_Invalids(tagsDefenitions, values):

    global TagStatus

    retValues = []
    try:
        time = str(datetime.now(tzlocal.get_localzone()))
        valuesDict = {}
        ci_print("start fill_Invalids", "INFO")
        # prepare values dictionery
        for val in values:
            # print "val" + str(val)
            # print "val[u'TagId']=" + str(val[u'TagId'])
            valuesDict[val["TagId"]] = val
        # print "valuesDict="+str(valuesDict)
        for tagdef in tagsDefenitions:
            TagId = tagdef["TagId"]
            # print "tagdef" + str(tagdef)
            if TagId in valuesDict:
                retValues.append(valuesDict[TagId])
            else:
                tagAddress = tagdef["TagAddress"]
                val = {
                    "TagAddress": tagAddress,
                    "TagId": TagId,
                    "time": time,
                    "value": None,
                    "status": TagStatus.Invalid,
                }
                retValues.append(val)
        # print "=============="
        # print str(retValues)
    except Exception as inst:
        handleError("Error in fill_Invalids", inst)

    return retValues


# ippp
# ============================
def readEtherNetIP_Tags(tags_definitions):

    global TagStatus
    ci_print("start readEtherNetIP_Tags", "INFO")
    ans = []

    arranged_tags = arrange_tags_by_plc(tags_definitions)

    try:

        for plc_address, tags_def_list in arranged_tags.items():
            tags = [tag_def["TagAddress"] for tag_def in tags_def_list]
            ci_print("readEtherNetIP_Tags: Read tags " + str(tags), "DEBUG")

            with client.connector(host=plc_address, port=address[1], timeout=1.0) as connection:
                operations = client.parse_operations(tags)
                failures, transactions = connection.process(
                    operations=operations,
                    depth=1,
                    multiple=0,
                    fragment=False,
                    printing=False,
                    timeout=1.0,
                )

            #host = plc_address  # Controller IP address
            #port = address[1]  # default is port 44818
            #depth = 1  # Allow 1 transaction in-flight
            #multiple = 0  # Don't use Multiple Service Packet
            #fragment = False  # Don't force Read/Write Tag Fragmented
            #timeout = 1.0  # Any PLC I/O fails if it takes > 1s
            #printing = False  # Print a summary of I/O

            ci_print("transactions " + str(transactions), "INFO")
            ci_print("failures " + str(failures), "INFO")


            # client.close()
            # sys.exit( 1 if failures else 0 )

            for index, tag_def in enumerate(tags_def_list):
                tag_address = tag_def["TagAddress"]
                try:
                    if transactions[index]:
                        tag_id = int(tag_def["TagId"])
                        value = transactions[index][0]
                        time = str(datetime.now(tzlocal.get_localzone()))
                        ci_print("get register tagAddress=" + str(tag_address) + " value=" + str(value), "INFO")
                        val = {
                            "TagAddress": tag_address,
                            "TagId": tag_id,
                            "time": time,
                            "value": value,
                            "status": TagStatus.Valid,
                        }
                        ans.append(val)
                    else:
                        ci_print("Error reading Tag " + tag_address, "INFO")
                except ValueError:
                    handleError("Error reading tag value " + tag_address, ValueError)

        ci_print("End Read readEtherNetIP Tag", "INFO")
    except Exception as inst:
        handleError("Error in readEtherNetIP_Tags", inst)

    return fill_Invalids(tags_definitions, ans)


def arrange_tags_by_plc(tags_definitions):

    arranged_tags = {}

    for tag_def in tags_definitions:
        plc_address = tag_def.get("PlcIpAddress")
        if plc_address:
            if plc_address not in arranged_tags:
                arranged_tags[plc_address] = []
            arranged_tags[plc_address].append(tag_def)

    return arranged_tags

# ============================
def readModBusTags(tags_definitions):

    ans = []

    arranged_tags = arrange_tags_by_plc(tags_definitions)

    try:
        ci_print("Start Read ModBus Tag", "INFO")

        for plc_address in arranged_tags:
            maxOffset = 0
            for p in arranged_tags[plc_address]:
                offset = int(p.TagAddress)
                maxOffset = max(maxOffset, offset)

            from pymodbus.client import ModbusTcpClient as ModbusClient

            client = ModbusClient(plc_address, port=502)
            client.connect()

            rr = client.read_input_registers(0, maxOffset)  # 30000
            ci_print(str(rr.registers), "INFO")


            for index in range(len(plc_address)):
                try:
                    offset = int(plc_address[index]["TagAddress"]) - 1
                    TagId = int(plc_address[index]["TagId"])

                    value = rr.registers[offset]
                    time = str(datetime.now(tzlocal.get_localzone()))
                    ci_print("get register offset=" + str(offset) + " value=" + str(value), "INFO")
                    val = {
                        "TagAddress": offset,
                        "TagId": TagId,
                        "time": time,
                        "value": value,
                        "status": TagStatus.Valid,
                    }
                    ans.append(val)
                    # ans.update({offset:[offset,CounterId,datetime.now(),value]})
                except ValueError:
                    ci_print(
                        "Error reading tag value " + plc_address[index]["TagAddress"],
                        "DEBUG",
                    )

            client.close()

        ci_print("End Read ModBus Tag", "INFO")
        return ans
    except Exception as inst:
        handleError("error reading modbus", inst)
        return fill_Invalids(tags_definitions, ans)


# ============================
def readSimulation_Tags(tags_definitions):

    ans = []
    arranged_tags = arrange_tags_by_plc(tags_definitions)

    ci_print("Start Read readSimulation_Tags", "INFO")

    try:

        for plc_address, tags_def_list in arranged_tags.items():
            for index, tag_def in enumerate(tags_def_list):
                try:
                    TagId = int(tag_def.get("TagId"))
                    value = random.uniform(-10, 10)
                    time = str(datetime.now(tzlocal.get_localzone()))
                    val = {
                        "TagId": TagId,
                        "time": time,
                        "value": value,
                        "status": TagStatus.Valid,
                    }
                    ans.append(val)
                    ci_print(f"PLC Address: {plc_address}, TagId: {TagId}, value: {value} ScanRate: {tag_def.get('ScanRate')}")


                except (ValueError, TypeError) as e:
                    ci_print(f"Error processing tag definition: {e}")


        ci_print("End Read readSimulation_Tags", "INFO")
    except Exception as inst:
        handleError("Error in readSimulation_Tags", inst)

    return ans


# ============================
def printTagValues(tagValues):
    ci_print("Count " + str(len(tagValues)) + " Tags", "INFO")
    for index in range(len(tagValues)):
        ci_print(str(tagValues[index]), "INFO")


# ============================
def getLocalVersion():
    return VERSION


# ============================
def getServerSugestedVersion():
    return SUGGESTED_UPDATE_VERSION


# ============================
# Tag Files Functions
# ============================

def write_tags_definition_to_file(tags):
    try:
        with open(TAGS_DEFINITION_FILE_NAME, "w") as f:
            json.dump(tags, f)
    except Exception as e:
        handleError("Error in write_tags_definition_to_file", e)


# ============================

def get_tags_definition_from_file():
    try:
        with open(TAGS_DEFINITION_FILE_NAME, "r") as f:
            tags = json.load(f)
        return tags
    except Exception as e:
        handleError("Error in get_tags_definition_from_file", e)

# ============================


def get_tags_values_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            values = json.load(file)
        return values
    except Exception as e:
        handleError("Error in get_tags_values_from_file", e)


# ============================
def save_values_to_file(values, fileName):

    try:
        file_name = (
                "[NEW]TagsValuesFile"
                + datetime.now().strftime("%Y%m%d-%H%M%S%f")
                + ".txt"
        )
        with open(file_name, "w") as f:
            json.dump(values, f)

        time.sleep(1)

    except Exception as inst:
        handleError("Error in save_values_to_file", inst)

# ============================
def handle_values_file(file_name, token=""):

    try:
        values = get_tags_values_from_file(file_name)
        if values:
            isOk = set_cloud_tags(values, token)
            if isOk:
                os.remove(file_name)
                return True
            else:

                # Create error directory if it does not exist
                err_dir = os.path.join(os.path.dirname(file_name), "ERR")
                if not os.path.exists(err_dir):
                    os.makedirs(err_dir)

                # Construct the new error file path
                base_name = os.path.basename(file_name)
                err_file = os.path.join(err_dir, base_name.replace("[NEW]", "[ERR]"))

                # Rename (move) the file to the error directory
                os.rename(file_name, err_file)

    except Exception as e:
        handleError("Error in handle_values_file", e)
    return False

# ============================
def handle_all_values_files(token=""):

    try:
        dir_path = os.getcwd()
        files_starting_with_tags_values_file = [
            file for file in os.listdir(dir_path) if file.startswith("[NEW]TagsValuesFile")
        ]
        files_starting_with_tags_values_file.sort(key=lambda s: os.path.getmtime(os.path.join(dir_path, s)))

        for file in files_starting_with_tags_values_file:
            if file.endswith(".txt") and file.startswith("[NEW]"):
                handle_values_file(os.path.join(dir_path, file), token)

    except Exception as e:
        handleError("Error in handle_all_values_files", e)


def arrange_by_connector_type(tags_def):
    arranged_tags = {}

    for tag in tags_def:
        connector_type = tag.get('connectorTypeName', '')  # Provide a default value if key doesn't exist
        if connector_type not in arranged_tags:
            arranged_tags[connector_type] = []
        arranged_tags[connector_type].append(tag)

    return arranged_tags

# ============================
# Main Loop
# ============================
def Main():

    global SCAN_RATE_LAST_READ
    global CURRENT_TOKEN
    try:

        if CURRENT_TOKEN == "":
            CURRENT_TOKEN = get_cloud_token()
        # currently must get tags from cloud to init server before setting values
        tagsDefScanRatesAns = get_cloud_tags(CURRENT_TOKEN)
        tagsDefScanRates = tagsDefScanRatesAns["Tags"]

        for scanRate in tagsDefScanRates:

            if scanRate in (None, 'null'):
                continue

            scanRateInt = int(scanRate)
            scanRateStr = str(scanRate)
            diff = 0
            if scanRateStr in SCAN_RATE_LAST_READ:
                now = datetime.now()
                diff = (now - SCAN_RATE_LAST_READ[scanRateStr]).total_seconds()
                # print ('diff = -------' + str(diff))


            if diff + 3 > scanRateInt or diff == 0:


                tagsDef = tagsDefScanRates[scanRate]
                arranged_tags = arrange_by_connector_type(tagsDef)

                for connector_type in arranged_tags:
                    print(connector_type)
                    values = None
                    if connector_type == "Simulation":
                        values = readSimulation_Tags(arranged_tags[connector_type])
                    if connector_type == "Modbus":
                        values = readModBusTags(arranged_tags[connector_type])
                    if connector_type == "Ethernet/IP":
                        values = readEtherNetIP_Tags(arranged_tags[connector_type])
                        if values == []:
                            ci_print("Ethernet Empty values ::1", "ERROR")
                            values = readEtherNetIP_Tags(arranged_tags[connector_type])
                            if values == []:
                                time.sleep(0.1)
                                ci_print("Ethernet Empty values ::1", "ERROR")
                                values = readEtherNetIP_Tags(arranged_tags[connector_type])
                                if values == []:
                                    time.sleep(1)
                                    ci_print("Ethernet Empty values ::2", "ERROR")
                                    values = readEtherNetIP_Tags(arranged_tags[connector_type])

                    if values:
                        save_values_to_file(values, "")
                        now = datetime.now()
                        SCAN_RATE_LAST_READ[scanRateStr] = now


        if CURRENT_TOKEN != "":
            handle_all_values_files(CURRENT_TOKEN)
        else:
            ci_print("No Token, skipping upload step", "WARNING")
    except Exception as inst:
        handleError("Error in Main", inst)
        CURRENT_TOKEN = ""



