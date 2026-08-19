"""DELIBERATELY VULNERABLE — BreachLens Secret-scan test target.

The AWS key below is AWS's DOCUMENTED, NON-FUNCTIONAL example credential
(see the AWS docs) — detector bait, not a real secret. Do NOT deploy.
"""

# Secret: hardcoded AWS credentials.
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

# Secret: hardcoded database password.
DB_PASSWORD = "SuperSecretP@ssw0rd123"

# Secret: hardcoded Flask secret key.
SECRET_KEY = "hardcoded-flask-secret-key-do-not-use"
