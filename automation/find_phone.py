import re

with open('./automation/potential-contacts.txt') as f:
    text_from_file = f.read()

    pattern = r"[(]\d{3}[)][\s.-]?\d{3}[\s.-]?\d{4}|\d{3}[\s.-]?\d{3}[\s.-]?\d{4}|\d{3}[\s.-]?\d{4}"

    phone_nums = re.findall(pattern, text_from_file)

    print(len(phone_nums))

    print(phone_nums)

    text_with_phone = " ".join(phone_nums)

    with open("automation/text_with_phone_nums.txt", "w") as f:
        f.write(text_with_phone)

