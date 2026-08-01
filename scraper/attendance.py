from bs4 import BeautifulSoup


def calculate_attendance(session, subject):

    response = session.get(subject["url"])

    soup = BeautifulSoup(response.text, "html.parser")

    present = 0
    absent = 0

    rows = soup.find_all("tr")

    for row in rows:

        cols = row.find_all("td")

        if len(cols) == 2:

            status = cols[1].get_text(strip=True)

            if status == "PRESENT":
                present += 1

            elif status == "ABSENT":
                absent += 1

    total = present + absent

    percentage = 0

    if total > 0:
        percentage = round((present / total) * 100, 2)

    return {
        "subject": subject["subject"],
        "present": present,
        "absent": absent,
        "total": total,
        "percentage": percentage
    }