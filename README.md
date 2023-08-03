# Docker Sandbox

Sandbox environment to study Airflow

```
docker compose up
```

```
mkdir -p ./dags ./logs ./plugins ./config ./utils
echo -e "AIRFLOW_UID=$(id -u)" > .env
```