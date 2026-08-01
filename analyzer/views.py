from django.shortcuts import render
from scraper.scraper import get_attendance

def home(request):

    if request.method == "POST":

        student_id = request.POST["studentid"]
        password = request.POST["password"]

        try:
            report = get_attendance(student_id, password)

            return render(
                request,
                "result.html",
                {
                    "report": report
                }
            )

        except Exception:
            return render(
                request,
                "index.html",
                {
                    "error": "Invalid Student ID or Password."
                }
            )

    return render(request, "index.html")