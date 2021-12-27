import re

def validate_phone(phone_num):
    pattern = r"[(]\d{3}[)][\s.-]?\d{3}[\s.-]?\d{4}|\d{3}[\s.-]?\d{3}[\s.-]?\d{4}|\d{3}[\s.-]?\d{4}"
    match_obj = re.match(pattern, phone_num)
    return match_obj.group() if match_obj else None

goodies = ["(111)-222-5555",
           "222-5555",
           "222-333-4444",
           "111.222.1122",
           ]

questionables = ["1111-22-3333"]

baddies = ["11-222-3333"]

for phone_nums in goodies:
    assert validate_phone(phone_nums)

for phone_nums in questionables:
    assert not validate_phone(phone_nums)

for phone_nums in baddies:
    assert not validate_phone(phone_nums)


def validate_email(email):
    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

    match_obj = re.match(pattern, email)
    return match_obj.group() if match_obj else None

email_goodies = ["ana@foo.bar",
                 "bill_x@foo.bar",
                 "chris.schmidt@bar.baz"]

email_questionables = ["ana.bill.chris_x@foo.b"]

email_badies = ["11@foo.@baz",
                 "bill_x.bar@",
                 "ana.$foo.bar"]

for emails in email_goodies:
    assert validate_email(emails)

for emails in email_questionables:
    assert not validate_email(emails)

for emails in email_badies:
    assert not validate_email(emails)

print("test passed")