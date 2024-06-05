import requests

class Telephony:

    def __init__(self, key: str):
        self.__baseUrl: str = "https://api.pressone.co/"
        if not key:
            raise Exception("Secret key needed for this object")
        self.__accessToken: str = key

    def getNumbers(self, page:int = 1, count: int = 100): 
        data = self.get("api/third-party/sdk/number/")
        
        response = []

        for number in data:
            phone_number = number.get("phone_number")
            status = number.get("verification_status")
            label = number.get("label")
            number_id = number.get("id")
            response.append({
                "phone_number": phone_number,
                "status": status,
                "label": label,
                "number_id": number_id,
            })

        return response

    def getMembers(self, page: int = 1, count: int = 100):
        data = self.get("api/third-party/sdk/team-member/")
        
        responseData = data.get("data", [])
        total = data.get("total", 0)
        page_size = data.get("page_size", 0)
        
        response = {
            "data": [],
            "total": total,
            "size": page_size
        }

        for businessData in responseData:
            receivers = businessData.get("receivers", [])
            for receiver in receivers:
                response.data.append({
                    "phone_number" : businessData.get("mobile", ""),
                    "full_name"    : f'{businessData.get("first_name", "")} {businessData.get("last_name", "")}',
                    "receiver_id"  : receiver.get("business_number", 0),
                    "receiver_code": receiver.get("extension_code"),
                })

        return response

    def assignNumber(self, param):

        if ("email" not in param or "phone_number" not in param):
            return {
                "message": "both email and phone_number are required.",
                "code"   : "404"
            }

        if ("number_ids" not in param):
            return {
                "message": "number_ids must be an array of int.",
                "code"   : "401"
            }

        payload = {
            "first_name" : param["first_name"] if "first_name" in param else param["phone_number"],
            "last_name"  : param["last_name"] if "last_name" in param else param["phone_number"],
            "email"      : param["email"],
            "mobile"     : param["phone_number"],
            "role"       : param["role"] if "role" in param else "owner",
            "note"       : None,
            "country"    : param["country"] if "country" in param else "NG",
            "can_make_calls": True,
            "permissions": {
                "can_export_call_logs"  : None,
                "can_view_all_call_logs": None,
                "can_export_contact" : None,
                "can_export_report"  : None,
                "can_manage_billing" : None,
                "can_manage_team"    : None,
                "can_manage_permissions": None,
                "can_manage_personalization": None,
                "can_access_call_recordings": None,
                "can_download_call_recordings"  : None,
                "can_view_performance_report": None,
                "can_view_activity_report": None,
                "business_numbers": param["number_ids"],
                "role"           : param["role"] if "role" in param else "owner",
            }
        }

        data = await self.post("api/third-party/sdk/team-member/", payload)

        receivers = data.get("receivers", [])
        first_name = data.get("first_name", "")
        last_name = data.get("last_name", "")

        response = []
        for receiver in receivers:
            response.append({
                "phone_number": data.get("mobile", None),
                "full_name": f"{first_name} {last_name}",
                "receiver_id": receiver.get("business_number", receiver.get("id", "")),
                "receiver_code": receiver.get("extension_code", ""),
            })

        return response

    def getCallCredentials(self, receiver_id: str, public_key: str):
        return self.post("api/third-party/sdk/receiver-line/", {
            "public_key": public_key,
            "receiver" : receiver_id
        })

    def getCallRecords(self, page: int = 1, count: int = 100):
        return self.get("api/third-party/sdk/contacts/?page_index=$page&page_size=$count")

    def get_contacts(self, page: int = 1, count: int = 100):
        return self.get("api/third-party/sdk/contacts/?page_index=$page&page_size=$count")
    
    def get(self, url: str):
        return self.make_request("GET", url)

    def post(self, url: str, data):
        return self.make_request("POST", url, data)

    def make_request(self, method: str, url: str, body):
        headers = {
            'Authorization': f"Bearer {self.__accessToken}",
            'Pressone-X-Api-Key': self.__accessToken,
        }

        full_url: str = f"{self.__baseUrl}{url}"

        try:
            if method == "POST":
                response = requests.post(full_url, json = body, headers = headers)
            if method == "GET":
                response = requests.get(full_url, headers = headers)
            
            statusCode: int = response.status_code

            if ( statusCode == 401 ):
                return response.json()

            if (statusCode > 300):
                raise Exception("Error Processing Request")

            return response.json()
        except:
            return {
                "message": "An error occured",
                "code"   : "404"
            }