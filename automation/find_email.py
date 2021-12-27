import re

with open('./automation/potential-contacts.txt') as f:
    text_from_file = f.read()

    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

    emails = re.findall(pattern, text_from_file)

    print(len(emails))

    print(emails)

    text_with_email = " ".join(emails)

    with open("automation/text_with_email.txt", "w") as f:
        f.write(text_with_email)
