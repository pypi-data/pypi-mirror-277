import requests

from .conf import settings
from .jwt import generate_jwt


class Client:
    def __init__(self, remote_module: str) -> None:
        self.remote_module = remote_module

    def _get_protocol_and_host(self):
        if self.remote_module in settings.INTERCONNECT_OVERRIDE_MODULE_HOST:
            return settings.INTERCONNECT_OVERRIDE_MODULE_HOST[self.remote_module]

        host = self._get_host()
        protocol = "https" if settings.INTERCONNECT_USE_SSL else "http"
        if settings.INTERCONNECT_PORT:
            port = settings.INTERCONNECT_PORT
            return f"{protocol}://{host}:{port}"
        return f"{protocol}://{host}"

    def _get_host(self):
        environment_domain = settings.INTERCONNECT_ENVIRONMENT_DOMAIN
        return f"{self.remote_module}.{environment_domain}"

    def _make_url(self, path: str):
        if not path.startswith("/"):
            path = f"/{path}"
        protocol_and_host = self._get_protocol_and_host()
        return f"{protocol_and_host}{path}"

    def _call_api_by_path(self, method, path, *args, **kwargs):
        url = self._make_url(path)
        return self._call_api(method, url, *args, **kwargs)

    def _call_api(self, method, url, *args, **kwargs):
        method_function = getattr(requests, method)
        headers = {
            **kwargs.pop("headers", {}),
            **self._make_headers(),
        }
        result = method_function(
            url,
            *args,
            headers=headers,
            **kwargs,
        )
        return result

    def _make_headers(self):
        jwt = generate_jwt()
        headers = {
            "Authorization": f"Bearer {jwt}",
        }
        return headers

    def get(self, path, *args, **kwargs):
        return self._call_api_by_path("get", path, *args, **kwargs)

    def post(self, path, *args, **kwargs):
        return self._call_api_by_path("post", path, *args, **kwargs)

    def patch(self, path, *args, **kwargs):
        return self._call_api_by_path("patch", path, *args, **kwargs)

    def delete(self, path, *args, **kwargs):
        return self._call_api_by_path("delete", path, *args, **kwargs)

    def get_all(self, path, *args, **kwargs):
        url = self._make_url(path)
        while url:
            result = self._call_api("get", url, *args, **kwargs)
            result.raise_for_status()
            response = result.json()

            yield from response["results"]

            url = response.get("next")
            if "params" in kwargs:
                del kwargs["params"]
