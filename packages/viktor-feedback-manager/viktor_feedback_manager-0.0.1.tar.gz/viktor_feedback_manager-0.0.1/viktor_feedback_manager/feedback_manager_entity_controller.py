"""Module that provides the feedback manager parent entity parametrization and controller"""

import pandas as pd
from viktor import ViktorController
from viktor import progress_message
from viktor.api_v1 import API
from viktor.parametrization import ChildEntityManager
from viktor.parametrization import NumberField
from viktor.parametrization import SetParamsButton
from viktor.parametrization import Table
from viktor.parametrization import TextField
from viktor.parametrization import ViktorParametrization
from viktor.result import SetParamsResult
from viktor_table_view import TableResult
from viktor_table_view import TableView

from viktor_feedback_manager.feedback_entity_controller import Feedback
from viktor_feedback_manager.feedback_entity_controller import get_response


class Parametrization(ViktorParametrization):
    """Parametrization of feedback manager entity"""

    company_name = TextField("Company name", description="Add the same name as in the URL (before .viktor.ai)")
    stop_iterating_after_n_tries = NumberField(
        "Maximum number of tries",
        default=50,
        description="The current implementation tries to get the next support ticket. "
        "If it does not exist, it will try the next. "
        "If you think you are missing tickets, increase this value",
    )
    workspace_table = Table(
        "Workspaces to get tickets from", description='Can be found in the URL behind ".../workspaces/"'
    )
    workspace_table.workspace_name = TextField("Name of workspace")
    workspace_table.workspace_id = NumberField("Workspace ID")

    retrieve_support_tickets = SetParamsButton("Retrieve feedback tickets", method="retrieve_feedback_items", flex=100)
    child_entity_manager = ChildEntityManager(entity_type_name="Feedback")


class FeedbackManager(ViktorController):
    """Controller for FeedbackManager"""

    parametrization = Parametrization
    label = "Feedback manager"
    children = ["Feedback"]
    show_children_as = "Table"

    @TableView("Overview", duration_guess=1)
    def visualize_table_from_url(self, params, entity_id, **kwargs):
        """Get an overview of the feedback support tickets"""
        feedback_lst = []

        for child in API().get_entity(entity_id).children():
            ticket_id, created_on, reported_by = Feedback.get_data_table(self, child.last_saved_params)

            if ticket_id and created_on and reported_by:
                feedback_lst.append({"Ticket ID": ticket_id, "Created on": created_on, "Reported by": reported_by})

        df = pd.DataFrame(feedback_lst)

        return TableResult(df)

    @staticmethod
    def retrieve_feedback_items(params, entity_id: int, **kwargs) -> SetParamsResult:
        """Retrieves feedback items (support tickets) from some workspace, and saves them as child entities"""
        api = API()
        children = api.get_entity_children(entity_id)
        ticket_id_lst = []

        for child in children:
            ticket_id_lst.append(child.last_saved_params.ticket_id)

        times_not_found = 0  # Initialize counter to keep track of how many times the ticket is not found
        support_ticket_id = max(ticket_id_lst, default=0)  # Don't find the ones we have found previously again
        while True:  # Setting out on a journey to find all support tickets...
            support_ticket_id += 1
            progress_message(f"Getting support ticket id {support_ticket_id}")
            for workspace_id in [row.workspace_id for row in params.workspace_table]:
                _, status = get_response(support_ticket_id, params.company_name, workspace_id)
                if status == 200:
                    times_not_found = 0  # We found one again! Reset this counter
                    if support_ticket_id not in ticket_id_lst:
                        feedback_params = {
                            "ticket_id": support_ticket_id,
                            "company_name": params.company_name,
                            "workspace_id": workspace_id,
                        }
                        _ = api.create_child_entity(
                            entity_id,
                            entity_type_name="Feedback",
                            name=f"Ticket {support_ticket_id}",
                            params=feedback_params,
                        )
                    continue  # We're done with this support_ticket_id
            # No ticket found! Keep track of how many times we have not found something
            times_not_found += 1
            if times_not_found >= params.stop_iterating_after_n_tries:
                break
        return SetParamsResult({})
