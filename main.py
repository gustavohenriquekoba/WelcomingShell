import assets

def main():
    assets.clear()
    print("---------------------------------------")
    print("   Welcome - To - Your - Shell   ")
    print(f"   Current User: {assets.user_name()}")
    print(f"   IP: {assets.user_ip()}")
    print(f"   Current Time: {assets.time_of_login()}")
    print("---------------------------------------")
    print("")
    print(f"{assets.welcoming_quote()}")

if __name__ == '__main__':
    main()