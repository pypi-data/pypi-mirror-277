import requests
from time import sleep
from datetime import datetime
import logging



def api_call(url, method='get', params=None, headers=None, timeout=30, files=None):
    logging.basicConfig(
        level=logging.DEBUG,  # Set the logging level
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Format of the log messages
        handlers=[
            logging.FileHandler('app.log'),  # Log to a file
            logging.StreamHandler()  # Log to console
        ]
    )
    logger = logging.getLogger(__name__)   
    try:
        method_types = ['get', 'post']
        if method not in method_types:
            raise ValueError("Invalid method type. Expected one of: %s" % method_types)
        if method == 'post':
            response = requests.post(url, data=params, headers=headers, timeout=timeout, files=files)
            response.raise_for_status()  # Raises HTTPError, if one occurred
        elif method == 'get':
            response = requests.get(url, params=params, headers=headers, timeout=timeout)
            response.raise_for_status()  # Raises HTTPError if the HTTP request returned an unsuccessful status code

        return response

    except requests.exceptions.HTTPError as http_err:
        # Handle specific HTTP errors (e.g., response status code 4xx or 5xx)
        logger.error(f"HTTP error occurred: {http_err}")
        logger.info(f"HTTP response content: {response.content}")
    except requests.exceptions.ConnectionError as conn_err:
        # Handle errors due to connection problems
        logger.error(f"Error connecting: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        # Handle errors for request timeouts
        logger.error(f"Timeout error: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        # Handle all requests' exceptions not caught by preceding blocks
        logger.error(f"An error occurred during the API request: {req_err}")
    return None

class Quokka:

    def __init__(self, key):
        self.api_key = key
        logging.basicConfig(
            level=logging.DEBUG,  # Set the logging level
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Format of the log messages
            handlers=[
                logging.FileHandler('app.log'),  # Log to a file
                logging.StreamHandler()  # Log to console
            ]
        )
        self.logger = logging.getLogger(__name__)

    def push_scan(self, the_file, subgroup_ids):
        # Upload APK or IPA to perform a scan
        # the_file - the APK/IPA to upload
        # subgroup_ids - comma separated list of subgroup Ids
        self.the_file = the_file
        self.subgroup_ids = subgroup_ids
        app_file = {'app': open(the_file, 'rb')}
        thePlatform = "android"
        if the_file[-3:].lower() == "ipa":
            thePlatform = "ios"

        self.platform = thePlatform
        
        if ( subgroup_ids == 0 ):
            params = {'key': self.api_key, 'platform': thePlatform}
        else:
            params = {'key': self.api_key, 'platform': thePlatform, 'subgroupIds': ','.join(subgroup_ids) }

        url = 'https://emm.kryptowire.com/api/submit'
        response = api_call(url, method='post', params=params, files=app_file)
        response_data = response.json()

        # Handle the response
        if response_data is not None:
            return response_data, thePlatform
        else:
            self.logger.error("No valid response received from the API")

    def get_sub_groups(self, the_group=None):
        # getSubGroups - make the API call to retrieve list of sub groups.
        #    key: your unique API key
        #      NOTE: the key must belong to a group admin. Regular users can't make this call
        #    theGroup - a string which will be matched against the list of sub groups
        #    note: if theGroup is "" this will simply print a list of subgroups
        try:
            method = "get"
            url = "https://api.kryptowire.com/group-admin/sub-groups"
            headers = {
            'Accept': 'application/json',
            }
            params={'key': self.api_key}
            response = api_call(url, method='get', params=params, headers=headers)
            response_data = response.json()
            # Handle the response
            if response_data is not None:
                if ( the_group is None):
                    for r in response_data:
                        self.logger.info('{} : {}'.format(r['id'], r['name']))
                else:
                    for r in response_data:
                        if ( r['name'].lower() == the_group.lower() ):
                            return r['id']
            else:
                self.logger.error("No valid response received from the API")
            
            return None
        
        except Exception as err:
            self.logger.error(err)

    def wait_for_scan_complete(self, uuid):
        status = 'processing'
        while status == 'processing':
            url = 'https://api.kryptowire.com/api/status'
            params = {'key': self.api_key, 'uuid': uuid}

            response = api_call(url, method='get', params=params)
            response_data = response.json()
            # Handle the response
            if response_data is not None:
                self.logger.info(response_data)
            else:
                self.logger.error("No valid response received from the API")
            status = response_data['status']
            sleep(15)
        return response_data
    
    def download_pdf(self, uuid, the_platform):
        # Check that the Quokka Analysis has completed before proceeding
        status = 'processing'
        while status == 'processing':
            url = 'https://emm.kryptowire.com/api/status'
            params = {'key': self.api_key, 'uuid': uuid}

            response = api_call(url, method='get', params=params)
            response_data = response.json()
            # Handle the response
            if response_data is not None:
                self.logger.info(response_data)
            else:
                self.logger.error("No valid response received from the API")
            status = response_data['status']
            sleep(15)

        # Print URL of Analysis results for adding comments
        
        self.logger.info(f"https://mast.kryptowire.com/#/{the_platform}-report/{uuid}")

        # Pause script and wait for adding of comments to URL
        input('Press enter key to proceed to download the PDF.\n')

        params['regeneratePDF'] = True
        url = 'https://emm.kryptowire.com/api/results/pdf'
        response = api_call(url, method='get', params=params)

        # Write content in pdf file
        pdf = open("pdf"+str(uuid)+".pdf", 'wb')
        pdf.write(response.content)
        pdf.close()
        self.logger.info(f"File pdf{uuid}.pdf downloaded")

    def get_app_issue(self, uuid):
        ###################################################################################
        # getAppIssue - make the API call to retrieve app issues in JSON format
        #    uuid: the unique ID of the app test run that issues are being retrieved for
        ############
        url = "https://api.kryptowire.com/app-issues/parsed/"
        params={'key': self.api_key, 'uuid': uuid}
        response = api_call(url, method='get', params=params)
        return response.text
    
    def get_results(self, start_date):
        # getResults - make the API call to retrieve specified results in JSON format
        #   start_date, date to retrieve the results as python datetime
        #   Note limitation on analytics API, can only do days from today, no end date
        days = (datetime.today() - start_date).days
        url = "https://api.kryptowire.com/api/analytics/"
        params={'key': self.api_key, 'range': days, 'type': 'days'}
        response = api_call(url, method='get', params=params)
        return response.text
    
    def get_apps(self, start_date, end_date):
        # getApps - make the API call to retrieve specified results in JSON format
        #   start_date, end_date - date to retrieve the results as python datetime
        url = "https://api.kryptowire.com/api/submitted-apps/"
        params={'key': self.api_key, 'startDate': start_date.strftime("%Y-%m-%d"), 'endDate': end_date.strftime("%Y-%m-%d")}
        response = api_call(url, method='get', params=params)
        return response.text

