logliner
========

- find a keyword in multiple log files
- sort log datetime created by user-defined `BaseDateExtractor`' subclass 
- present log files according to datetime ascending. 


### config.yaml 

 - Using `yaml` format. 

```yaml
input:
    - ./log_files/a.log
    - ./log_files/b.log
output:
    format: file
    path: ./result/report.txt

q : 201705301451479331561400
date_extractor: date_extractor.custom_date_extractor.CustomDateExtractor
```

- input : file list (unlimited)

- output 
    - format : file | html | stdout 
    - path : file path (stdout not required)

- q : searching keyword 
- date_extractor : user-defined `BaseDateExtractor`' subclass, `my_package.my_module.MyClass`
