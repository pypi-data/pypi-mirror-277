from typing import Literal

from .auth_client import AuthClient  # noqa: F401
from .search_client import SearchClient  # noqa: F401

Datasources = Literal["confluence", "google-drive", "jira", "zendesk", "slack", "sharepoint"]
