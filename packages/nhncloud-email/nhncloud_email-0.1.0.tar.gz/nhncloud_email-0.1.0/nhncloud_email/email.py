import requests
import base64

class NHNCloudEmail:
    def __init__(self, app_key, secret_key, sender_email):
        self.api_url = f"https://api-mail.cloud.toast.com/email/v2.1/appKeys/{app_key}"
        self.app_key = app_key
        self.secret_key = secret_key
        self.sender_email = sender_email

    def send_email(self, recipient_email, subject, body, attachments=None):
        headers = self._get_headers()
        payload = {
            "senderAddress": self.sender_email,
            "title": subject,
            "body": body,
            "receiverList": [{"receiveMailAddr": recipient_email, "receiveType": "MRT0"}],
        }
        if attachments:
            payload["attachments"] = self._prepare_attachments(attachments)

        print(headers, payload, self.api_url)
        response = requests.post(f"{self.api_url}/sender/mail", json=payload, headers=headers)
        return self._handle_response(response)

    def send_bulk_email(self, recipient_emails, subject, body, attachments=None):
        headers = self._get_headers()
        receivers = [{"receiveMailAddr": email, "receiveType": "MRT0"} for email in recipient_emails]
        payload = {
            "senderAddress": self.sender_email,
            "title": subject,
            "body": body,
            "receiverList": receivers,
        }
        if attachments:
            payload["attachments"] = self._prepare_attachments(attachments)
        response = requests.post(f"{self.api_url}/sender/mail", json=payload, headers=headers)
        return self._handle_response(response)

    def schedule_email(self, recipient_email, subject, body, schedule_time, attachments=None):
        headers = self._get_headers()
        payload = {
            "senderAddress": self.sender_email,
            "title": subject,
            "body": body,
            "receiverList": [{"receiveMailAddr": recipient_email, "receiveType": "MRT0"}],
            "sendTime": schedule_time,
        }
        if attachments:
            payload["attachments"] = self._prepare_attachments(attachments)
        response = requests.post(f"{self.api_url}/sender/eachMail", json=payload, headers=headers)
        return self._handle_response(response)

    def get_email_status(self, request_id):
        headers = self._get_headers()
        response = requests.get(f"{self.api_url}/sender/mail/{request_id}", headers=headers)
        return self._handle_response(response)

    def get_sent_email_list(self, start_date, end_date):
        headers = self._get_headers()
        params = {
            "startSendDate": start_date,
            "endSendDate": end_date
        }
        response = requests.get(f"{self.api_url}/sender/mails", headers=headers, params=params)
        return self._handle_response(response)

    def _get_headers(self):
        return {
            "Content-Type": "application/json;charset=UTF-8",
            "X-Secret-Key": self.secret_key,
        }

    def _handle_response(self, response):
        if response.status_code == 200:
            return response.json()
        else:
            return {
                "status_code": response.status_code,
                "error": response.text
            }

    def _prepare_attachments(self, attachments):
        prepared_attachments = []
        for attachment in attachments:
            with open(attachment, "rb") as file:
                encoded_file = base64.b64encode(file.read()).decode('utf-8')
                prepared_attachments.append({
                    "fileName": attachment.split("/")[-1],
                    "fileBody": encoded_file,
                })
        return prepared_attachments
