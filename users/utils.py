import secrets

def generate_api_key():
    return secrets.token_hex(32) # Option 07a4c758442597ee841ae49e51e677f5
    # return secrets.token_urlsafe(16) # zk5R7g9WAUQ1hsNFc06aoA