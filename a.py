class Dict2Class(object):

    def __init__(self, my_dict):
        for key in my_dict:
            setattr(self, key, my_dict[key])

        # Driver Code


if __name__ == "__main__":
    # Creating the dictionary
    my_dict = {"name": "Geeks",
               "address": "1223 o lane"
               }

    s = Dict2Class(my_dict)
    print(s.address)
