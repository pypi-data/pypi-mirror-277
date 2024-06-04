# fastapi_helmet/utils.py
def generate_csp(directives: dict) -> str:
    return "; ".join(f"{key} {value}" for key, value in directives.items())
