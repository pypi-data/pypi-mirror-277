from decouple import config

# Hostname for the TCP Orchestrator
TCP_ORCHESTRATOR_HOST: str = config(
    "TCP_ORCHESTRATOR_HOST", cast=str, default="0.0.0.0"
)

# Port for the TCP Orchestrator
TCP_ORCHESTRATOR_PORT: int = config("TCP_ORCHESTRATOR_PORT", cast=int, default=9990)

# Hostname for the Orchestrator Webapp
ORCHESTRATOR_WEBAPP_HOST: str = config(
    "ORCHESTRATOR_WEBAPP_HOST", cast=str, default="0.0.0.0"
)

# Port for the Orchestrator Webapp
ORCHESTRATOR_WEBAPP_PORT: int = config("ORCHESTRATOR_WEBAPP_PORT", cast=int, default=80)

# External URL for the Orchestrator Webapp, useful if behind a reverse proxy
ORCHESTRATOR_WEBAPP_URL: str = config(
    "ORCHESTRATOR_WEBAPP_URL", cast=str, default=ORCHESTRATOR_WEBAPP_HOST
)

# Timeout in seconds for each action from an orchestrated client, after which execution will be aborted
ACTION_TIMEOUT: int = config("ACTION_TIMEOUT", cast=int, default=10)

# Timeout in seconds for a response from the server script, after which execution will be aborted
SERVER_SCRIPT_RESPONSE_TIMEOUT: int = config(
    "SERVER_SCRIPT_RESPONSE_TIMEOUT", cast=int, default=5
)

# Every how often the server will ping the ServerScript to check if it's still connected
HEARTBEAT_TIMEOUT: int = config("HEARTBEAT_TIMEOUT", cast=int, default=3)

# Flag for the challenge
FLAG: str = config("FLAG")

# Maximum number of thread workers allowed to simulate clients
MAX_ORCHESTRATED_CLIENT_WORKERS: int = config(
    "MAX_ORCHESTRATED_CLIENT_WORKERS", cast=int, default=8
)

# Maximum number of simulated clients per execution, per user
MAX_ORCHESTRATED_CLIENTS_PER_USER: int = config(
    "MAX_ORCHESTRATED_CLIENTS_PER_USER", cast=int, default=10
)

# Maximum number of actions per execution
MAX_ACTIONS: int = config("MAX_ACTIONS", cast=int, default=100)
