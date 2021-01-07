# flaskmana

#migrate 步骤
1. python manage.py db init  # 第一次初始化时用  
2. 记得在写完model的class后, 导入在migrate的py文件中  
3. python manage.py db migrate  #每次修改后执行 再执行第4步  
4. -- 更新用 python manage.py db upgrade  

创建迁移仓库#  
这个命令会创建migrations文件夹，所有迁移文件都放在里面。  
python manage.py db init   # 将database.py替换为有manager.run()的执行文件  
创建迁移脚本#  
自动创建迁移脚本有两个函数  
upgrade()：函数把迁移中的改动应用到数据库中。  
downgrade()：函数则将改动删除。  
自动创建的迁移脚本会根据模型定义和数据库当前状态的差异，生成upgrade()和downgrade()函数的内容。  
对比不一定完全正确，有可能会遗漏一些细节，需要进行检查  
python manage.py db migrate -m 'initial migration'  # 第一次迁移不要使用 - m  
更新数据库#  
python manage.py db upgrade  
返回以前的版本#  
可以根据history命令找到版本号,然后传给downgrade命令:  
python manage.py db history  

输出格式：<base> ->  版本号 (head), initial migration  
回滚到指定版本  
python manage.py db downgrade 版本号  


# 安装 pip install flask-jwt-extended  
# 安装 pip install flask-restful  

