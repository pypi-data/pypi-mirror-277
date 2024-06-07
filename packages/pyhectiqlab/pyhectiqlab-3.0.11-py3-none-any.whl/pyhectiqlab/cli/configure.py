import os
import click

from typing import Optional


@click.group()
def config_group():
    pass


@config_group.command("info", help="Display information about your current project")
def display_info():
    import toml
    from pyhectiqlab.auth import is_authenticated
    from pyhectiqlab.settings import getenv

    if not is_authenticated():
        click.secho("You need to authenticate first.", fg="red")
        return

    configs_path = getenv("HECTIQLAB_CONFIGS", os.path.expanduser("~/.hectiq-lab/configs.toml"))
    with open(configs_path, "r") as f:
        configs = toml.load(f)

    click.secho("🔧 Configuration for your projects.")
    for project, config in configs.items():
        click.secho(f"[{project}]", fg="green")
        for k, v in config.items():
            click.secho(f"  - {k}: {v}", fg="blue")


@config_group.command("configure", help="Configure the current project")
@click.option("--project", help="Project name", default=None)
@click.option("--repos", help="Repos to be used, separated by commas.", default=None)
@click.option("--model-path", help="Path where the model are saved.", default=None)
@click.option("--dataset-path", help="Path where the dataset are saved.", default=None)
@click.option("--configs-path", help="Path where the configs are saved.")
@click.option("--allow-dirty", help="Whether to allow dirty repos.", is_flag=True)
def configure(
    project: Optional[str],
    repos: Optional[str],
    model_path: Optional[str],
    dataset_path: Optional[str],
    configs_path: Optional[str],
    allow_dirty: Optional[bool],
):
    import toml

    from pyhectiqlab.auth import is_authenticated
    from pyhectiqlab.settings import getenv

    click.secho("🔧 Configuring your project.")
    if not is_authenticated():
        click.secho("You need to authenticate first.", fg="red")
        return

    info = {}
    info["project"] = click.prompt("Project name", type=str) if project is None else project
    if info["project"] is None:
        click.secho("Project name is required.", fg="red")
        return

    info["allow_dirty"] = (
        click.prompt("Allow dirty repos", type=bool, show_default=True) if allow_dirty is None else allow_dirty
    )

    info["repos"] = (
        click.prompt("Repos to be used, separated by commas", type=str, default="", show_default=True)
        if repos is None
        else repos
    ) or None
    if info["repos"] is not None:
        info["repos"] = info["repos"].split(",")

    info["model_path"] = (
        click.prompt("Path to the model", type=str, show_default=True, default="")
        if model_path is None
        else model_path
    ) or None
    if info["model_path"] is not None:
        info["model_path"] = os.path.abspath(info["model_path"])

    info["dataset_path"] = (
        click.prompt("Path to the dataset", type=str, show_default=True, default="")
        if dataset_path is None
        else dataset_path
    ) or None
    if info["dataset_path"] is not None:
        info["dataset_path"] = os.path.abspath(info["dataset_path"])

    # Writing to the configs file
    configs_path = configs_path or getenv("HECTIQLAB_CONFIGS", os.path.expanduser("~/.hectiq-lab/configs.toml"))
    with open(configs_path, "r") as f:
        configs = toml.load(f)
    info = {k: v for k, v in info.items() if v is not None}
    if info["project"] not in configs:
        configs[info["project"]] = {}

    for k, v in info.items():
        if v is None:
            info.pop(k)
        if k == "project":
            continue
        if k in configs[info["project"]] and configs[info["project"]][k] == v:
            continue
        elif k in configs[info["project"]]:
            click.secho(f"- {k}={configs[info['project']][k]}.", fg="red")
        click.secho(f"+ {k}={v}.", fg="green")
        configs[info["project"]][k] = v

    with open(configs_path, "w") as f:
        toml.dump(configs, f)
    click.secho("✅ Configuration saved.", fg="green")
    conda_env = getenv("CONDA_PREFIX_2")

    if conda_env is None or not click.prompt(
        f"Do you want to sync the configuration to your conda environment ({conda_env})?",
        type=bool,
        default=True,
        show_choices=True,
    ):
        return

    # Syncing the configuration to the conda environment
    env_sh = os.path.join(conda_env, "etc/conda/activate.d/env_vars.sh")
    with open(env_sh, "r") as f:
        lines = f.readlines()

    def find(lines, prefix):
        val = list(filter(lambda x: x.startswith(prefix), lines))
        if len(val) == 0:
            return None
        return val[0]

    begin = lines.index("# Hectiq Lab configuration\n") if "# Hectiq Lab configuration\n" in lines else len(lines)
    end = lines.index("# End configuration\n") if "# End configuration\n" in lines else len(lines)

    config_lines = ["# Hectiq Lab configuration\n"]
    config_lines.append(f"export HECTIQLAB_PROJECT='{info['project']}'\n")
    if "allow_dirty" in info:
        config_lines.append(f"export HECTIQLAB_ALLOW_DIRTY={int(info['allow_dirty'])}\n")

    if "repos" in info:
        config_lines.append(f"export HECTIQLAB_REPOS='{','.join(info['repos'])}'\n")
    if "model_path" in info:
        config_lines.append(f"export HECTIQLAB_MODELS_DOWNLOAD='{info['model_path']}'\n")
    if "dataset_path" in info:
        config_lines.append(f"export HECTIQLAB_DATASETS_DOWNLOAD='{info['dataset_path']}'\n")
    config_lines.append("# End configuration\n")

    with open(env_sh, "w") as f:
        f.writelines(lines[:begin] + config_lines + lines[end:])
    click.secho("✅ Configuration synced to conda environment.", fg="green")
