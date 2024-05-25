import scratchattach as scratch
from scratchattach import Session
import time

session = Session(".eJxVj01PhDAQhv8LZxdptxTYmxyM0UTj166eyLSdLhVoCZSQrPG_2yZc9vo-M8-885ssM04WBkwOiZjcamEce5xhkZjcJN51aAOhpdZElUIiICtzDTwDDQx5XmlSCHJonnbDl5Cn9X56rT_k8f34-HmqH17gkgVN787G7swYTMU-rXjK05yEvIHFt01s0BgVICnynNGMBaR-wJ5d482AF2dju7sBJyPh9hnX5ttN3fV-C3MbhrKM0ZKCLJRgiksmKdWswHJfMZ1zXUnUBDmNpTzOXjrXmShfgxDVtVKADN_HXjFD68N1b5xNNzCnbzj2W1hvw3__171vEw:1sAKDe:Un6EETGHLDY2S8Pv_wmARtmmGZ8", username="brownapplesauce")

connection = session.connect_cloud("1026857057")

client = scratch.CloudRequests(connection)

@client.request
def follow(who, from_user):
    
    user = session.connect_user(who)
    
    user.follow()
    
    time.sleep(5)
    
    print(f"Now following {who}, courtesy of {from_user}")
    
    return "Done"

@client.request
def unfollow(who, from_user):
    
    user = session.connect_user(who)
    
    user.unfollow()
    
    time.sleep(5)
    
    print(f"Now unfollowing {who}, courtesy of {from_user}")
    
    return "Done"

@client.event
def on_ready():
    print("Client is connected")

client.run()
