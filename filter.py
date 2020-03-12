import requests as req


def filter():
    """ Puts the proxies that work in a file named 'result.txt' """

    print(
        '''Note that every time you check the quality of these proxies, the previous proxies saved in output file will be deleted.
You may want to copy them and save them in another text file''')

    global default_input
    default_input = "IO/default.txt"
    global default_output
    default_output = "IO/result.txt"
    protocols = ["HTTP", "HTTPS", "SOCKS5"]
    for i in protocols:
        print("-", i)
    while True:
        print("What protocol are your target proxies using?")
        proto = input("> ").upper()
        if proto in protocols:
            break
    while True:
        try:
            choice = int(input(
                "Enter 0 for using custom input/output files and enter 1 for using the default ones.\n> "))
            if choice == 1:
                result = open(default_output, 'w')
                proxy_list = open(default_input)
                break
            elif choice == 0:
                proxy_list = open(
                    input("Enter the path to the input file: (e.g. C:/Downloads/proxies.txt)\n> "))
                result = open(
                    input("Enter the path to the output file: (e.g. C:/Downloads/result.txt)\n> "),
                    'w')
                break
        except (ValueError, FileNotFoundError):
            pass

    for proxy in proxy_list:
        success = []
        fail = []
        if proto in ("HTTP", "HTTPS"):
            proxy_dict = {
                "http": f"http://{proxy}",
                "https": f"http://{proxy}"
            }
        elif proto == "SOCKS5":
            proxy_dict = {
                "http": f"socks5://{proxy}",
                "https": f"socks5://{proxy}"
            }
        target = '<img alt="Google"'
        bw = 7
        for i in range(3):
            if 1 in success:
                break
            try:
                resp1 = req.get(
                    "https://www.google.com",
                    proxies=proxy_dict,
                    timeout=bw)

                if target in resp1.text:
                    print("{}".format(proxy.strip('\n')))
                    success.append(1)
            except (req.exceptions.ProxyError, req.exceptions.ConnectTimeout, req.exceptions.ConnectionError):
                fail.append(0)
            bw -= 3

        if 1 in success:
            result.write(proxy)
    result.close()


def dtbl():
    """ Deletes the blank lines """

    try:
        with open(default_output, 'r') as f:
            lines = [line for line in f]
        with open(default_output, 'w') as f:
            for line in lines:
                if line.strip("\n") != "":
                    f.write(line)
    except FileNotFoundError:
        pass


def main():
    """ Executes everything """
    a = filter()
    if a != 0:
        dtbl()


if __name__ == "__main__":
    main()
