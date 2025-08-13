import csv

class ProxyManager:
    def __init__(self, proxy_csv):
        self.proxies = self._load_proxies(proxy_csv)
        self.index = 0

    def _load_proxies(self, file_path):
        proxies = []
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                proxies.append(row)
        return proxies

    def get_next_proxy(self):
        proxy = self.proxies[self.index]
        self.index = (self.index + 1) % len(self.proxies)
        return proxy
