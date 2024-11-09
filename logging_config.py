
# logging_config.py - Centralized Logging Setup for Firewall Rule Cleaner Tool

import logging

# Configure logging settings
def setup_logging(log_file="firewall_rule_cleaner.log"):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
    logging.info("Logging setup complete.")
