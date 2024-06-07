import requests


class NHNCloudSMS:
    def __init__(self, app_key, secret_key, sender_phone_number):
        self.api_url = f"https://api-sms.cloud.toast.com/sms/v3.0/appKeys/{app_key}"
        self.app_key = app_key
        self.secret_key = secret_key
        self.sender_phone_number = sender_phone_number

    def send_sms(self, recipient_number, message):
        headers = self._get_headers()
        payload = {
            "body": message,
            "sendNo": self.sender_phone_number,
            "recipientList": [{"recipientNo": recipient_number}],
        }
        response = requests.post(f"{self.api_url}/sender/sms", json=payload, headers=headers)
        return response.json()

    def send_bulk_sms(self, recipient_numbers, message):
        headers = self._get_headers()
        recipient_list = [{"recipientNo": number} for number in recipient_numbers]
        payload = {
            "body": message,
            "sendNo": self.sender_phone_number,
            "recipientList": recipient_list,
        }
        response = requests.post(f"{self.api_url}/sender/sms", json=payload, headers=headers)
        return response.json()

    def schedule_sms(self, recipient_number, message, schedule_time):
        headers = self._get_headers()
        payload = {
            "body": message,
            "sendNo": self.sender_phone_number,
            "recipientList": [{"recipientNo": recipient_number}],
            "scheduleCode": schedule_time
        }
        response = requests.post(f"{self.api_url}/sender/sms", json=payload, headers=headers)
        return response.json()

    def get_sms_status(self, request_id):
        headers = self._get_headers()
        response = requests.get(f"{self.api_url}/sender/sms/{request_id}", headers=headers)
        return response.json()

    def get_sent_sms_list(self, start_date, end_date):
        headers = self._get_headers()
        params = {
            "startCreateDate": start_date,
            "endCreateDate": end_date
        }
        response = requests.get(f"{self.api_url}/sender/sms", headers=headers, params=params)
        return response.json()

    def _get_headers(self):
        return {
            "Content-Type": "application/json;charset=UTF-8",
            "X-Secret-Key": self.secret_key,
        }
