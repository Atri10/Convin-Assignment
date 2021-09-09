from django.http import HttpResponse, JsonResponse
import requests
from salesforce.Cred import Credentials, OAuthUrl, Query, Header, API_Url
from salesforce.models import SalesForceUsers


def FetchData():
    # Todo: Get Response form salfeforce DONE
    Response = requests.post(OAuthUrl, params=Credentials)

    # Todo: Get OAuth Token and Instance URL DONE
    AccessToken = Response.json().get("access_token")
    InstanceUrl = Response.json().get("instance_url")

    # Todo: Get User Data and return to parent function
    Response = requests.get(API_Url(Query), headers=Header(AccessToken))
    return Response.json()


def PutData(request):
    # Todo: Get data from server
    UserData = FetchData()

    # Todo: Push Data into Database
    for User in UserData["records"]:
        SalesForceUsers.objects.get_or_create(AccountName=User["Name"], Type=User["Type"], Phone=User["Phone"])


    # Todo: Return Success Response
    return HttpResponse("Database was Updated with Users from Sales force", status=200)


def PullData(request):
    if request.method == "GET":
        # Todo: Get data from Database
        Users = list(SalesForceUsers.objects.values())
        return JsonResponse(Users, safe=False)

    else:
        # Todo: Return 405 Response
        return HttpResponse("Method Not Allowed", status=405)
