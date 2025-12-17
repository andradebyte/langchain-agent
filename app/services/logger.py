import logging

logging.basicConfig(
    level=logging.INFO,
    # format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    format='%(levelname)s:     %(message)s'
)

logger = logging.getLogger(__name__)