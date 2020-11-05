# ServerStatBot 
![](tests/example1.jpg)
该项目是为了定时(周期性)获取某些服务器的健康状态（通过http协议，访问指定url的方式）。

并通过钉钉机器人（配置webhook）的上报健康状态，格式为`MarkDown`。

对于非`200`的状态码的服务器，发出异常警告⚠


## 项目依赖
本项目基于`guniflask`创建，相关依赖
见[requirements/app.txt](requirements/app.txt)文件
[gunicorn手册](https://docs.gunicorn.org/en/stable/settings.html)

## 参数配置
参数文件位于`conf/app.yml`文件和`server_stat_bot/config/security_config.py`文件中，功能如下：

| 参数 | 注释 | 样例 |
| :----: | :----: | :----: |
| DINGTALK_WEBHOOK_URL|钉钉机器人的webhook地址|  "https://oapi.dingtalk.com/robot/send?access_token=7e1c56b0r2dtc9ze9ct4553fe1490067be780476e4fz45v061c3dz3e079f8e"|
| SQLALCHEMY_DATABASE_URI|mysql(pymysql驱动)的url|  "mysql+pymysql://root:123456@localhost:3306/test?charset=UTF8MB4"|
| FETCH_TIME_MIN_PLAN|多少分钟为计划周期访问特定服务器，获取健康状态| 5 |
| DES_WEB_LIST|目标服务器地址，格式为yaml List,一行一个 | - "http://localhost:8000/health" |
| DINGTALK_AT_ALL| 是否在钉钉消息中，at所有人（true/false） | false |
| DINGTALK_TITLE| 钉钉消息的标题 | "服务器健康报警" |

* mysql表配置见下

## mysql配置
每一次获取的信息都会存入mysql数据库。
mysql的表结构如下，若修改表结构后需要执行```sh bin/manage table2model```
```sql
create table record_history
(
	id int auto_increment
		primary key,
	server_address varchar(256) not null,
	serverStatCode varchar(10) null,
	fetchTime datetime not null,
	remark varchar(512) null,
	dingtalkRespStatCode varchar(10) not null,
	dingtalkRespText varchar(1024) not null
);
```


## 启动工程
1. 安装相关依赖，保证`guniflask-cli`正常安装
2. 配置你的`mysql`地址,并创建表
3. 运行``` sh bin\manage debug ```测试，或者``` sh bin\manage start ```正式运行
