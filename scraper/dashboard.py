import requests

DASHBOARD_URL = "https://agclms.in/DashBoardStudent"


def get_dashboard(session):
    response = session.get(DASHBOARD_URL)

    if response.status_code != 200:
        raise Exception("Dashboard could not be loaded.")

    return response.text