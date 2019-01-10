import datetime

slackish = {}
#{'home': {'messages': [{'author': 'andy', 'datestamp': '2018-12-17-06:43:54', 'content': 'here is my message'}]}}


def newMessage(channel, author, content):
    # checks is channel size is within range parameters
    if len(slackish[channel]['messages']) < 100:
        print(len(slackish[channel]['messages']))
        # creates datestamp
        time = datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
        # creates message object
        message = {'author': author, 'datestamp': time, 'content': content}
        # inserts message into appropriate channel object
        slackish[channel]['messages'].insert(0, message)
        return slackish
    else: 
        # if channel is at max size, deletes oldest message and calls the function again.
        slackish[channel]['messages'].pop()
        newMessage(channel, author, content)

def newChannel(channelName):
    # checks if channel already exists
    if channelName in slackish.keys():
        print('already a channel')
    # creates new channel object
    else: 
        print('new channel created')
        slackish[channelName] = {'messages': []}
        return slackish


newChannel('home')
newChannel('home')
# test for what program does at channel's max capacity
# i = 0
# while i < 110:
#     content = ('%(language)sth message.' %{'language': i})
#     newMessage('home', 'andy', content)
#     i += 1

# newMessage('home', 'andy', '2nd message')