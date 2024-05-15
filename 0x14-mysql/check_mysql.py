from fabric.api import env, run, task, settings

env.hosts = ['54.236.8.64', '100.24.72.30']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'

@task
def check_mysql_grants():
    with settings(warn_only=True):
        result = run("mysql -uholberton_user -pprojectcorrection280hbtn -e 'SHOW GRANTS FOR \"holberton_user\"@\"localhost\";'")
        print(result)

@task
def check_mysql_table_exists():
    with settings(warn_only=True):
        result = run("mysql -uholberton_user -pprojectcorrection280hbtn -e 'USE tyrell_corp; SELECT * FROM nexus6;'")
        print(result)
