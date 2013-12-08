from fabric.operations import local, run
from fabric import api
import os
import config

def deploy():
    with api.cd(config.code_dir):
        api.run("git pull origin master")
        api.run("%s install -r %s/requirements.txt --quiet" % (config.pip, config.code_dir))

        api.sudo("supervisorctl restart hood")

