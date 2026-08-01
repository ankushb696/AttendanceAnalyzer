from bs4 import BeautifulSoup

BASE_URL = "https://agclms.in"


def get_subjects_and_links(html):

    soup = BeautifulSoup(html, "html.parser")

    rows = soup.find_all("tr")

    subjects = []

    for row in rows:

        cols = row.find_all("td")

        if len(cols) >= 3:

            subject = cols[0].get_text(strip=True)

            attendance = row.find("a", string="Attendance")

            if attendance:

                href = attendance.get("href")

                subjects.append({
                    "subject": subject,
                    "url": BASE_URL + href
                })

    return subjects


def get_student_info(html):

    soup = BeautifulSoup(html, "html.parser")

    # Student Name
    name = soup.find("span", class_="fs-4").get_text(strip=True)

    # Student Photo
    img = soup.find("img", alt="Student Image")

    photo = BASE_URL + "/" + img["src"].replace("../", "")

    # Section
    section = soup.find("h6").get_text(strip=True)
    section = section.replace("SectionName :", "")

    return {
        "name": name,
        "photo": photo,
        "section": section
    }