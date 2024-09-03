# Banka Uygulaması

Bu proje, bir bankacılık uygulamasıdır ve Django ile REST API kullanarak geliştirilmiştir. Müşteri hesap yönetimi, para çekme/yatırma işlemleri ve daha fazlasını destekler. Docker kullanarak uygulamanın taşınabilirliği ve kolay kurulumu sağlanmıştır.

## Gereksinimler
   * Python 3 (Python'ın sisteminize kurulu olduğundan emin olun)
   * Pip (Python paket yöneticisi)
   * Django == 1.11
   * Docker & Docker Compose
   * PostgreSQL

## Django Kurulumu
* İlk olarak çalışacağınız klasörü oluşturun:
  ```
  mkdir banksystem_project
  ```
* Oluşturduğunuz klasöre girin:
  
  ```
    cd banksystem_project
  ```
* Global ortamda Django'yu kurmak için pip'i kullanabilirsiniz:
* 
    ```
    pip install django==1.11
    ```
* Şimdi Django projenizi oluşturun:
  
  ```
   django-admin startproject bank
  ```
### Django Uygulaması Oluşturma

* Django projenizin kök dizininde (yani manage.py dosyasının bulunduğu dizinde) şu komutu çalıştırın:
  
```
python manage.py startapp api

```
Bu komut, api adında bir uygulama oluşturacaktır. Proje dosya yapınız aşağıdaki gibi görünecektir:

 ```
[bank]/
├── [bank]/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
|____[api]/
|    |__ __init__.py
|    |__ models.py
|    |__ views.py
|    |__[migrations]/
|    |  |___ __init__.py
|    |
|    |__admin.py
|    |__tests.py
|
└── manage.py

```
Api uygulamasını settings.py dosyanıza ekleyin.

  ```
  INSTALLED_APPS = [
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'api',
]
```
## Rest Framework Kurulumu
* pip kullanarak kurulum yapabilirsiniz.

```
pip install djangorestframework
pip install django-filter  # Filtreleme desteği için.
```
* Settings.py dosyanızda, INSTALLED_APPS ayarınıza 'rest_framework' ekleyin.
  
```
INSTALLED_APPS = (
    ...
    'rest_framework',
)
```
### Projenin Çalıştırılması
* Veritabanını aşağıdaki komut ile yükleyin.

```
python3 manage.py migrate

```
* Projeyi istediğiniz IP adresi ve portta çalıştırmak için aşağıdaki komutu kullanabilirsiniz.
```
python3 manage.py runserver <ip adresi>:<port numarası>
```
* Sunucuyu başlattıktan sonra tarayıcınızda ` http:// <ip adresi : port numarası> ` adresine giderek projeyi görebilirsiniz.

## Docker Kurulumu
* Öncelikle, Docker'ı sisteminize kurmanız gerekiyor. Eğer Docker yüklü değilse, resmi [Docker](https://docs.docker.com/engine/install/) sitesinden işletim sisteminize uygun olanı indirip yükleyebilirsiniz.
* Projenizin kök dizininde docker-compose.yml adlı bir dosya oluşturun.
* Docker'da gizli bilgileri saklamak için .env dosyasını oluşturup bu  dosyaya IP adresi ve port gibi bilgileri ekleyebilrsiniz.
* Docker ve Docker Compose kurulumları tamamlandıktan sonra, terminalde projenizin kök dizinine gidin ve aşağıdaki komutu çalıştırın:
  
```
docker-compose up --build
```
* Konteynerlerin çalıştığından emin olmak için aşağıdaki komutu kullanabilirsiniz:
  
```
docker ps
```
* Konteynerin içine girmek için şu komutu kullanabilirsiniz:
  
```
docker exec -it <container_name> /bin/bash
```
