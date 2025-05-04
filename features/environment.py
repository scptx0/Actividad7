def before_scenario(context, scenario):
    from unittest.mock import MagicMock
    from src.belly import Belly
    from datetime import datetime
    
    fake_clock = MagicMock()
    fake_clock.return_value = datetime(2025, 5, 4, 12, 0, 0)
    context.belly = Belly(clock_service=fake_clock)