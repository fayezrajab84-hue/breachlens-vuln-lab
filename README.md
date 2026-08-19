# breachlens-vuln-lab

**Deliberately vulnerable test target for BreachLens.** Every file here contains
*intentional* security defects — one tier per file — so a code scan lights up all
four scanners. **Do not deploy, `docker build`, or `terraform apply` any of this.**

| Tier | File | Deliberate defect |
|---|---|---|
| **SAST** | `app.py` | OS-command injection, `eval`, SQL string-concat, MD5 password hash, Flask `debug=True`, bind `0.0.0.0` |
| **SCA** | `requirements.txt` | pins known-CVE versions (Flask 0.12.2, PyYAML 3.13, Django 2.0.0, requests 2.19.0, …) |
| **IaC** | `terraform/main.tf`, `Dockerfile` | public-read S3, SSH open to `0.0.0.0/0`, unencrypted + public RDS, container runs as root |
| **Secret** | `config.py` | AWS **example** key (`AKIAIOSFODNN7EXAMPLE`), hardcoded DB password + app secret |

> The AWS key is AWS's **published, non-functional example credential** — detector
> bait, never a real secret. The passwords are obvious placeholders.
