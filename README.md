# Развертка инфраструктуры с помощью Ansible

## https://github.com/ErickWer0/at-3/

Задание

Создать ansible роли для развертки Elastic Stack или monitoring, создать ansible playbook, применяющий соответствующие роли. Цель мониторинга и сбора логов - nginx на одной из виртуалок (можно использовать развернутый сервис из домашнего задания по IaC.



Технические детали:

Можно выбрать одно из двух:

Elastic Stack роль. Забираем установочные архивы с адресов, представленных на основном сайте. Установить и сконфигурировать Elasticsearch, Kibana, filebeat

Monitoring роль. Выберите Zabbix или Prometheus+Grafana, установите и сконфигурируйте необходимые компоненты для выбранного решения

## Monitoring

Испрльзуется playbook1.yml. Включает в себя следующие роли:
* prometheus
* grafana
* node-exporter
* nginx
* nginx-exporter


![](https://i.imgur.com/RKrc3N8.png)

## Node-exporter
![](https://i.imgur.com/MglMbzV.png)

## Nginx-exporter

![](https://i.imgur.com/8p2hNqR.png)

## Prometheus targets

![](https://i.imgur.com/FZLcRbT.png)


## Drafana
### Node-exporter

![](https://i.imgur.com/TZXtXPM.png)

### Nginx-exporter

![](https://i.imgur.com/yL0vlMM.png)


## Nginx.conf

![](https://i.imgur.com/251sCB8.png)

## Site
![](https://i.imgur.com/xlNtEEg.png)

## Ansible
![](https://i.imgur.com/VEoqzZ6.png)
