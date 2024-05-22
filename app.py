import scratchattach as scratch3

session = scratch3.Session(".eJxVj01PhDAQhv8LZxdptxTYmxyM0UTj166eyLSdLhVoCZSQrPG_2yZc9vo-M8-885ssM04WBkwOiZjcamEce5xhkZjcJN51aAOhpdZElUIiICtzDTwDDQx5XmlSCHJonnbDl5Cn9X56rT_k8f34-HmqH17gkgVN787G7swYTMU-rXjK05yEvIHFt01s0BgVICnynNGMBaR-wJ5d482AF2dju7sBJyPh9hnX5ttN3fV-C3MbhrKM0ZKCLJRgiksmKdWswHJfMZ1zXUnUBDmNpTzOXjrXmShfgxDVtVKADN_HXjFD68N1b5xNNzCnbzj2W1hvw3__171vEw:1s9Ums:yYA2TzIhVTSxb6kgxIFgMe95tl8", username="brownapplesauce")

conn = session.connect_cloud("1025120117")

client = scratch3.CloudRequests(conn)

pong = 0

@client.request
def follower_number(username):
    user = scratch3.get_user(username)
    followers = user.follower_count()
    print(followers)
    return followers

@client.request
def message_number(username):
    user = scratch3.get_user(username)
    messages = user.message_count()
	print(messages)
    return messages

@client.event
def on_ready():
    print("Request handler is ready")

client.run()
