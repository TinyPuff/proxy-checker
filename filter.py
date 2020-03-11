# To-Do: 1- I should use threads to get the job done as quickly as possible.
# 2- Allow the user to pick their own input and output file.
import requests as req
from fake_useragent import UserAgent


def filter():  # Puts the proxies that work in a file named "result.txt"
    print("Note that every time you check the quality of these proxies, the previous proxies"
          + " saved in result.txt\n" + "will be deleted. You may want to copy them and save them in another "
          + "text file")
    while True:
        make_sure = input("Are you sure you want to do this?(y/n)\n> ").lower()
        if make_sure in ["y", "yes"]:
            print("Here we go...")
            result = open('result.txt', 'w')
            break
        elif make_sure in ["n", "no"]:
            print("Ciao!")
            return 0

    proxy_list = open('default.txt')
    for proxy in proxy_list:
        success = []
        fail = []
        ua = UserAgent()
        user_agent = ua.random
        headers = {
            "User-Agent": user_agent
        }
        proxy_dict = {
            "http": f"http://{proxy}",
            "https": f"http://{proxy}"
        }
        target = '<img alt="Google"'
        bw = 7
        for i in range(3):
            if 1 in success:
                break
            try:
                resp1 = req.get("https://www.google.com", headers=headers, proxies=proxy_dict, timeout=bw)

                if target in resp1.text:
                    # print(f"{proxy}: Successful!")
                    print("{}".format(proxy.strip('\n')))
                    success.append(1)
            except (req.exceptions.ProxyError, req.exceptions.ConnectTimeout, req.exceptions.ConnectionError):
                # print(f"{proxy}: Failure!")
                fail.append(0)
                pass
            bw -= 3

        if 1 in success:
            result.write(proxy)
    result.close()


def dtbl():  # Deletes the blank lines
    try:
        with open('result.txt', 'r') as f:
            lines = f.readlines()
        with open('result.txt', 'w') as f:
            for line in lines:
                if line.strip("\n") != "":
                    f.write(line)
    except FileNotFoundError:
        pass


if __name__ == "__main__":
    a = filter()
    if a != 0:
        dtbl()
