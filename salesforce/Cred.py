"""
Following Credentials are for test purposes only.
This repository is  made for https://convin.ai/ to
evaluate my django skills by completing task to
integrate Salesforce to Django without using 3rdParty Library


I Atriya Patel Owner doesn't Hold Any responsibility of any kind
of misuse done by any user using this particular credentials.

"""

Credentials = {
    "grant_type": "password",
    "client_id": "3MVG9fe4g9fhX0E7Q0ql652cbde7SqV0YTz9d3LIiyEueLAxwtEoSHpI3P_TzP6FsTY54.YkpF3__rsEIan5J",
    "client_secret": "FC5209D8E2D7F2FC56D4DF9C383419C8B076E79D6AFF122D5596A7241F93EA7E",
    "username": "demo369@test.com",
    "password": "RootAdmin@369+noIjcIgsqDbfbfa1hwAhsZH66"
}

OAuthUrl = "https://login.salesforce.com/services/oauth2/token"

Query = "SELECT+Name,Type,Phone+FROM+Account"


def Header(Access_token):
    Headers = {
        "Content_type": "application/json",
        "Accept_Encoding": "gzip",
        'Authorization': f"Bearer {Access_token}"
    }
    return Headers


def API_Url(Query):
    url = f"https://d5g00000cqm99ead-dev-ed.my.salesforce.com/services/data/v42.0/query/?q={Query}"
    return url
