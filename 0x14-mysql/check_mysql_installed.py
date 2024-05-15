from fabric.api import env, run

env.hosts = ['54.236.8.64', '100.24.72.30']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'

def check_mysql_version():
    version = run('mysql --version')
    if 'Distrib 5.7' in version:
        print(f"MySQL 5.7 is installed on {env.host}. Version: {version}")
    else:
        print(f"MySQL 5.7 is not installed on {env.host}. Version: {version}")

for host in env.hosts:
    env.host_string = host
    check_mysql_version()
