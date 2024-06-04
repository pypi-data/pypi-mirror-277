# fastapi_helmet/settings.py
from pydantic import BaseModel


class HelmetSettings(BaseModel):
    x_content_type_options: bool = True
    x_frame_options: bool = True
    x_xss_protection: bool = True
    referrer_policy: bool = True
    content_security_policy: bool = True
    strict_transport_security: bool = True
    expect_ct: bool = True
    custom_headers: dict = {}
