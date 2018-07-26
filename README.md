#Zabbix配置示例

##门户用户行为统计（user-activity）

###说明
利用Zabbix的Low Level Discovery功能自动发现Portal中的用户，并对各用户在指定周期内的登录次数进行统计。

###文件列表
* zabbix_agentd.conf    使用UserParmameter配置用户列表指标及用户登录次数统计指标。
* zbx_export_templates.xml  包含了门户监控指标的模板，用户列表指标、用户登录次数指标原型及所用到的宏都在这个模板中定义。
* user-list-discovery.py    查询门户用户列表的Python脚本。
* get-user-login-count.py   统计某用户在特定时间段内登录次数的Python脚本。
---
* zbx-discovery.env.tgz 运行以上两个Python脚本的Python运行环境。

###使用方法
* 准备一台能够访问Portal数据库的主机（并且安装了zabbix-agent）作为运行环境，在这台主机上展开zbx-discovery.env.tgz。
* 将user-list-discovery.py和get-user-login-count.py拷贝到运行环境某目录下。
* 将zabbix_agentd.conf中的UserParameter配置增加到运行环境的zabbix_agentd.conf中，并根据脚本文件和Python环境的路径对UserParameter的参数进行调整。
* 根据Portal数据库的配置调整python脚本中访问数据库的参数。
* 测试脚本是否能正常运行
    zabbix_agentd -t portal.user.list
    zabbix_agentd -t user.login.count[admin,30]
* 将zbx_export_templates.xml导入Zabbix，并链接到为Portal服务器配置的监控主机。
* 观察Portal监控主机的指标（Application为Portal）。



