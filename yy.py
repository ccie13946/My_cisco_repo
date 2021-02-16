
"""
class Student:
    def __init__(self,name,age,height):
        self.name = name
        self.age = age
        self.height = height

print("lala")

"""
import netmiko
import json
import getpass
"""
devices = """
#10.160.21.101
#10.160.21.102
""".strip().splitlines()

device_type = 'cisco_ios_telnet'
username = ''
password = ''

for device in devices:
  try:
    print("-"*80)
    print("connecting to device",device)
    connection = netmiko.ConnectHandler(ip = device,device_type = device_type,
                                        username = username,password = password)
    print(connection.send_command('show ip int brief'))
    connection.disconnect()
  except:
    print("there is an error")
"""
"""
r1 = {'ip': '10.160.21.101', 'device_type': 'cisco_ios_telnet', 'username': '', 'password': ''}
r2 = {'ip':'10.160.21.102','device_type': 'cisco_ios_telnet','username' : '','password': ''}
devices = [r1,r2]

for device in devices:
  try:
    print("-"*80)
    print("connecting to device",device['ip'])
    connection = netmiko.ConnectHandler(**device)
    print(connection.send_command('show ip int brief'))
    connection.disconnect()
  except:
    print("there is an error")
"""
"""
devices =[ {'ip': '10.160.21.101', 'device_type': 'cisco_ios_telnet', 'username': '', 'password': ''},
           {'ip':'10.160.21.102','device_type': 'cisco_ios_telnet','username' : '','password': ''}]


for device in devices:
  try:
    print("-"*80)
    print("connecting to device",device['ip'])
    connection = netmiko.ConnectHandler(**device)
    print(connection.send_command('show ip int brief'))
    connection.disconnect()
  except:
    print("there is an error")

"""


"""
with open('devices.json') as dev_file:
   devices = json.load(dev_file)


for device in devices:
  try:
    print("-"*80)
    print("connecting to device",device['ip'])
    connection = netmiko.ConnectHandler(**device)
    print(connection.send_command('show ip int brief'))
    connection.disconnect()
  except:
    print("there is an error")
"""
#import signal
#signal.signal(signal.SIGPIPE,signal.SIG_DFL)
#signal.signal(signal.SIGINT,signal.SIG_DFL)
import sys
if len(sys.argv) < 3:
  print('command usage:yy.py router_commands.txt devices.json')


def get_input(prompt = ''):
  line = input(prompt)
  return line

#username = get_input("Enter your username: ")
#password = get_input("Enter your password: ")


def get_credentials():
  username = get_input("Please enter your username: ")
  #password = None
  #while password:
  password = getpass.getpass()
#      password_verify = password_verify("pls re-eneter your password")
 #     if password != password_verify:
  #      print("password does not match,pls retry: ")
        # password = None
  return username,password



username,password = get_credentials()

with open(sys.argv[1]) as router_command:
  commands = router_command.readlines()



with open(sys.argv[2]) as dev_file:
  devices = json.load(dev_file)


for device in devices:
  device["username"] = username
  device["password"] = password
  try:
    print("-" * 80)
    print("connecting to device", device['ip'])
    connection = netmiko.ConnectHandler(**device)
    filename = connection.base_prompt+ '.txt'
    with open(filename,"w") as file:
      for command in commands:
        file.write("###output of "+command+'\n\n')
        file.write(connection.send_command(command))
    connection.disconnect()
  except:
    print("there is an error")