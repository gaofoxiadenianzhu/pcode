from pyhdfs import HdfsClient

fs = HdfsClient(hosts='centosserver1:50070', user_name='root')
root_dir = fs.get_home_directory()
print(root_dir)
