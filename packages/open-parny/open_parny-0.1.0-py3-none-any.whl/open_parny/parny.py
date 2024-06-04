# open_parny/parny.py

import requests

class Parny:
    def __init__(self, url, headers=None):
        self.url = url
        self.headers = headers if headers else {'Content-Type': 'application/json'}

    def send_alert(self, alert_name, alert_service, alert_date, alert_description, alert_severity, alert_instance):
        data = {
            "alert_name": alert_name,
            "alert_service": alert_service,
            "alert_date": alert_date,
            "alert_description": alert_description,
            "alert_severity": alert_severity,
            "alert_instance": alert_instance
        }
        
        response = requests.post(self.url, json=data, headers=self.headers)
        
        if response.status_code == 200:
            return {"status": "success", "message": "Alert sent successfully."}
        else:
            return {"status": "error", "message": f"Failed to send alert. Status code: {response.status_code}"}

# Example usage
if __name__ == "__main__":
    alert_url = 'https://webhook.parny.io/alert/<token>'
    parny = Parny(alert_url)

    response = parny.send_alert(
        alert_name="Webhook Test Alert",
        alert_service="Webhook",
        alert_date="2023-11-10 09:05:00.0000",
        alert_description="This is an example alert for Webhook integration. You can fill here with whatever you want!",
        alert_severity="medium",
        alert_instance="https://parny.io"
    )

    print(response)
