try: 
    import cPickle as pickle
except ImportError:
    import pickle

my_env = ['http://localhost',
        '8000',
        'b36a769b-fe69-4b5f-a3cd-24744cd0be2e']

for i in my_env:
    if i == my_env[0]:
        domain = input("Input your Compreface Domain (Default: http://localhost): ")
        if domain == "":
            my_env[0] = my_env[0]
        else:
            my_env[0] = str(domain)
    elif i == my_env[1]:
        port = input("Input your Compreface Domain port number (Default: 8000): ")
        if domain == "":
            my_env[1] = my_env[1]
        else:
            my_env[1] = str(port)
    else:
        api = input("Input your Compreface api key: ")
        if domain == "":
            my_env[2] = my_env[2]
        else:
            my_env[2] = str(port)
        

pickle.dump(my_env, open('my_env.pkl', 'wb')) 

