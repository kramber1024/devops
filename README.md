# Devops

<a href="https://github.com/kramber1024/devops/actions/workflows/mypy.yml" target="_blank"><img src="https://github.com/kramber1024/devops/actions/workflows/mypy.yml/badge.svg" alt="Tests"></a>
<a href="https://github.com/kramber1024/devops/actions/workflows/ruff.yml" target="_blank"><img src="https://github.com/kramber1024/devops/actions/workflows/ruff.yml/badge.svg" alt="Coverage"></a>
<a href="https://github.com/astral-sh/ruff"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json" alt="Ruff"></a>

## Стек технологий и фичи

- 🌐 [**FastAPI**](https://fastapi.tiangolo.com/) для апи.
- 💾 [**PostgreSQL**](https://www.postgresql.org/) для SQL базы данных.
- 🐋 [**Docker**](https://www.docker.com/) для запуска проекта.
- 🏭 CI/CD при помощи [**GitHub Actions**](https://github.com/kramber1024/url-shortener-api/actions/).
- 📝 [**Swagger**](https://swagger.io/) для документации апи.

## Запуск проекта

### Зависимости

- [**Docker**](https://www.docker.com/)

### Запуск

1. Склонировать репозиторий:
```bash
git clone https://github.com/kramber1024/devops.git
```

2. Перейти в папку с проектом:
```bash
cd devops
```

3. Запустить проект:
```bash
docker-compose up --build
```

## Результат

После запуска проекта, вы сможете перейти на **http://localhost:8000/docs**, чтобы увидеть документацию к апи.

### Скриншоты
![image](https://github.com/kramber1024/devops/blob/main/assets/swagger.png?raw=true)

## Лицензия
Этот проект лицензирован по лицензии MIT - см. файл [LICENSE](./LICENSE).
