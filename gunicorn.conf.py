workers = 4
timeout = 120
max_requests = 1000  # Restart worker after handling 1000 requests
max_requests_jitter = 50  # Add some randomness to prevent all workers restarting at the same time