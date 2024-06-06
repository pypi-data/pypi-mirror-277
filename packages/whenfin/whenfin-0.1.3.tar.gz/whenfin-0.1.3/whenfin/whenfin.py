import requests

class Whenfin(object):
  USER = None
  PROJECT_NAME = None
  PROJECT_SECRET = None
  BACKEND_URL = "https://whenfin-api.l-uca.com"

  @staticmethod
  def connect(u, pn, ps):
    response = requests.post(Whenfin.BACKEND_URL + "/validate_project_exists", json={"user": u, "project_name": pn, "project_secret": ps})
    json_response = response.json()
    if "error" in json_response:
      raise Exception(json_response["error"])
    if json_response["valid"]:
      Whenfin.USER = u
      Whenfin.PROJECT_NAME = pn
      Whenfin.PROJECT_SECRET = ps
      print("Whenfin connected successfully")
    else:
      raise Exception("Unable to connect to Whenfin")
      

  @staticmethod
  def send(title, message):
    if Whenfin.USER == None:
      raise Exception("Whenfin not setup yet; call connect()")
    package = {
      "user": Whenfin.USER,
      "project_name": Whenfin.PROJECT_NAME,
      "project_secret": Whenfin.PROJECT_SECRET,
      "title": title,
      "message": message,
    }
    response = requests.post(Whenfin.BACKEND_URL + "/send_notification", json=package)
    print(response.json())

    