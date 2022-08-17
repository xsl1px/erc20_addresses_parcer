from requests import get
import json

API_KEY = "YOUR_ETHERSCAN_API_KEY_HERE"
BASE_URL = "https://api.etherscan.io/api"

def make_api_url(module, action, address, **kwargs):
	url = BASE_URL + f"?module={module}&action={action}&address={address}&apikey={API_KEY}"
	for key, value in kwargs.items():
		url += f"&{key}={value}"
	return url

def get_account_balance(address):
	balance_url = make_api_url("account", "txlistinternal", address, tag="latest")
	response = get(balance_url)
	data = response.json()
	value = data["result"]
	new_list = []
	for a in value:
		new_list.append(a['from'])
	return(list(dict.fromkeys(new_list)))

def get_account_balance_erc20(address):
	balance_url_erc20 = make_api_url("account", "tokentx", address, tag="latest")
	response_erc20 = get(balance_url_erc20)
	data_erc20 = response_erc20.json()
	value_erc20 = data_erc20["result"]
	new_list_erc20 = []
	for a in value_erc20:
		new_list_erc20.append(a['from'])
	return(list(dict.fromkeys(new_list_erc20)))

address = "INSERT_ADDRESS_HERE"
zero = "0x0000000000000000000000000000000000000000"
total_list = get_account_balance(address) + get_account_balance_erc20(address)
for b in total_list:
	if b == zero:
	 	total_list.remove(zero)
print(total_list)
print(len(set(total_list)))
