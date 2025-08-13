import csv

class CredentialManager:
    def __init__(self, credentials_csv):
        self.credentials = self._load_credentials(credentials_csv)
        self.index = 0

    def _load_credentials(self, file_path):
        creds = []
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                creds.append(row)
        return creds

    def get_next_credential(self):
        cred = self.credentials[self.index]
        self.index = (self.index + 1) % len(self.credentials)
        return cred
