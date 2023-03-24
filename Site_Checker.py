import urllib.request as urllib


def site_checker(url):
    print("Checking connectivity ")

    response = urllib.urlopen(input_url)
    print(f"Connected to ,{url}, Successfully")
    print("The response code was:", response.getcode())


print("This is a site connectivity checker program")
input_url = input("Input the url of the site you want to check: ")


site_checker(input_url)
