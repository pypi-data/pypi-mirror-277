import random
from typing import Dict
from emotion_detective.logger.logger import setup_logging

def adjust_hyperparameters(current_hyperparameters: Dict[str, float]) -> Dict[str, float]:
    """
    Adjust hyperparameters randomly within predefined ranges.

    Args:
        current_hyperparameters (Dict[str, float]): Dictionary containing current hyperparameters.

    Returns:
        Dict[str, float]: Dictionary containing adjusted hyperparameters.
        
    Author: Martin Vladimirov
    """
    logger = setup_logging()
    
    logger.info("Adjusting hyperparameters.")
    hyperparameter_ranges = {
        'MAX_LEN': (128, 512),
        'TRAIN_BATCH_SIZE': (16, 64),
        'VALID_BATCH_SIZE': (16, 64),
        'TEST_BATCH_SIZE': (16, 64),
        'EPOCHS': (1, 5),
        'LEARNING_RATE': (1e-6, 1e-4),
        'WEIGHT_DECAY': (0.0001, 0.01)
    }

    # Adjust hyperparameters within specified ranges
    for param, (min_val, max_val) in hyperparameter_ranges.items():
        current_hyperparameters[param] = random.uniform(min_val, max_val)

    return current_hyperparameters

