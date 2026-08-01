import requests

LOGIN_URL = "https://agclms.in/Elogin/StudentLogin"


def login(student_id, password):
    session = requests.Session()

    # Open login page
    session.get(LOGIN_URL)

    payload = {
        "StudentId": student_id,
        "Password": password
    }

    response = session.post(
        LOGIN_URL,
        data=payload,
        headers={
            "User-Agent": "Mozilla/5.0"
        }
    )

    # Verify login
    if "Logout" not in response.text:
        raise Exception("Login Failed")

    return session