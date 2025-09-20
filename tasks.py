from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/index.py", pty=True)

@task
def test(ctx):
    ctx.run("PYTHONPATH=src pytest", pty=True)

@task
def coverage(ctx):
    ctx.run("PYTHONPATH=src coverage run --branch -m pytest src", pty=True)

@task(coverage)
def coverage_report(ctx):
    ctx.run("PYTHONPATH=src python3 -m coverage html", pty=True)

@task
def autopep8(ctx):
    ctx.run("autopep8 --in-place --recursive src", pty=True)

@task
def lint(ctx):
    ctx.run("pylint src", pty=True)
