import requests
from datetime import datetime


username="ayush2000"
token="erangd65h4gghfh8"
pixela_endpoint="https://pixe.la/v1/users"
user_params={
    "token":token,
    "username":username,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}
# response=requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)
graph_endpoint=f"{pixela_endpoint}/{username}/graphs"

graph_config={
    "id":"graph1",
    "name":"Swimming",
    "unit":"minutes",
    "type": "int",
    "color":"sora",
}
headers={
    "X-USER-TOKEN":token,

}
today=datetime.now()
time_format=today.strftime("%Y%m%d")

pixel_endpoint=f"{pixela_endpoint}/{username}/graphs/{graph_config['id']}"
pixel_config={
    "date":time_format,
    "quantity":"60",
}
#
# response=requests.post(url=pixel_endpoint, json=pixel_config,headers=headers)
# print(response.text)
"""Go to "https://pixe.la/v1/users/ayush2000/graphs/graph1.html" to track your habits daily"""
update_endpoint=f"{pixela_endpoint}/{username}/graphs/{graph_config['id']}/{time_format}"
new_pixel_data={
    "quantity": "75"
}
delete_endpoint=f"{pixela_endpoint}/{username}/graphs/{graph_config['id']}/{time_format}"
response=requests.delete(url=delete_endpoint,headers=headers)
print(response.text)