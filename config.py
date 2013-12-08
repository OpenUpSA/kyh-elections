from fabric import api

api.env.hosts = ["adi@code4sa.org:2222"]

code_dir = "/var/www/hood.code4sa.org"
env_dir = "/home/adi/.virtualenvs/hood"
python = "%s/bin/python" % env_dir
pip = "%s/bin/pip" % env_dir
