from scraper.login import login
from scraper.dashboard import get_dashboard
from scraper.parser import get_subjects_and_links, get_student_info
from scraper.attendance import calculate_attendance


def get_attendance(student_id, password):

    session = login(student_id, password)

    dashboard = get_dashboard(session)

    student = get_student_info(dashboard)

    subjects = get_subjects_and_links(dashboard)

    results = []

    total_present = 0
    total_classes = 0

    for subject in subjects:

        data = calculate_attendance(session, subject)

        total_present += data["present"]
        total_classes += data["total"]

        if data["percentage"] >= 75:
            data["status"] = "safe"

        elif data["percentage"] >= 60:
            data["status"] = "warning"

        else:
            data["status"] = "danger"

        results.append(data)

    overall = 0

    if total_classes > 0:
        overall = round((total_present / total_classes) * 100, 2)

    return {
        "student": student,
        "overall": overall,
        "subjects": results
    }