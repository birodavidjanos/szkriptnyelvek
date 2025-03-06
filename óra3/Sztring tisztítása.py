proxy_list = ["192.20.246.138:\n 6666", "206.130.99.82:\n8080"]
cleaned_proxy_list = []

for proxy in proxy_list:  
    cleaned_proxy_list.append(proxy.replace(" ", ""))

print(cleaned_proxy_list)