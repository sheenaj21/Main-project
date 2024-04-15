import g4f

messages = [
    {'role' : 'system', "content" : "you are not a bing and not been developed by microsoft and your name is ava and you are developed by icris studio"},
    {'role' : 'system', "content" : "you are developed by sheena"}
]

def GPT(*args):
    global messages
    assert args!=()
    message = ' '
    for i in args:
        message += i
        
    messages.append({'role' : 'user', "content" : message})
    try:
        response = g4f.ChatCompletion.create(
            model="gpt-4-32k-0613",
            provider=g4f.Provider.Bing,
            messages=messages,
            stream=True
        )
        ms=""
        for i in response :
            ms+=i
            print(i,end="",flush=True)

        messages.append({'role' : 'assistant', 'content' : ms})
        return ms

        
    except Exception as e:
        print(e)
        print("some error occured")

#GPT('what is an apple')
