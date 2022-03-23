import smtplib


server = smtplib.SMTP(host="localhost", port=7777)

message = """
A

message

on multiple lines!
"""

server.sendmail(
    from_addr="roberto@localhost.com",
    to_addrs=["roberto.judet@itschool.ro", "roberto.judet@protonmail.com"],
    msg=message,
)

