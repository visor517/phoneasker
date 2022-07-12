import requests


def post_contact(contact):
    requests.post(
        url="https://s1-nova.ru/app/private_test_python/",
        headers={"Content-type": "application/json"},
        data=contact,
    )
