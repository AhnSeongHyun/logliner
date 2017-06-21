logliner 
========

- find a keyword in multiple log files
- sort log datetime created by user-defined `BaseDateExtractor` subclass 
- present log files according to datetime ascending. 

### install 
```shell
$ python setup.py install 
```

### run 

```shell

$ logliner 
usage: logliner [-h] [-c C]

optional arguments:
  -h, --help  show this help message and exit
  -c C        conf file(.yaml)


```

```shell
$ cd ./example        
$ logliner -c ./conf.yaml
```

### config

 - Using `yaml` format. 

```yaml
input:
  path:
    - ./log_files/a.log
    - ./log_files/b.log
output:
    format: file
    path: ./result/report.txt

q : 20170530145147dkjvosuiier
date_extractor: custom_date_extractor.CustomDateExtractor
```

- input : file list 

- output 
    - format : file | html | stdout 
    - path : file path (stdout not required)

- q : searching keyword 
- date_extractor : user-defined `BaseDateExtractor` subclass, `my_package.my_module.MyClass`

