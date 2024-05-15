from fabric.api import env, run, task

env.hosts = ['54.236.8.64', '100.24.72.30']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'

@task
def check_mysql_version():
    run("mysql --version")

@task
def check_mysql_access():
    result = run("mysql -uholberton_user -pprojectcorrection280hbtn -e 'SHOW GRANTS FOR \"holberton_user\"@\"localhost\";'")
    print(result)

# Run the tasks
check_mysql_version()
check_mysql_access()
