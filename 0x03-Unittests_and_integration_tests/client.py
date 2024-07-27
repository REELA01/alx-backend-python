#!/usr/bin/env python3
"""git hub client"""
from typing import (
    List,
    Dict,
)

from utils import (
    get_json,
    access_nested_map,
    memoize,
)


class GithubOrgClient:
    """github client"""
    ORG_URL = "https://api.github.com/orgs/{org}"

    def __init__(self, org_name: str) -> None:
        """initialization"""
        self._org_name = org_name

    @memoize
    def org(self) -> Dict:
        """memorize org"""
        return get_json(self.ORG_URL.format(org=self._org_name))

    @property
    def _public_repos_url(self) -> str:
        """public repo URL"""
        return self.org["repos_url"]

    @memoize
    def repos_payload(self) -> Dict:
        """memorize repo payload"""
        return get_json(self._public_repos_url)

    def public_repos(self, license: str = None) -> List[str]:
        """public repos"""
        json_payld = self.repos_payload
        public_repo = [
            repo["name"] for repo in json_payld
            if license is None or self.has_license(repo, license)
        ]
        return public_repo

    @staticmethod
    def has_license(repo: Dict[str, Dict], license_key: str) -> bool:
        """static"""
        assert license_key is not None, "license_key cannot be None"
        try:
            has_license = access_nested_map(
                repo,
                ("license", "key"),
            ) == license_key
        except KeyError:
            return False
        return has_license
