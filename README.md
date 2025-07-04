# 🚀 Мониторинговая платформа на Django + DRF

## 🎯 Цель проекта
Демонстрация комплексной интеграции современных инструментов в Django-приложение:
- **Оркестрация**: Kubernetes-развёртывание с кастомными манифестами
- **Мониторинг**: Prometheus для сбора метрик + Grafana для визуализации
- **Асинхронные задачи**: Celery с Redis как брокером сообщений
- **CI/CD**: Автоматизация с GitHub Actions
- **Производственная среда**: PostgreSQL вместо SQLite

## 📌 Основной функционал

- Регистрация и аутентификация пользователей (JWT)
- CRUD для задач, с правами доступа (IsOwner)
- Фильтрация и поиск задач
- Автоматическое удаление просроченных задач
- Отправка напоминаний по задачам (Celery)
- Экспорт в CSV
- Метрики Prometheus + Grafana (в Docker Compose)
- Kubernetes-манифесты

## 🛠️ Технологический стек

- **Backend**: Django 5, Django REST Framework
- **Auth**: JWT (djangorestframework-simplejwt)
- **Database**: SQLite (по умолчанию), PostgreSQL (в production)
- **Background tasks**: Celery + Redis
- **Monitoring**: Prometheus + Grafana
- **Документация**: drf-spectacular (OpenAPI)
- **Deployment**: Docker, Docker Compose, Kubernetes
- **Тестирование**: pytest, pytest-django, coverage
- **CI/CD**: GitHub Actions

## 🚀 Запуск проекта

### ⚙️ Docker Compose

```bash
docker-compose up --build
```

Приложение по умолчанию доступно на: `http://localhost:8000`

### ⚙️ Kubernetes

```bash
# Сборка образа
docker build -t web:latest .

# Настройка Minikube
minikube start
eval $(minikube docker-env)
docker build -t web:latest .

# Применение манифестов
kubectl apply -k k8s

# Проброс портов
kubectl port-forward svc/web 8000:80 -n django-project
kubectl port-forward svc/grafana 3000:3000 -n monitoring
```


## 🧪 Тестирование

```bash
pytest --cov=.
```

* Используется `pytest-django`
* Конфигурация: `pytest.ini`
* Покрытие кода: `pytest-cov`, `coverage`

## 📈 Мониторинг

* Интеграция через `django-prometheus`
* Метрики доступны по `/metrics`
* Готов к подключению Grafana через порт 3000

## 📂 Структура проекта

```
monitoring_platform/
├── accounts/             # Пользователи и аутентификация
├── core/                 # Общая логика и утилиты
├── metrics/              # Интеграция с Prometheus
├── tasks/                # Celery-задачи
├── monitoring_platform/  # Конфигурация Django
├── k8s/                  # Kubernetes-манифесты
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
```

## 🔐 Аутентификация

* JWT-аутентификация через `djangorestframework-simplejwt`
* Ограничение доступа: `IsOwnerPermission` (пользователь может управлять только своими задачами)

## ✅ CI/CD

* CI реализован через **GitHub Actions**
* Проверка кода, запуск тестов и покрытия при каждом push/pull request
* Файлы CI хранятся в `.github/workflows/`

## 🧑‍💻 Автор

**Shestakov Nikita**  
[GitHub](https://github.com/MrMrMops)
