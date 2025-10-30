# src/utils/logger.py
import logging
import os

# Make sure logs folder exists
os.makedirs("logs", exist_ok=True)

# Configure logging settings
logging.basicConfig(
    filename="logs/system.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_action(action, student_id=None):
    if student_id:
        logging.info(f"{action} - Student ID: {student_id}")
    else:
        logging.info(action)
