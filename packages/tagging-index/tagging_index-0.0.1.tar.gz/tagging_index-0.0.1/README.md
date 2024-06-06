# tagging Index lib

## initialize account and environment

- Install Aliyun CLI: [Install guide](https://help.aliyun.com/zh/cli/installation-guide)
- run the aliyun configure command to setup account

``` configure
$ aliyun configure
Configuring profile 'default' ...
Aliyun Access Key ID [None]: <Your AccessKey ID>
Aliyun Access Key Secret [None]: <Your AccessKey Secret>
Default Region Id [None]: cn-zhangjiakou
Default output format [json]: json
Default Language [zh]: zh
```

- install pyodps: `pip install pyodps`

## initialize maxcompute instance

- run `python maxcompute/init_maxcompute.py`  in terminal to initialize the maxcompute environment, only need to run once
- use release_tag.ipynb to validate tag config and upload to new version
