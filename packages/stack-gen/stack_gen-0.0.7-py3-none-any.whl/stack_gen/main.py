import click
import os


@click.command()
@click.option(
    "--template",
    "-t",
    type=click.Choice(["fastapi", "vuejs"]),
    prompt="Template to generate",
    help="The name of the template to generate: fastapi | vuejs",
)
@click.option("--url", help="GIT url of the template")
@click.option("--github_access_token", "-gac", help="GITHUB access token")
def main(template, url, github_access_token):
    os.system(f"git clone git@github.com:hourlier96/{template}-generator.git --quiet")
    os.system(
        f"python3 -m pip install -r {template}-generator/requirements.txt --quiet",
    )

    if github_access_token:
        with open(
            f"{template}-generator/app/{{{{cookiecutter.project_slug}}}}/.env", "a+"
        ) as file:
            file.write(f'\nGITHUB_ACCESS_TOKEN="{github_access_token}"')

    os.system(f"cookiecutter {template}-generator/app")
    os.system(f"rm -rf {template}-generator")
    


if __name__ == "__main__":
    main()
