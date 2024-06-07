import slugify
import clisync
import toml
import os
import logging

from typing import Optional, List
import pyhectiqlab.settings as settings
from pyhectiqlab.client import Client
from pyhectiqlab.decorators import classproperty, online_method, functional_alias

logger = logging.getLogger()


class Project:
    """
    Project class for handling project related operations.

    Args:
        slug (str): Slug of the project.
        configs (str): Path to the config file.
        allow_dirty (bool): Allow dirty state of the project.
        client (Client): Client object.
    """

    _slug: str = settings.getenv("HECTIQLAB_PROJECT", None)
    _configs: str = settings.getenv("HECTIQLAB_CONFIGS", os.path.expanduser("~/.hectiq-lab/configs.toml"))
    _allow_dirty: Optional[bool] = None
    _client: Client = Client

    @classproperty
    def slug(cls) -> str:
        return cls._slug

    @classproperty
    def repo(cls) -> str:
        if not cls._slug:
            return None
        if not os.path.exists(cls._configs):
            return None
        with open(cls._configs, "r") as file:
            config = toml.load(file)
            return config.get(cls._slug, {}).get("repo")

    @classmethod
    def allow_dirty(cls) -> bool:
        if not Client.online():
            return True
        if cls._allow_dirty is None and os.path.exists(cls._configs):
            with open(cls._configs, "r") as file:
                config = toml.load(file)
                cls._allow_dirty = not config.get(cls._slug, {}).get("force_no_git_diff", False)
        return cls._allow_dirty or True

    @staticmethod
    @online_method
    @clisync.include()
    def create(
        name: str,
        repo: Optional[str] = None,
        force_no_git_diff: bool = True,
        write_config: bool = True,
    ) -> Optional[str]:
        """
        Create a project.

        Args:
            name (str): Name of the project.
            repo (str, optional): Repository URL. Default: None.
            force_no_git_diff (bool): Force no git diff. Default: True.
            write_config (bool): Write the config file. Default: True.
        """
        from pyhectiqlab.const import DISABLE_PROJECT_CREATION

        if DISABLE_PROJECT_CREATION:
            logging.error("Project creation is disabled. Continuing anyway...")
            return
        slug = "/".join([slugify.slugify(n) for n in name.split("/")])
        body = {
            "slug": slug,
            "name": name,
            "repo": repo,
            "force_no_git_diff": force_no_git_diff,
        }
        project = Project._client.post("/app/projects", json=body, wait_response=True)
        if project is None:
            logging.error(f"Failed to create project.")
            return
        if write_config:
            Project.write_config(slug)
        logger.info(f"Project `{slug}` created.")
        return slug

    @staticmethod
    @online_method
    def write_config(project: str):
        if not os.path.exists(Project._configs):
            config = {project: {}}
        else:
            config = toml.load(Project._configs)
            config[project] = {}
        project = Project.retrieve(project, fields=["slug", "repo", "force_no_git_diff", "description"])
        config[project["slug"]]["repo"] = project.get("repo")
        config[project["slug"]]["force_no_git_diff"] = project.get("force_no_git_diff")
        config[project["slug"]]["description"] = project.get("description")

        with open(Project._configs, "w") as file:
            toml.dump(config, file)

    @staticmethod
    @online_method
    def exists(slug: str) -> bool:
        project = Project._client.get(f"/app/projects/{slug}", wait_response=True)
        if project is None:
            return False
        return True

    @staticmethod
    @online_method
    @functional_alias("retrieve_project")
    @clisync.include()
    def retrieve(
        slug: str,
        fields: Optional[List[str]] = [],
        update_config: bool = False,
    ) -> Optional[dict]:
        """Retrieve a project info.

        Args:
            slug (str): Slug of the project.
            fields (List): Fields to retrieve.
        """
        info = Project._client.get(f"/app/projects/{slug}", params={"fields": fields}, wait_response=True)
        if update_config:
            Project.write_config(slug)
        return info

    @staticmethod
    @functional_alias("get_project")
    def get(slug: Optional[str] = None):
        return slug or Project._slug

    @staticmethod
    @functional_alias("set_project")
    def set(slug: str):
        if not Project.exists(slug):
            logging.error(f"The project `{slug}` does not exist. Continuing with the current project.")
            Project._client.online(False)
            return
        Project._slug = slug
