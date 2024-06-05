from pathlib import Path
from typing import Optional, Union, List

import requests


class Jupy:
    """The Jupy SDK for https://jupy.dev.

    The SDK helps interact with the Jupy API.

    Parameters:
        api_key (str): The API key for the request. Defaults to the one set in the SDK.
    """

    def __init__(self, api_key: Optional[str] = None) -> None:
        self.base_url = "https://app.jupy.dev"
        self.api_key = api_key

    def create_notebook(
        self,
        content: Union[bytes, str, Path],
        name: str,
        namespace: str,
        description: Optional[str] = None,
        tags: Optional[List[str]] = None,
        api_key: Optional[str] = None,
    ) -> dict:
        """Create a new notebook.

        Args:
            content (Union[bytes, str, Path]): The content of the notebook. This is expected to be a path to Jupyter notebook.
            name (str): The name of the notebook.
            namespace (str): The namespace of the notebook.
            description (Optional[str]): The description of the notebook.
            tags (Optional[List[str]]): The tags of the notebook.
            api_key (Optional[str]): The API key for the request. Defaults to the one set in the SDK.

        Returns:
            dict: The response from the API.
        """
        api_key = api_key or self.api_key
        if api_key is None:
            raise ValueError("API key is required. You must provide one either on init or as an argument.")

        if isinstance(content, str):
            with open(content, "rb") as file:
                loaded_content = file.read()
        elif isinstance(content, Path):
            loaded_content = content.read_bytes()

        response = requests.put(
            f"{self.base_url}/api/v1/notebooks/",
            headers={"Authorization": f"Bearer {api_key}"},
            data={
                "name": name,
                "namespace": namespace,
                "description": description,
                "tags": ",".join(tags) if tags else None,
            },
            files={"content": loaded_content},
        )
        response.raise_for_status()
        return response.json()
