from scratchclient import ScratchSession, ScratchExceptions
import getpass
import json
import os

loginloop = True
while loginloop:
  try:
    os.system("clear")
    print("VarMesh V1")
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    session = ScratchSession(username, password)
    loginloop = False
  except ScratchExceptions.InvalidCredentialsException:
    os.system("clear")
    print("Username or passowrd is invalid")
    input()
    loginloop = True

settings = json.load(open('settings.json', ))

try:
  connection1 = session.create_cloud_connection(settings["proj1"])
  connection2 = session.create_cloud_connection(settings["proj2"])
except AttributeError:
  os.system("clear")
  print("Something in settings.json isnt right. Check settings.json")
  input()
  exit()

def setvar1(val):
  connection1.set_cloud_variable(settings["var1"], val)
def setvar2(val):
  connection2.set_cloud_variable(settings["var2"], val)

try:
  oldvar1 = connection1.get_cloud_variable(settings["var1"])
  oldvar2 = connection2.get_cloud_variable(settings["var2"])
  var1 = connection1.get_cloud_variable(settings["var1"])
  var2 = connection2.get_cloud_variable(settings["var2"])
except ValueError:
  os.system("clear")
  print("Something in settings.json isnt right. Check settings.json")
  input()
  exit()

os.system("clear")
print("Linked        ")
print(var1 + " <------> " + var2)


while True:
  var1 = connection1.get_cloud_variable(settings["var1"])
  var2 = connection2.get_cloud_variable(settings["var2"])
  if var1 != oldvar1:
    setvar2(var1)
    oldvar1 = var1
    oldvar2 = var1
    var1 = connection1.get_cloud_variable(settings["var1"])
    os.system("clear")
    print("Linked       ")
    print(var1 + " <------>" + var2)
  if var2 != oldvar2:
    setvar1(var2)
    oldvar1 = var2
    oldvar2 = var2
    var1 = connection1.get_cloud_variable(settings["var1"])
    os.system("clear")
    print("Linked")
    print(var1 + " <------> " + var2)
