"""Module that provides the feedback entities parametrization and controller"""

import os

import requests
from viktor import ViktorController
from viktor.parametrization import DynamicArray
from viktor.parametrization import HiddenField
from viktor.parametrization import TextField
from viktor.parametrization import ViktorParametrization
from viktor.views import Summary
from viktor.views import SummaryItem
from viktor.views import WebResult
from viktor.views import WebView


class Parametrization(ViktorParametrization):
    """Parametrization of feedback entity"""

    ticket_id = HiddenField("Ticket ID")
    company_name = HiddenField("Company name")
    workspace_id = HiddenField("Workspace ID")

    ticket_status = TextField("Ticket status")

    comments_array = DynamicArray("Comments")
    comments_array.comment = TextField("")


def get_response(ticket_id: int, company_name: str, workspace_id: int):
    """Query company environment company_name with workspace_id for some support ticket_id"""
    token = os.environ["API_KEY"]
    url = f"https://{company_name}.viktor.ai/api/workspaces/{workspace_id}/support_tickets/{ticket_id}/"
    response = requests.get(url=url, headers={"Authorization": f"Bearer {token}"}, timeout=10)
    return response.json(), response.status_code


class Feedback(ViktorController):
    """Controller for Feedback"""

    label = "Feedback"
    parametrization = Parametrization

    summary = Summary(item_1=SummaryItem("Ticket status", str, "parametrization", "ticket_status"))

    def get_data_table(self, params):
        """Get data about the feedback entity"""
        response, _ = get_response(params.ticket_id, params.company_name, params.workspace_id)

        ticket_id = response["id"]
        created_at = response["created_at"].split("T")[0]
        created_by = response["created_by"]["name"]

        return ticket_id, created_at, created_by

    @WebView("Support ticket", duration_guess=1)
    def get_web_view(self, params, **kwargs):
        """Parse support ticket data in HTML"""
        response, _ = get_response(params.ticket_id, params.company_name, params.workspace_id)

        html_text = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Feedback Details</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 20px;
                }}
                .container {{
                    border: 1px solid #ccc;
                    padding: 20px;
                    border-radius: 10px;
                    max-width: 600px;
                    margin: auto;
                    background-color: #f9f9f9;
                }}
                .header {{
                    text-align: center;
                    margin-bottom: 20px;
                }}
                .content {{
                    line-height: 1.6;
                }}
                .content div {{
                    margin-bottom: 10px;
                }}
                .label {{
                    font-weight: bold;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>Feedback Details</h1>
                </div>
                <div class="content">
                    <div><span class="label">ID:</span> {response['id']}</div>
                    <div><span class="label">Topic:</span> {response['topic']}</div>
                    <div><span class="label">Subject:</span> {response['subject']}</div>
                    <div><span class="label">Content:</span> {response['content']}</div>
                    <div><span class="label">Created At:</span> {response['created_at']}</div>
                    <div><span class="label">Created By:</span></div>
                    <div style="margin-left: 20px;">
                        <div><span class="label">ID:</span> {response['created_by']['id']}</div>
                        <div><span class="label">Name:</span> {response['created_by']['name']}</div>
                        <div><span class="label">First Name:</span> {response['created_by']['first_name']}</div>
                        <div><span class="label">Last Name:</span> {response['created_by']['last_name']}</div>
                        <div><span class="label">Email:</span> {response['created_by']['email']}</div>
                    </div>
                </div>
            </div>
        </body>
        </html>
        """
        return WebResult(html=html_text)
