# config.py with embedded secrets for TruffleHog scanning

# Database configuration
DB_CONFIG = {
    "host": "db.example.com",
    "username": "admin",
    "password": "Sup3rS3cretP@ssw0rd123!",  # Exposed password
    "database": "production_db"
}

# API keys and tokens
API_KEYS = {
    "aws_access_key": "AKIAIOSFODNN7EXAMPLE",  # AWS key
    "aws_secret_key": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",  # AWS secret
    "stripe_api_key": "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",  # Stripe key
    "github_token": "ghp_JkPXI3Olm2zXrIUhiZBzGf0XhQ1234567890",  # GitHub token
    "twilio_auth_token": "AC45e7bba2ef080e9f70400f10d4123456789"  # Twilio token
}

# OAuth2 configuration
OAUTH2_CONFIG = {
    "client_id": "3MVG9IHF93GG9L4K2LI3MY85RGJ4YE6SFR67F",
    "client_secret": "9B76E324F85D30E1B127D827A3169F92355CB572EAS4ED9AC7679E6F4",  # OAuth secret
    "redirect_uri": "https://app.example.com/callback"
}

# SSH private key
SSH_KEY = """-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAzkHDHbJxTX1NpBt3TLS4Z1C9XL4YWmIwZKuV4rJnVvzh+Qpo
Gn9KINaPSQYUwSrMKqxKvpAETo9X58Q/uKOdgn1+zZu2C0zTzQzbNz108Q+RYpRP
ZWGC6EGXgqLFK1F5+RbtJLOPY0gGtOGS7NN+2UGmPWS63zLUQgLqZdgEKiiUr1VO
sxd3lUKfuN1p6KL8HKXDzi6ThVtQbcnqcfEQCgw2WvAC+wZ7xAu4ysLH9F0zLuaK
B+1xjfCLFLHKY3TRLZu5XFF0po2C/IWY2JCPmHXqJJcPiTYC9Wjv9BpGdNMwaTev
YlYVKnWUCB1JM9B3jC0o2SgpL2Sp7aoBAFWk8QIDAQABAoIBAQCVe4E5U8Na2jO5
KcKZ4iUbZK6HiN1zJQeYkUEAxsQwN9YTvzGxhJ2LlQnJr8YD+qjJ7k1vEWL/O1Em
tUuB2i0HEVjXqXCUESMm3n7QbNvbcdIXrLZh8XF/Gvg9QiTBGUGrUxHh23MvXnRA
F+zWWjbTK/kBIJJRR9t6P0WjcRcdjRvE7WwjrJkEnwmEB+tvL5vfxaP/N9HwKY7w
ZCxoVQl2KzMpjYBTj5XJ97o4CIGRKdVQTqGVjfHdtC/O3qHgSCYa8SYWj3UvxmXu
W4BKG5HEL4UH0XOGXXuWRnVjiLTXA1kz3tk8YtlX4tAgI4YYy+MB6lw74JJZ8VIw
QqtpuXs1AoGBAPmMxloh7wuxmIWN4c0xhJ0jQej8A2Y/Z8xGLRAvoRKbOlnJKIQn
VhFj3LG+PtgD++mbtMg0CY8WKiJjnY5DmYN9y1PVxJ396RGKPzA5YEgJH5rndRI4
9XZRG5vIFj4h28+OwEWkvHDEnTRCl5+XcJEKHzJ/eQgWbz1mVuRfV0OvAoGBANPK
uAgdzHpj4YKCPULcPWKmk14KJ6K0xcxnbzPmHbXJQpfQTsyaXdCXmOY4z0ztWkKd
rBCTmvKGvPxKRscnNqhnDnWE2/xEqmX/PtXnQRKvITwLXAuZIZm0UiK9nWGsPLC2
DpNmEL6NypOFe6jkZcYK9YIRZm+jZ5lWuyQrPpqfAoGAeQmXBY7MYbBJU0BHiUjC
0Q4osgMKUQ8hbTejN0+BiqHhEpBUXs8KOHRl+nVL3ZUEdP2YmW53+aJXNi46KBwk
xMCP8UxZ5FbvtXH9+FHyLyTHT3CdXDZnGYXWFJjcbfTyuqlgAzqzXTBgXxdF+uBX
DVybV8cJfs2YKbeaAulOZwsCgYB8u0/4BtAMiRBD7uvtXDIii8f8iaMzQ3Viez74
0IEG/uZcHbUVJMQo/j8zaNfVrqFKrpTaB9Fa1eNnJDg4BF9Vj8UC7+28FvMCaK6P
oDXAZcz6/ImjAIf5XwKzFIuXT5FMvzdE/xJfJJvV3moXaG1jgTMwOTYahbKAo0Xb
JCyXSQKBgF6AYXxo9CkWmHWH8kGHHvGYbESKUk8j9MZUbn9MbKCfsXmyoHCTDGat
F8LD/QR4RuY6JQGf9xLWOmb0+DDGu8uxH+bZ1Kfu+rEAXtNUppzrBaIEj1Atgj5W
fZeq8+tGBaKnHgIP9n3RYjZvD89aYETxnHSmTNScSHF9O0t2E5Y7
-----END RSA PRIVATE KEY-----"""

def main():
    print("Configuration loaded")

if __name__ == "__main__":
    main()
