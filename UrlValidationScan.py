import validators # Import that validates url formats 

# Defining a funciton to use import against url
def ValidatorsScan(url):

    # import that validates a given urls format ensuring it is a valid url
    ValidateUrl = validators.url(url)

    # return clear if the validation was sucessful, else return invaluid.
    if str(ValidateUrl) == "True":
        return "Clear"
    else:
        return "Invalid"

