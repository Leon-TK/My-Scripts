from requests import get

ip = get('https://checkip.amazonaws.com').content.decode('utf8')
print('My public IP address is: {}'.format(ip))